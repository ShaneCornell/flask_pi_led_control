#
# Exercise 1
# Write a class to encapsuate the functionality of your Raspberry Pi LED contraption. It should do the following:
#
# Initialize itself by setting up all the LEDs we need to control.
# Provide a led_on() method to turn on individual LEDs
# Provide a led_off() method to turn off individual LEDs
# Provide a race_up() method to make the leds race up
# Provide a race_down() method to make the leds race down
# Provide a dance_randomly() method to make the leds dance on and off randomly
# Your class should also include tests when the file is run by itself using the if name == "main" trick you've learned.

#from gpiozero import LED
from time import sleep
import random


class PiLedContraption:
    _led = []
    _valid_leds = []
    _physical_leds = []
    _led_index = []
    _sleep = .01

    def __init__(self):
        print("initializing")
        #setup leds
        self._valid_leds = [1, 2, 3, 4]

        for i in self._valid_leds:

            #self._physical_leds.append(LED(i))
            self._physical_leds.append((i))

        self._led_index = [0, 1, 2, 3]

    def led_on(self, led_number):
        if led_number in self._led_index:
           print(' self._physical_leds[led_number].on()')
           print("led {} is on".format(led_number))
        else:
            print("led{} is an invalid number".format(led_number))


    def led_off(self, led_number):
        if led_number in self._led_index:
           print(' self._physical_leds[led_number].off()')
           print("led {} is off".format(led_number))
        else:
            print("led{} is an invalid led".format(led_number))

    def raceup(self):
        for i in self._physical_leds:
            print('i.on()')
            sleep(self._sleep)
            print('i.off()')

    def racedown(self):
        for i in reversed(self._physical_leds):
            print('i.on()')
            sleep(self._sleep)
            print('elem.off()')

    def random(self):
        random.seed()
        for i in range (0,20):
            r = random.randint(0,4)
            print('self.led_on(r)")
            sleep(self._sleep)
            print('self.led_off(r))


if __name__=="__main__":

    #Testing Initialization
    test = PiLedContraption()
    print(type(test))

    #testing valid leds
    test.led_on(2)
    test.led_on(20)


    #Individual/Group
    print('test.led.on(1)')
    print('sleep(1)')
    print('test.led.off(1)')

    sleep(1)

    #Testing Race UP
    print('test.raceup()')

    sleep(1)

    #Testing Race Down
    print('test.racedown()')

    sleep(1)

    #Testing Dance
    print('test.dance()')
