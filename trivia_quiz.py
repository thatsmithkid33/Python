import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT) #red led
GPIO.setup(25, GPIO.OUT) #green led
GPIO.setup(12, GPIO.OUT) #white led
GPIO.setup(15, GPIO.OUT) # 
GPIO.setup(14, GPIO.OUT)
count = 0

 

GPIO.output(12, False)
GPIO.output(25, False)
GPIO.output(23, False)

#  Introduction

print ('Hello. This is Python speaking. Please answer a few questions for me.')
time.sleep(.2)
print ('The color of the light will indicate what subject the question is about.')
time.sleep(.2)
print ('White - Sports, Green - Science, Red - Math, Yellow - Movies, Blue - History')
time.sleep(.2)

#  Correct Flashes

def sportCorrect():
        GPIO.output(12, False)
        time.sleep(.3)
        GPIO.output(12, True)
        time.sleep(.3)
        GPIO.output(12, False)
        time.sleep(.3)
        GPIO.output(12, True)
        time.sleep(.3)
        GPIO.output(12, False)
        time.sleep(.3)
        GPIO.output(12, True)
        time.sleep(.3) 

def scienceCorrect():
        GPIO.output(25, False)
        time.sleep(.3)
        GPIO.output(25, True)
        time.sleep(.3)
        GPIO.output(25, False)
        time.sleep(.3)
        GPIO.output(25, True)
        time.sleep(.3)
        GPIO.output(25, False)
        time.sleep(.3)
        GPIO.output(25, True)
        time.sleep(.3)


select = str(input('Please type in the category you would like: '))
print (select)
        

if select == 'Sports' or 'sports' or 'Sport' or 'sport':
        GPIO.output(12, True)
                
        racingQA = str(input('Where did Chase Elliot get his first Cup Series win in 2018? '))

        if racingQA == 'Watkins Glen' or 'Watkins glen' or 'watkins glen' or 'Watkins Glenn' or 'watkins glenn' or 'Watkins glenn':
                print('CORRECT')
                sportCorrect()
                        
elif select == 'Science' or 'science':
        GPIO.output(25, True)
                
        scienceQA = str(input('Sample Question. Enter "Test": '))

        if scienceQA == 'Test':
                print('CORRECT')
                scienceCorrect()

elif select == 'Math' or 'math':
        GPIO.output(23, True)
        print ('Whuttttt???')
