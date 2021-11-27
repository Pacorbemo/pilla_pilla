from keyboard import *
import turtle
pepe = turtle.Turtle()
pepe.penup()
pepe.goto(100,100)
enemy= turtle.Turtle()
enemy.penup()
vida = True 
enemy.speed(0)
enemy.color('red')

print(enemy.pos())
print(pepe.pos())
def muerte():
    if abs(pepe.pos()[1]) - abs(enemy.pos()[1]) <10 and abs(pepe.pos()[0]) - abs(enemy.pos()[0]) < 10:
        global vida
        vida = False   
pepe.speed(0)
pos='rgt'
e_pos = 'rgt'

while vida:
    if is_pressed('up'):
        if pos == 'rgt':
            pepe.left(90)
        elif pos == 'left':
            pepe.right(90)
        elif pos == 'down':
            pepe.right(180)
        pos = 'up'
        pepe.forward(2)
    if is_pressed('down'):
        if pos == 'rgt':
            pepe.right(90)
        elif pos == 'left':
            pepe.left(90)
        elif pos == 'up':
            pepe.right(180)
        pos = 'down'
        pepe.forward(2)
    if is_pressed('left'):
        if pos == 'rgt':
            pepe.right(180)
        elif pos == 'down':
            pepe.right(90)
        elif pos == 'up':
            pepe.left(90)
        pos = 'left'
        pepe.forward(2)
    if is_pressed('right'):
        if pos == 'left':
            pepe.right(180)
        elif pos == 'down':
            pepe.left(90)
        elif pos == 'up':
            pepe.right(90)
        pos = 'rgt'
        pepe.forward(2)
    if is_pressed('esc'):
        break
    
    if pepe.pos()[0] < enemy.pos()[0]:
        if e_pos == 'rgt':
            enemy.right(180)
        elif e_pos == 'down':
            enemy.right(90)
        elif e_pos == 'up':
            enemy.left(90)
        e_pos = 'left'
        enemy.forward(1)

    if pepe.pos()[0] > enemy.pos()[0]:
        if e_pos == 'left':
            enemy.right(180)
        elif e_pos == 'down':
            enemy.left(90)
        elif e_pos == 'up':
            enemy.right(90)
        e_pos = 'rgt'
        enemy.forward(1)
    
    if pepe.pos()[1] < enemy.pos()[1]:
        if e_pos == 'rgt':
            enemy.right(90)
        elif e_pos == 'left':
            enemy.left(90)
        elif e_pos == 'up':
            enemy.right(180)
        e_pos = 'down'
        enemy.forward(1)

    if pepe.pos()[1] > enemy.pos()[1]:
        if e_pos == 'rgt':
            enemy.left(90)
        elif e_pos == 'left':
            enemy.right(90)
        elif e_pos == 'down':
            enemy.right(180)
        e_pos = 'up'
        enemy.forward(1)
    muerte()
print('p')