from time import sleep
import LNdigitalIO


DELAY = 1.0  # seconds


if __name__ == "__main__":
    LNdigital = LNdigitalIO.LNdigitals()
    while True:
        LNdigital.leds[7].toggle()
        sleep(DELAY)
