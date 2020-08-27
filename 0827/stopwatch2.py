import time
import RPi.GPIO as GPIO

from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment(address=0x70)

segment.begin()

counter = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(24) == False:
			GPIO.wait_for_edge(24, GPIO.RISING)
			print("Start")
			break

	while(True):
		start = time.perf_counter()
		time.sleep(0.01)
		end = time.perf_counter()
		
		segment.clear()

		counter += (end-start)
	   
		ttime = str(counter).split(".")

		sec1 = int(int(ttime[0])/10)
		sec2 = int(ttime[0])%10
		mis1 = int(int(ttime[1][:2])/10)
		mis2 = int(ttime[1][:2])%10

	   # print("perf_counter:{0}{1}:{2}{3} ".format(sec1, sec2, mis1, mis2))

		segment.set_digit(0, sec1)
		segment.set_digit(1, sec2)
		segment.set_digit(2, mis1)
		segment.set_digit(3, mis2)

		segment.set_colon(1)
		segment.write_display()
		
		if GPIO.input(24) == False:
			print("lap:{0}{1}:{2}{3} ".format(sec1, sec2, mis1, mis2))
			GPIO.wait_for_edge(24, GPIO.BOTH)
			
		if GPIO.input(27) == False:
			print("End")
			print("End:{0}{1}:{2}{3} ".format(sec1, sec2, mis1, mis2))
			break
			
    
except KeyboardInterrupt:
	GPIO.cleanup()
	print()
	
finally:
	GPIO.cleanup()
	segment.clear()
	segment.write_display()
    
