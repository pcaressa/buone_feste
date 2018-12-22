import turtle as T
import random

def triangolo(y, base, altezza):
    T.begin_fill()
    T.up()
    T.color('green')
    T.setposition(0,y)
    T.down()
    T.setposition(base/2,y)
    T.setposition(0,y + altezza)
    T.setposition(-base/2,y)
    T.setposition(0,y)
    T.up()
    T.end_fill()

H = T.window_height()
B = T.window_width()

c = 100

T.speed(5)
T.hideturtle()
T.bgcolor('blue')

# Disegna un po' di stelle a caso
T.color('yellow')
for i in range(20):
    T.up()
    T.setposition(random.randrange(-B//2, B//2),
                  random.randrange(-H//2+c, H//2))
    T.dot()
    T.down()

# Disegna l'albero
y = -H/2 + c
b = 500
a = 200
while y < H/2 - c:
    triangolo(y, b, a)
    y += a/1.5
    b /= 1.3
    a /= 1.3

# Disegna il tronco
T.color("brown")
T.begin_fill()
T.setposition(-c//2, -H//2)
T.down()
T.setposition(c//2, -H//2)
T.setposition(c//2, c-H//2)
T.setposition(-c//2, c-H//2)
T.setposition(-c//2, -H//2)
T.end_fill()

# Disegna la cometa
T.color("yellow")
T.begin_poly()
T.up()
T.setposition(-c, H//2-c/2)
T.down()
for i in range(19):
    T.forward(c//2)
    T.left(170)
T.end_poly()

# coda della cometa
T.begin_poly()
for i in range(15, -15, -5):
    T.up()
    T.setposition(-c//2-c//4, H//2-c/2)
    T.down()
    T.setheading(i)
    T.forward(2*c)
T.end_poly()

# Scritta!
T.color("red")
T.up()
T.setposition(-B//2 + 100, 0)
T.write("Buone Feste!!!", font=('Arial', 50, 'bold'))

T.done()

