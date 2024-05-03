import RPi.GPIO as GPIO
import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

import requests

url = "https://transloc-api-1-2.p.rapidapi.com/arrival-estimates.json"

querystring = {"agencies":"603","callback":"call"}

headers = {
	"X-RapidAPI-Key": "83d18cd3a1msh5007a4981f06aacp1aa353jsnd6a69e405ee9",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"}

response = requests.get(url, headers=headers, params=querystring)


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)


BUTTON1 = 16
BUTTON2 = 20
BUTTON3 = 21
BUTTON4 = 26

while True:
     time.sleep(0.15)

     GPIO.setmode(GPIO.BCM)
     GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

     if GPIO.input(BUTTON1) == GPIO.LOW:
          with canvas(device) as draw:
               text(draw, (0, 0), "MSH", fill="white", font=proportional(CP437_FONT))

     GPIO.setmode(GPIO.BCM)
     GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

     if GPIO.input(BUTTON2) == GPIO.LOW:
          with canvas(device) as draw:
               text(draw, (0, 0), "WDW", fill="white", font=proportional(CP437_FONT))

     GPIO.setmode(GPIO.BCM)
     GPIO.setup(BUTTON3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

     if GPIO.input(BUTTON3) == GPIO.LOW:
          msg = "hello"
          show_message(device, msg, fill="white", font=proportional(CP437_FONT))
          time.sleep(1)

     GPIO.setmode(GPIO.BCM)
     GPIO.setup(BUTTON4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

     if GPIO.input(BUTTON4) == GPIO.LOW:
          if GPIO.input(BUTTON4) == GPIO.LOW:
          msg = "hello"
          show_message(device, msg, fill="white", font=proportional(CP437_FONT))
          time.sleep(1)
          
