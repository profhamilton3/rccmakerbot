radio.onReceivedNumber(function (receivedNumber) {
    if (1 == receivedNumber) {
        basic.showIcon(IconNames.Fabulous)
        wuKong.setAllMotor(100, 100)
        basic.showArrow(ArrowNames.North)
    } else if (2 == receivedNumber) {
        basic.showArrow(ArrowNames.East)
        wuKong.setAllMotor(25, 75)
        basic.pause(250)
    } else if (3 == receivedNumber) {
        basic.showArrow(ArrowNames.West)
        wuKong.setAllMotor(75, 25)
        basic.pause(250)
    } else if (4 == receivedNumber) {
        basic.showArrow(ArrowNames.South)
        wuKong.setAllMotor(-25, -25)
    } else if (5 == receivedNumber) {
        basic.showArrow(ArrowNames.NorthEast)
        wuKong.setAllMotor(60, 20)
        basic.pause(500)
    } else if (6 == receivedNumber) {
        basic.showIcon(IconNames.Umbrella)
        wuKong.setAllMotor(10, 40)
        basic.pause(1000)
    } else if (7 == receivedNumber) {
        basic.showArrow(ArrowNames.SouthWest)
        wuKong.setAllMotor(25, 75)
        basic.pause(500)
    } else if (8 == receivedNumber) {
        basic.showArrow(ArrowNames.SouthEast)
        basic.showIcon(IconNames.Cow)
        wuKong.setAllMotor(75, 15)
        basic.pause(500)
    } else if (9 == receivedNumber) {
        basic.showNumber(5)
    } else if (10 == receivedNumber) {
    	
    } else if (11 == receivedNumber) {
    	
    } else if (12 == receivedNumber) {
        basic.showIcon(IconNames.Butterfly)
        wuKong.setAllMotor(-15, 15)
        basic.pause(2000)
    } else if (13 == receivedNumber) {
        basic.showIcon(IconNames.StickFigure)
        wuKong.setAllMotor(15, -15)
        basic.pause(2000)
    } else if (14 == receivedNumber) {
    	
    } else if (15 == receivedNumber) {
    	
    } else if (0 == receivedNumber) {
        basic.showNumber(0)
    } else {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Funeral), music.PlaybackMode.InBackground)
    }
})
input.onButtonPressed(Button.A, function () {
    wuKong.setAllMotor(50, 50)
    basic.pause(500)
    wuKong.setAllMotor(-10, 50)
    basic.pause(1000)
    wuKong.setAllMotor(73, 34)
    basic.pause(5000)
    wuKong.stopAllMotor()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    wuKong.stopAllMotor()
    basic.showNumber(2)
    radio.sendNumber(2)
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
})
radio.setTransmitPower(7)
radio.setGroup(2)
radio.setFrequencyBand(32)
basic.showNumber(2)
wuKong.setLightMode(wuKong.LightMode.OFF)
