import requests
#import uvmAgencies
#import uvmArrivals
#import uvmRoutes
#import uvmStops
#import uvmVehicles
import RPi.GPIO as GPIO
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


BUTTON1 = 16
BUTTON2 = 20
BUTTON3 = 21
BUTTON4 = 26

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90,
                     rotate=0, blocks_arranged_in_reverse_order=False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

routes = ['Redston Express', 'On-Campus']

with canvas(device) as draw:
    text(draw, (0, 0), "Welcome to Catbus+       Press 1 to Start", fill="white", font=proportional(CP437_FONT))

while True:
    for x in routes:
        with canvas(device) as draw:
                text(draw, (0, 0), x, fill="white", font=proportional(CP437_FONT))
        if GPIO.int(BUTTON1) == GPIO.LOW:
            with canvas(device) as draw:
                text(draw, (0, 0), "Hello", fill="white", font=proportional(CP437_FONT))
            if GPIO.input(BUTTON2) == GPIO.LOW:
                with canvas(device) as draw:
                    text(draw, (0, 0), "2", fill="white", font=proportional(CP437_FONT))
            if GPIO.input(BUTTON3) == GPIO.LOW:
                with canvas(device) as draw:
                    text(draw, (0, 0), "3", fill="white", font=proportional(CP437_FONT))
            if GPIO.input(BUTTON4) == GPIO.LOW:
                with canvas(device) as draw:
                    text(draw, (0, 0), "4", fill="white", font=proportional(CP437_FONT))

'''redstone_dict = {'Coolidge': 4169218,
                 'Royal Tyler Theatre': 4164154,
                 'Billings Library': 4164158,
                 'Billings Library': 4164158}
                 
querystring = {"agencies":"603","callback":"call"}

headers = {
	"X-RapidAPI-Key": "83d18cd3a1msh5007a4981f06aacp1aa353jsnd6a69e405ee9",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

routes = ['WDW', 'On-Campus']

def route_selection(i):
    while True:
        with canvas(device) as draw:
               text(draw, (0, 0), routes[i], fill="white", font=proportional(CP437_FONT))
    
    


def run():
    
    while True:
     time.sleep(0.15)

     if GPIO.input(BUTTON1) == GPIO.LOW:
        route_select_count = route_select_count + 1
        route_selection(route_select_count)
        

run()

for i in range (0,1):
    if uvmVehicles.response.json().get('data').get('603')[i]:
        arrivals.append(uvmVehicles.response.json().get('data').get('603')[i].get('route_id'))   '''
    
    

