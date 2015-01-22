########
Examples
########

Basic usage
===========

::

    >>> import LNdigitalIO

    >>> LNd = LNdigitalIO.LNdigitals() # creates a LN Digtal object

    >>> LNd.leds[1].turn_on()    # turn on/set high the second LED
    >>> LNd.leds[1].set_high()   # turn on/set high the second LED
    >>> LNd.leds[2].toggle()     # toggle third LED
    >>> LNd.switches[3].value    # check the logical status of switch3
    0
    >>> LNd.relays[0].value = 1  # turn on/set high the first relay

    >>> LNd.output_pins[6].value = 1
    >>> LNd.output_pins[6].turn_off()

    >>> LNd.input_pins[6].value
    0

    >>> LNd.output_port.all_off()
    >>> LNd.output_port.value = 0xAA
    >>> LNd.output_port.toggle()

    >>> bin(LNd.input_port.value)  # fourth switch pressed (logical input port)
    '0b1000'

    >>> bin(LNd.gpiob.value)  # fourth switch pressed (physical input port)
    '0b11110111'

    >>> LNd.deinit_board()  # disables interrupts and closes the file

.. note: Inputs are active low on GPIO Port B. This is hidden in software
   unless you inspect the GPIOB register.

Here are some functions you might want to use if objects aren't your thing::

    >>> import LNdigitalIO as p
    >>> p.init()
    >>> p.digital_write(0, 1)    # writes pin0 high
    >>> p.digital_write(5, 1, 2) # writes pin5 on board2 high
    >>> p.digital_read(4)        # reads pin4 (on board0)
    0
    >>> p.digital_read(2, 3)     # reads pin2 (on board3)
    1
    >>> p.deinit()

.. note: These are just wrappers around the LNdigital object.

Interrupts
==========

Instead of polling for input we can use the :class:`InputEventListener` to
register actions that we wish to be called on certain input events.

    >>> import LNdigitalIO
    >>> def toggle_led0(event):
    ...     event.chip.leds[0].toggle()
    ...
    >>> LNdigital = LNdigitalIO.LNdigitals()
    >>> listener = LNdigitalIO.InputEventListener(chip=LNdigital)
    >>> listener.register(0, LNdigitalIO.IODIR_FALLING_EDGE, toggle_led0)
    >>> listener.activate()

When input 0 is pressed, led0 will be toggled. To stop the listener, call it's
``deactivate`` method:

    >>> listener.deactivate()

The :class:`Event` object has some interesting attributes. You can access them
like so::

    >>> import LNdigitalIO
    >>> LNdigital = LNdigitalIO.LNdigitals()
    >>> listener = LNdigitalIO.InputEventListener(chip=LNdigital)
    >>> listener.register(0, LNdigitalIO.IODIR_RISING_EDGE, print)
    >>> listener.activate()

This would print out the event informaion whenever you unpress switch 0::

    interrupt_flag:    0b1
    interrupt_capture: 0b11111111
    pin_num:           0
    direction:         1
    chip:              <LNdigitalIO.core.LNdigitals object at 0xb682dab0>
    timestamp:         1380893579.447889
