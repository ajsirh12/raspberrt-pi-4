import time
import RPi.GPIO as GPIO

from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment(address=0x70)

segment.begin()

counter = 0

SWITCH1 = 24
SWITCH2 = 27
GPIO.setmode(GPIO.BCM)

GPIO.setup(SWITCH1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

flag = False
flag2 = False
flag3 = False

def lap(sec1, sec2, mis1, mis2):
	print("lap:{0}{1}:{2}{3} ".format(sec1, sec2, mis1, mis2))
	#GPIO.wait_for_edge(SWITCH1, GPIO.BOTH)
	return

if __name__ == "__main__":
	try:
		#while True:
			while not flag2:
				if GPIO.input(SWITCH1) == False:
					#GPIO.wait_for_edge(SWITCH1, GPIO.RISING)
					print("Start")
					flag2 = True
					break
			
			while flag2:
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

				segment.set_digit(0, sec1%10)
				segment.set_digit(1, sec2)
				segment.set_digit(2, mis1)
				segment.set_digit(3, mis2)

				segment.set_colon(sec2%2)
				segment.write_display()

				if GPIO.input(SWITCH1) == False:
					if flag == True:
						print("lap:{0}{1}:{2}{3} ".format(sec1, sec2, mis1, mis2))
						flag = False
					#GPIO.wait_for_edge(SWITCH1, GPIO.BOTH)
				else:
					flag = True
				
				if GPIO.input(SWITCH2) == False:
					print("End:{0}{1}:{2}{3} ".format(sec1, sec2, mis1, mis2))
					flag2 = False
					break
					
		
	except KeyboardInterrupt:
		print()
		
	finally:
		GPIO.cleanup()
		segment.clear()
		segment.write_display()

