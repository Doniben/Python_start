import turtle

window = turtle.Screen() #Crear el espacio para graficar
cuadrado = turtle.Turtle() #aplicar la librer'ia turtle a la variable cuadrado

for i in range(1,50):  #iteracion para ir aumentando el tamano de la variable en forma de espiral cuadrada
    cuadrado.forward(i)
    cuadrado.right(90)

turtle.mainloop() #evitar que se cierre la ventana
