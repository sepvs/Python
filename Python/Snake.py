import turtle
import time
import random

#pantalla del juego

canvas = turtle.Screen()
canvas.setup(width=600, height=600)
color_fondo=canvas.bgcolor("black")
canvas.tracer()
    
#cabeza de la serpiente

cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.fillcolor("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Se genera la manzana

manzana=turtle.Turtle()
manzana.speed(1000)
manzana.shape("square")
manzana.fillcolor("red")
randx=random.randrange(-270, 270, 10)
randy=random.randrange(-270, 270, 10)
manzana.goto(randx,randy)


#DEFINICIÓN DE FUNCIONES

#Limites en los que la serpiente puede circular
def limites():
    if cabeza.xcor() >= 250:
        exit()
    elif cabeza.xcor() <= -250:
        exit()
    elif cabeza.ycor() >= 250:
        exit()
    elif cabeza.ycor() <= -250:
        exit()
   
#creación de bordes 
def bordes():
    lapiz=turtle.Turtle()
    lapiz.speed(6)
    lapiz.goto(-270, -270)
    if lapiz.xcor() != -270:
        lapiz.pencolor("black")
    if lapiz.xcor() == -270:
        lapiz.pencolor("green")
    for i in range (4): 
        lapiz.forward(540)
        lapiz.pos()
        lapiz.left(90)

#funciones de dirección
def derecha():
    cabeza.direction="right"
def izquierda():
    cabeza.direction="left"
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"

def movimiento():
    if cabeza.direction == "up":
        y=cabeza.ycor()
        cabeza.sety(y+10)
    if cabeza.direction == "down":
        y=cabeza.ycor()
        cabeza.sety(y-10)
    if cabeza.direction == "right":
        x=cabeza.xcor()
        cabeza.setx(x+10)
    if cabeza.direction == "left":
        x=cabeza.xcor()
        cabeza.setx(x-10)

#definicion de la creación del cuerpo de la serpiente
"""def generar_cuerpo():
    cuerpo=turtle.Turtle()
    cuerpo.shape("square")
    cuerpo.fillcolor("green")
    cuerpo.penup()
    coordenadax=cabeza.xcor+10
    coordenaday=cabeza.ycor
    cuerpo.setx(coordenadax+10)
    cuerpo.sety(coordenaday)
    cuerpo.direction = "stop"
    if cabeza.direction == "up":
        y=cuerpo.ycor()
        cuerpo.sety(y+10)
    if cabeza.direction == "down":
        y=cuerpo.ycor()
        cuerpo.sety(y-10)
    if cabeza.direction == "right":
        x=cuerpo.xcor()
        cuerpo.setx(x+10)
    if cabeza.direction == "left":
        x=cuerpo.xcor()
        cuerpo.setx(x-10)"""




canvas.listen()
canvas.onkeypress(arriba, "Up")
canvas.onkeypress(abajo, "Down")
canvas.onkeypress(derecha, "Right")
canvas.onkeypress(izquierda, "Left")

bordes()


while True:
    canvas.update()
    # Se definen las coordenadas de la manzana para que se saquen indefinidamente
    randx=random.randrange(-270, 270, 10)
    randy=random.randrange(-270, 270, 10)

    # Planteamiento del movimiento de la manzana
    if cabeza.xcor() == manzana.xcor() and cabeza.ycor() == manzana.ycor():
        manzana.goto(randx, randy)
        """generar_cuerpo()"""
    limites()
    movimiento()
    
    time.sleep(0.1)




turtle.done()
