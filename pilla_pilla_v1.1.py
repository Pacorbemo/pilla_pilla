from re import M
from keyboard import *
import turtle

pepe = turtle.Turtle()
enemy= turtle.Turtle()

pepe.penup()
pepe.goto(100,100)

enemy.penup() 
enemy.speed(0)
enemy.color('red')

def muerte():
    if abs(pepe.pos()[1]) - abs(enemy.pos()[1]) <10 and abs(pepe.pos()[0]) - abs(enemy.pos()[0]) < 10:
        global vida
        vida = False   
pepe.speed(0)
pos='rgt'
e_pos = 'rgt'

def mov_up(position,entity,velocity):
    if position == 'rgt':
            entity.left(90)
    elif position == 'left':
            entity.right(90)
    elif position == 'down':
            entity.right(180)
    entity.forward(velocity)
    position='up'
    return(position)

direction = [('up',90),('right', 0), ('left',180), ('down',270), ('up_r', 45), ('up_l', 135), ('down_l', 225), ('down_r', 310)]
def mov(dir,position,entity,speed):
    if position != dir:
        position = dir
    for i in range(0,8):
        if direction[i][0] == position:
            entity.setheading(direction[i][1])
    entity.forward(speed)
    return(position)

vida = True
while vida:
    if is_pressed('up'):
        if is_pressed('left') and is_pressed('right'):
            mov('up',pos,pepe,4)
        elif is_pressed('left'):
            mov('up_l',pos,pepe,4)
        elif is_pressed('right'):
            mov('up_r',pos,pepe,4)
        else:
            mov('up',pos,pepe,4)
    elif is_pressed('down'):
        if is_pressed('left') and is_pressed('right'):
            mov('down',pos,pepe,2)
        elif is_pressed('left'):
            mov('down_l',pos,pepe,2)
        elif is_pressed('right'):
            mov('down_r',pos,pepe,2)
        else:
            mov('down',pos,pepe,2)
    elif is_pressed('left'):
        mov('left',pos,pepe,2)
    elif is_pressed('right'):
        mov('right',pos,pepe,2)
    elif is_pressed('esc'):
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