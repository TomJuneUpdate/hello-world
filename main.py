music_play = 0

def on_button_pressed_a():
    global music_play
    if music_play == 1:
        music.stop_all_sounds()
        music_play = 0
    else:
        music._play_default_background(music.built_in_playable_melody(Melodies.BIRTHDAY),
            music.PlaybackMode.IN_BACKGROUND)
        music_play = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    basic.show_string("Love all k69!")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    basic.show_string("UED Xin chao")
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_forever():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        """)
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
