let asteroid_3 = 0
let asteroid_2 = 0
let level = 0
let my_position = 2
let asteroid_1 = randint(0, 4)
let count = 0
let score = 0
let score_manager = 0
basic.forever(function () {
    music.play(music.stringPlayable("- - - - - - - - ", 120), music.PlaybackMode.InBackground)
    my_position = Math.constrain(Math.round((input.acceleration(Dimension.X) + 500) / 250), 0, 4)
    basic.clearScreen()
    led.plot(my_position, 4)
    led.plotBrightness(asteroid_1, count % 5, 32)
    count = (count + 1) % 5
    basic.pause(250)
    if (count == 4) {
        if (my_position == asteroid_1) {
            basic.showLeds(`
                . # . . .
                . # . . .
                . # . . .
                . # . . .
                . # # # .
                `)
            my_position = 2
            score = 0
            score_manager = 0
            basic.pause(5000)
            basic.showString("" + (score_manager))
        } else {
            score += 1
            if (score == 10) {
                basic.showLeds(`
                    # . . . #
                    # . . . #
                    # . # . #
                    # . # . #
                    # # # # #
                    `)
                score = 0
                level = 1
                score_manager += 1
                basic.pause(5000)
                basic.showString("" + (score_manager))
            }
        }
    }
    if (count == 0) {
        asteroid_1 = randint(0, 4)
    }
})
