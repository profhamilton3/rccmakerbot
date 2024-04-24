def on_received_number(receivedNumber):
    if 1 == receivedNumber:
        basic.show_icon(IconNames.FABULOUS)
        wuKong.set_all_motor(100, 100)
        basic.show_arrow(ArrowNames.NORTH)
    elif 2 == receivedNumber:
        basic.show_arrow(ArrowNames.EAST)
        wuKong.set_all_motor(25, 75)
        basic.pause(250)
    elif 3 == receivedNumber:
        basic.show_arrow(ArrowNames.WEST)
        wuKong.set_all_motor(75, 25)
        basic.pause(250)
    elif 4 == receivedNumber:
        basic.show_arrow(ArrowNames.SOUTH)
        wuKong.set_all_motor(-25, -25)
    elif 5 == receivedNumber:
        basic.show_arrow(ArrowNames.NORTH_EAST)
        wuKong.set_all_motor(60, 20)
        basic.pause(500)
    elif 6 == receivedNumber:
        basic.show_icon(IconNames.UMBRELLA)
        wuKong.set_all_motor(10, 40)
        basic.pause(1000)
    elif 7 == receivedNumber:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
        wuKong.set_all_motor(25, 75)
        basic.pause(500)
    elif 8 == receivedNumber:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.show_icon(IconNames.COW)
        wuKong.set_all_motor(75, 15)
        basic.pause(500)
    elif 9 == receivedNumber:
        basic.show_number(5)
    elif 10 == receivedNumber:
        pass
    elif 11 == receivedNumber:
        pass
    elif 12 == receivedNumber:
        basic.show_icon(IconNames.BUTTERFLY)
        wuKong.set_all_motor(-15, 15)
        basic.pause(2000)
    elif 13 == receivedNumber:
        basic.show_icon(IconNames.STICK_FIGURE)
        wuKong.set_all_motor(15, -15)
        basic.pause(2000)
    elif 14 == receivedNumber:
        pass
    elif 15 == receivedNumber:
        pass
    elif 0 == receivedNumber:
        basic.show_number(0)
    else:
        music._play_default_background(music.built_in_playable_melody(Melodies.FUNERAL),
            music.PlaybackMode.IN_BACKGROUND)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    wuKong.set_all_motor(50, 50)
    basic.pause(500)
    wuKong.set_all_motor(-10, 50)
    basic.pause(1000)
    wuKong.set_all_motor(73, 34)
    basic.pause(5000)
    wuKong.stop_all_motor()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    wuKong.stop_all_motor()
    basic.show_number(2)
    radio.send_number(2)
    music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
        music.PlaybackMode.IN_BACKGROUND)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

radio.set_transmit_power(7)
radio.set_group(2)
radio.set_frequency_band(32)
basic.show_number(2)
wuKong.set_light_mode(wuKong.LightMode.OFF)