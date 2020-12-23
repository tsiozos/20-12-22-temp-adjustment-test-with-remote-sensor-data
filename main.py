radio.set_group(99)
radio.set_transmit_power(7)
showTemp = False
transmitTemp = False
sensorDataCount = 0
lastTemp = input.temperature()

def onSet_interval_interval():
    global sensorDataCount, transmitTemp, lastTemp
    if sensorDataCount == 0:
        lastTemp = input.temperature()/5
    else:
        lastTemp = lastTemp + input.temperature()/5
        if sensorDataCount == 4:
            if transmitTemp:
                radio.send_value("temp", lastTemp * 100)
                led.plot(0,0)
                basic.pause(100)
                led.unplot(0, 0)

    sensorDataCount = (sensorDataCount+1) % 5


control.set_interval(onSet_interval_interval, 5000, control.IntervalMode.INTERVAL)


def on_received_value(name, value):
    global showTemp
    if showTemp:        #show the temperature on receivers display
        if name=="temp":
            value = value / 100
            basic.show_number(value)
            stationID = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
            print(str(stationID)+": "+str(radio.received_packet(RadioPacketProperty.TIME/1000))+": "+str(value))
            basic.pause(1000)
            basic.clear_screen()
radio.on_received_value(on_received_value)

def on_button_pressed_a():
    global showTemp
    showTemp = not showTemp
    if showTemp:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
    basic.pause(1000)
    basic.clear_screen()

def on_button_pressed_b():
    global transmitTemp
    transmitTemp = not transmitTemp
    if transmitTemp:
        basic.show_icon(IconNames.LEFT_TRIANGLE)
    else:
        basic.show_icon(IconNames.NO)
    basic.pause(1000)
    basic.clear_screen()

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)