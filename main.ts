radio.setGroup(99)
radio.setTransmitPower(7)
let showTemp = false
let transmitTemp = false
let sensorDataCount = 0
let lastTemp = input.temperature()
control.setInterval(function onSet_interval_interval() {
    
    if (sensorDataCount == 0) {
        lastTemp = input.temperature() / 5
    } else {
        lastTemp = lastTemp + input.temperature() / 5
        if (sensorDataCount == 4) {
            if (transmitTemp) {
                radio.sendValue("temp", lastTemp * 100)
                led.plot(0, 0)
                basic.pause(100)
                led.unplot(0, 0)
            }
            
        }
        
    }
    
    sensorDataCount = (sensorDataCount + 1) % 5
}, 5000, control.IntervalMode.Interval)
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    if (showTemp) {
        // show the temperature on receivers display
        if (name == "temp") {
            value = value / 100
            basic.showNumber(value)
            console.log("" + radio.receivedPacket(RadioPacketProperty.Time / 1000) + ": " + ("" + value))
            basic.pause(1000)
            basic.clearScreen()
        }
        
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    showTemp = !showTemp
    if (showTemp) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
    
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    transmitTemp = !transmitTemp
    if (transmitTemp) {
        basic.showIcon(IconNames.LeftTriangle)
    } else {
        basic.showIcon(IconNames.No)
    }
    
    basic.pause(1000)
    basic.clearScreen()
})
