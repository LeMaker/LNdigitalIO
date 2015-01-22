import LNdigitalIO


def switch_pressed(event):
    event.chip.output_pins[event.pin_num].turn_on()


def switch_unpressed(event):
    event.chip.output_pins[event.pin_num].turn_off()


if __name__ == "__main__":
    LNdigital = LNdigitalIO.LNdigitals()

    listener = LNdigitalIO.InputEventListener(chip=LNdigital)
    for i in range(4):
        listener.register(i, LNdigitalIO.IODIR_ON, switch_pressed)
        listener.register(i, LNdigitalIO.IODIR_OFF, switch_unpressed)
    listener.activate()
