import max7219.led as led

matrix = led.matrix()

matrix.brightness(5)

matrix.orientation(0)

matrix.show_message("Test text 001")

matrix.letter(0, ord("1"))

matrix.clear()

matrix.clear()
