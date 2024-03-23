def on_forever():
    music._play_default_background(music.built_in_playable_melody(Melodies.CHASE),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
basic.forever(on_forever)
# Python code
#
my_position = 0
asteroid_1 = 0
count = 0
score = 0
level = 0
asteroid_2 = 0
asteroid_3 = 0
score_manager = 0
level = 0
my_position = 2
asteroid_1 = randint(0, 4)
count = 0
score = 0
score_manager = 0

def on_forever():
  global my_position
  global count
  global score
  global score_manager
  global level
  global asteroid_1
  my_position = Math.constrain(Math.round(((input.acceleration(Dimension.X) + 500) / 250)), 0, 4)
  basic.clear_screen()
  led.plot(my_position, 4)
  led.plot_brightness(asteroid_1, (count % 5), 32)
  count = ((count + 1) % 5)
  basic.pause(250)
  if count == 4:
    if my_position == asteroid_1:
      basic.show_leds("""
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # # # .
        """)
      my_position = 2
      score = 0
      score_manager = 0
      basic.pause(5000)
      basic.show_string("" + score_manager)
    else:
      score += 1
      if score == 10:
        basic.show_leds("""
          # . . . #
          # . . . #
          # . # . #
          # . # . #
          # # # # #
          """)
        score = 0
        level = 1
        score_manager += 1
        basic.pause(5000)
        basic.show_string("" + score_manager)
  if count == 0:
    asteroid_1 = randint(0, 4)
basic.forever(on_forever)
