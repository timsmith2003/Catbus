import RPi.GPIO as GPIO
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
import uvmRoutes
import uvmVehicles
import uvmArrivals
import requests



serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90,rotate=0, blocks_arranged_in_reverse_order=False)


BUTTON1 = 16
BUTTON2 = 20
BUTTON3 = 21
BUTTON4 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#msg = "Welcome to catbus+"
#show_message(device, msg, fill="white", font=proportional(CP437_FONT))
#time.sleep(1)

vehicles = []
vehicle_speed = []

#index for vehicle scroll
count = 0
# stop index for redstone
count1 = 0
#stop index for on camp
count3 = 0
#speed vehicle list index 
count4 = 0
#vehicle index for initialization
count5 = 0
# redstone number
# on campus then redstone speed number
count6 = 1
count7 = 1
#index for vehicle speed scroll
count8 = 0


redstone_dict = {'Coolidge Hall': 4169218,
                 'Royal Tyler Theatre': 4164154,
                 'Billings Library': 4164158,
                 'Waterman': 4169222}
redstone_stops =['Coolidge Hall', 'Royal Tyler Theatre', 'Billings Library', 'Waterman']

redstone_arrivals = {'Billings Library':0, 'Coolidge Hall':1,'Waterman':2, 'Royal Tyler Theatre':3}

onCampus_dict = {'Mercy Hall': 4164166,
                 'McAuley': 4164162,
                 'STEM': 4232128,
                 'CCRH': 4232130,
                 'Marsh Life':4223882,
                 'Given/Rowell':4164182,
                 'Davis South':4164186,
                 'Living and Learning':4164150,
                 'Harris/Millis':4164142,
                 'University Heights':4164146,
                 'Coolidge Hall':4164190,
                 'Redstone Apts.':4169202,
                 'WDW':4164134,
                 'PFG':4164138,
                 'Royal Tyler Theatre':4164154,
                 'Billings Library':4164158}

onCampus_stops = ['Mercy Hall', 'McAuley', 'STEM', 'CCRH', 'Marsh Life', 'Given/Rowell', 'Davis South', 'Living and Learning', 'Harris/Millis', 'University Heights', 'Coolidge Hall', 'Redstone Apts.', 'WDW', 'PFG', 'Royal Tyler Theatre', 'Billings Library']

onCampus_arrivals = {'Billings Library':0,'Coolidge Hall':1, 'STEM':2, 'Royal Tyler Theatre':3, 'Marsh Life':4, 'Living and Learning':5, 'Redstone Apts.':6, 'University Heights':7, 'CCRH':8, 'Harris/Millis':9, 'Mercy Hall':10, 'PFG':11, 'WDW':12, 'Davis South':13, 'Given/Rowell':14, 'McAuley':15}

for vehicle in uvmVehicles.response.json().get('data').get('603'):
    if uvmVehicles.response.json().get('data').get('603')[count5].get('route_id') == '4006422' and 'On-Campus' not in vehicles:
        vehicles.append('On-Campus')
        count5 += 1
    if uvmVehicles.response.json().get('data').get('603')[count5].get('route_id') == '4006426' and 'Redstone Express' not in vehicles:
        vehicles.append('Redstone Express')
        count5 += 1
#speed lists maker
for vehicle in uvmVehicles.response.json().get('data').get('603'):
    if uvmVehicles.response.json().get('data').get('603')[count8].get('route_id') == '4006422':
        vehicle_speed.append('On-Campus ' + str(count4))
        count4 += 1
        count7 += 1
    if uvmVehicles.response.json().get('data').get('603')[count8].get('route_id') == '4006426':
        vehicle_speed.append('Redstone express' + str(count4))
        count4 += 1
        count6 += 1 

while True:
    if GPIO.input(BUTTON1) == GPIO.LOW and len(vehicles) == 1:
        msg = vehicles[1]
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
        count = 1
    if GPIO.input(BUTTON1) == GPIO.LOW:
        msg = vehicles[count % len(vehicles)]
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
        count = count + 1

    if GPIO.input(BUTTON2) == GPIO.LOW and 'On-Campus' in vehicles[(count - 1) % len(vehicles)]:
        msg = onCampus_stops[count3 % 16]
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
        count3 = count3 + 1
    if GPIO.input(BUTTON2) == GPIO.LOW and 'Redstone Express' in vehicles[(count - 1) % len(vehicles)]:
        msg = redstone_stops[count1 % 4]
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
        count1 = count1 + 1
    if GPIO.input(BUTTON3) == GPIO.LOW and 'On-Campus' in vehicles[(count-1) % len(vehicles)]:
        url = "https://transloc-api-1-2.p.rapidapi.com/arrival-estimates.json"
        querystring = {"agencies":"603","routes":"4006422","callback":"call"}
        headers = {
             "X-RapidAPI-Key": "83d18cd3a1msh5007a4981f06aacp1aa353jsnd6a69e405ee9",
             "X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
             }
        response = requests.get(url, headers=headers, params=querystring)
        
        msg = response.json().get('data')[onCampus_arrivals[onCampus_stops[(count3-1) % 16]]].get('arrivals')[0].get('arrival_at')
        timer = int(msg[11:13]) % 12
        show_message(device,str(timer) + msg[13:16], fill="white", font=proportional(CP437_FONT))
    
    if GPIO.input(BUTTON3) == GPIO.LOW and 'Redstone Express' in vehicles[(count-1) % len(vehicles)]:
        
        url = "https://transloc-api-1-2.p.rapidapi.com/arrival-estimates.json"
        querystring = {"agencies":"603","routes":"4006426","callback":"call"}
        headers = {
             "X-RapidAPI-Key": "83d18cd3a1msh5007a4981f06aacp1aa353jsnd6a69e405ee9",
             "X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
             }
        response = requests.get(url, headers=headers, params=querystring)
        
        msg = response.json().get('data')[redstone_arrivals[redstone_stops[(count1-1) % 4]]].get('arrivals')[0].get('arrival_at')
        timer = int(msg[11:13]) % 12 
        show_message(device,str(timer) + msg[13:16], fill="white", font=proportional(CP437_FONT))




    #SPEEEDS


    if GPIO.input(BUTTON4) == GPIO.LOW and GPIO.input(BUTTON1) == GPIO.LOW and 'On-Campus' in vehicle_speed[(count8-1) % len(vehicle_speed)]:
        msg = vehicle_speed[count8 % len(vehicles)] + "Speed"
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
        count8 = count8 + 1
    if GPIO.input(BUTTON4) == GPIO.LOW and GPIO.input(BUTTON1) == GPIO.LOW and 'Redstone' in vehicle_speed[(count8-1) % len(vehicle_speed)]:
        msg = vehicle_speed[count8 % len(vehicles)] + "Speed"
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
        count8 = count8 + 1
    if GPIO.input(BUTTON4) == GPIO.LOW and GPIO.input(BUTTON2) == GPIO.LOW:
        url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"
        querystring = {"agencies":"603","callback":"call"}
        headers = {
            "X-RapidAPI-Key": "83d18cd3a1msh5007a4981f06aacp1aa353jsnd6a69e405ee9",
            "X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
            }
        response = requests.get(url, headers=headers, params=querystring)
        msg = response.json().get('data').get('603')[count8-1].get('speed') + 'mph'
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    

    