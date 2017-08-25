import RPi.GPIO as GPIO
import time

def BlinkGreen():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(26,GPIO.OUT)
 for i in range(0,100):
  #print @iterstion @+str(i+1)
  GPIO.output(26,True)
  time.sleep(0.1)
  GPIO.output(26,False)
  time.sleep(0.1)
def BlinkRed():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(21,GPIO.OUT)
 for i in range(0,100):
  #print @iterstion @+str(i+1)
  GPIO.output(21,True)
  time.sleep(0.1)
  GPIO.output(21,False)
  time.sleep(0.1)
 print 'done'
 GPIO.cleanup()
iterations=raw_input('enter no of blinks')
speed=raw_input('enter length of each blink(seconds):')
BlinkGreen()
#Blink(int(iterations),float(speed))
