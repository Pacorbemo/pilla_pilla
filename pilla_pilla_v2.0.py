from keyboard import *
import turtle,time
from random import randint

pepe = turtle.Turtle()
enemy= turtle.Turtle()
coin= turtle.Turtle()
contador = turtle.Turtle()
freeze = turtle.Turtle()

coinsCollected=0
coinX,coinY,freezeX,freezeY = randint(-300,300), randint(-300,300),randint(-300,300),randint(-300,300)
coin.penup(), coin.color('yellow'), coin.speed(0), coin.shape('circle'), coin.hideturtle(), coin.setposition(coinX,coinY)
freeze.penup(), freeze.color(0.2,1,1), freeze.speed(0), freeze.shape('circle'), freeze.hideturtle(), freeze.setposition(freezeX,freezeY)
pepe.penup(), pepe.setposition(100,100), pepe.speed(0)
enemy.penup(), enemy.speed(0), enemy.color('red')
contador.penup(), contador.hideturtle(), contador.setposition(-430, 380), contador.write(f'Coins: {coinsCollected}', font=('times',15,'normal'))
pos='rgt'
e_pos = 'rgt'


direction = [('up',90),('right', 0), ('left',180), ('down',270), ('up_r', 45), ('up_l', 135), ('down_l', 225), ('down_r', 310)]
def mov(dir,position,entity,speed):
    if position != dir:
        position = dir
    for i in range(0,8):
        if direction[i][0] == position:
            entity.setheading(direction[i][1])
    entity.forward(speed)
    return(position)

def muerte():
    if -5<= abs(pepe.pos()[0] - (enemy.pos()[0])) <5 and -5 <= abs(pepe.pos()[1] - (enemy.pos()[1])) <5:
        global vida
        vida = False   

init_time=int(time.time())
current_time = time.time()
e_vel = 2
pepe_vel = 4
vida,move_enemy,increase_speed = True,True,True
move_time,current_time3 = 0,0

while vida:
    if increase_speed:
        current_time2 = time.time() - current_time
        current_time = time.time()
        current_time3 += current_time2 
        if current_time3 >= 5:
            e_vel+=1
            current_time3= 0
            current_time = time.time()
    else:
        current_time = time.time()

    if init_time+3 == int(time.time()):
        coin.showturtle(), freeze.showturtle()
        
    if init_time+3 < int(time.time()) and abs(pepe.pos() - coin.pos()) < 10:
            coin.hideturtle()
            pepe_vel +=1
            coinX,coinY = randint(-300,300), randint(-300,300)
            coin.setposition(coinX,coinY)
            coin.showturtle()

            contador.clear()
            coinsCollected += 1
            contador.write(f'Coins: {coinsCollected}', font=('times',15,'normal')) 

    if init_time+3 < int(time.time()) and abs(pepe.pos() - freeze.pos()) < 10:
            freeze.hideturtle()
            move_enemy=False
            increase_speed=False
            move_time = int(time.time())
            freezeX,freezeY = randint(-300,300), randint(-300,300)
            freeze.setposition(freezeX,freezeY)
            freeze.showturtle()

    if int(time.time()) == move_time + 3:
        move_enemy = True
        increase_speed=True

    if is_pressed('up'):
        if is_pressed('left') and is_pressed('right'):
            mov('up',pos,pepe,pepe_vel)
        elif is_pressed('left'):
            mov('up_l',pos,pepe,pepe_vel)
        elif is_pressed('right'):
            mov('up_r',pos,pepe,pepe_vel)
        else:
            mov('up',pos,pepe,pepe_vel)
    elif is_pressed('down'):
        if is_pressed('left') and is_pressed('right'):
            mov('down',pos,pepe,pepe_vel)
        elif is_pressed('left'):
            mov('down_l',pos,pepe,pepe_vel)
        elif is_pressed('right'):
            mov('down_r',pos,pepe,pepe_vel)
        else:
            mov('down',pos,pepe,pepe_vel)
    elif is_pressed('left'):
        mov('left',pos,pepe,pepe_vel)
    elif is_pressed('right'):
        mov('right',pos,pepe,pepe_vel)
    elif is_pressed('esc'):
        break

    if move_enemy:
        if int(pepe.pos()[0]) < int(enemy.pos()[0]):
            if int(pepe.pos()[1]) > int(enemy.pos()[1]):
                e_pos=mov('up_l',e_pos,enemy,e_vel)
            elif int(pepe.pos()[1]) < int(enemy.pos()[1]):
                e_pos=mov('down_l',e_pos,enemy,e_vel)
            else:
                e_pos=mov('left',e_pos,enemy,e_vel)
        elif int(pepe.pos()[0]) > int(enemy.pos()[0]):
            if int(pepe.pos()[1]) < int(enemy.pos()[1]):
                e_pos=mov('down_r',e_pos,enemy,e_vel)
            elif int(pepe.pos()[1]) > int(enemy.pos()[1]):
                e_pos=mov('up_r',e_pos,enemy,e_vel)
            else:
                e_pos=mov('right',e_pos,enemy,e_vel)    
        elif int(pepe.pos()[1]) < int(enemy.pos()[1]):
            e_pos=mov('down',e_pos,enemy,e_vel)
        elif int(pepe.pos()[1]) > int(enemy.pos()[1]):
            e_pos=mov('up',e_pos,enemy,e_vel)
    muerte()
