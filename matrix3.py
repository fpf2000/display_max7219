import max7219.led as led

matrix = led.matrix(cascaded = 4)

# matrix = led.matrix()

matrix.brightness(0)

matrix.orientation(90)

#deviceiD=1

matrix.show_message("Exploting Kitty")

matrix.clear()

matrix.clear()
