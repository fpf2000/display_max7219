import max7219.led as led

matrix = led.matrix()

matrix.brightness(5)

matrix.orientation(0)

matrix.show_message("Bsp. Name")

matrix.show_message("Bsp frage?")


matrix.letter(2, ord("1"))

matrix.clear()

matrix.clear()
