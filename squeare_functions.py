import turtle

def main():
    window = turtle.Screen()
    doni = turtle.Turtle()

    make_square(doni)

    turtle.mainloop()

def make_square(doni):
    len = int(raw_input('Tamaño del cuadrado: '))

    for i in range(4):
        make_line_and_turn(doni, len)

def make_line_and_turn(doni, len):
    doni.forward(len)
    doni.left(90)
