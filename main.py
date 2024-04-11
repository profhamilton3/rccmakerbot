def on_received_number(receivedNumber):
    basic.clear_screen()
    if receivedNumber == 1:
        wuKong.set_all_motor(100, 100)
    elif receivedNumber == 0:
        wuKong.set_all_motor(0, 0)
    else:
        wuKong.stop_all_motor()
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