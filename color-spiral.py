import turtle
colors = ['red','purple','blue','green','orange','yellow']
spiral = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    spiral.pencolor(colors[x%6])
    spiral.width(x/100+1)
    spiral.forward(x)
    spiral.left(59)
turtle.mainloop()
