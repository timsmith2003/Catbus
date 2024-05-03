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

routes = []

count = 0

count1 = 0

count3 = 0

count4 = 0

redstone_dict = {'Coolidge': 4169218,
                 'Royal Tyler Theatre': 4164154,
                 'Billings Library': 4164158,
                 'Waterman': 4164158}
redstone_stops =['Coolidge', 'Royal Tyler Theatre', 'Billings Library', 'Waterman']

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

for vehicle in uvmVehicles.response.json().get('data').get('603'):
    if uvmVehicles.response.json().get('data').get('603')[i].get('route_id') == 4006422:
        count4 = count4 + 1
        




while True:
    if GPIO.input(BUTTON1) == GPIO.LOW:
        msg = routes[count % 2]
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
        count = count + 1
    if GPIO.input(BUTTON2) == GPIO.LOW and count % 2 == 1:
        msg = redstone_stops[count1 % 4]
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
        count1 = count1 + 1
    if GPIO.input(BUTTON2) == GPIO.LOW and count % 2 == 0:
        msg = onCampus_stops[count3 % 15]
        show_message(device, msg, fill="white", font=proportional(CP437_FONT))
        count3 = count3 + 1



    #if GPIO.input(BUTTON4) == GPIO.LOW:
     #   msg = uvmRoutes.response.json().get('data').get('603')[1].get('long_name')
      #  show_message(device, msg, fill="white", font=proportional(CP437_FONT))

#LEAVE BUTTON4 OPEN, THIS WAY YOU CAN HOLD IT AND USE IT TO UNLOCK ANOTHER SET OF BUTTONS
