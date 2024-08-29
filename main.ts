let music_play = 0
input.onButtonPressed(Button.A, function () {
    if (music_play == 1) {
        music.stopAllSounds()
        music_play = 0
    } else {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Birthday), music.PlaybackMode.InBackground)
        music_play = 1
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showString("Love all k69!")
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.showString("UED Xin chao")
})
basic.forever(function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showIcon(IconNames.SmallDiamond)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        `)
    basic.showIcon(IconNames.Heart)
})
