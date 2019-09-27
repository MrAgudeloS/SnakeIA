#!/usr/bin/env python
# coding: utf-8

# from __future__ import print_function
from libreria import createProblem
import math
import pygame as pg
import random as r

method = "dfs"

def moveSnake(direction, snake):
    snakeX = snake[0].rect.x
    snakeY = snake[0].rect.y
    if direction == 1:
        snakeX+=16
    if direction == 2:
        snakeY+=16
    if direction == 3:
        snakeX-=16
    if direction == 4:
        snakeY-=16
    
    tail = snake.pop()
    tail.rect.x = snakeX
    tail.rect.y = snakeY
    snake = [tail] + snake
    return snake


def insertHead(direction, snakeList):
    snakeX = snakeList[0].rect.x
    snakeY = snakeList[0].rect.y
    if direction == 1:
        snakeX+=16
    if direction == 2:
        snakeY+=16
    if direction == 3:
        snakeX-=16
    if direction == 4:
        snakeY-=16

    s =  snake()
    s.rect.x = snakeX
    s.rect.y = snakeY
    Snake.add(s)
    snakeList = [s] + snakeList
    return snakeList

def checkCollision(snakeList):
    cabezaX = snakeList[0].rect.x
    cabezaY = snakeList[0].rect.y
    for i in snakeList[1:]:
        if cabezaX == i.rect.x and cabezaY == i.rect.y:
            print("nonas")
            return True



def generateSnake():
    length = 3
    for i in range(length,-1,-1):
        snakeList.append({"x":i*16, "y": 32})
    return snakeList

VIWEPORT_SIZE = (320, 320)

snakeList = []



class snake(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([16,16])
        self.image.fill((10,20,30))
        self.rect = self.image.get_rect()
        # self.snakeList = []
        self.rect.x = 0
        self.rect.y = 0
        self.direction = 1


class Food(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([16,16])
        self.image.fill([255,0,255])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
    def generateFood(self):
        print("me genere")
        self.rect.x = r.randrange(32,288,16)
        self.rect.y = r.randrange(32,288,16)

        return [self.rect.x, self.rect.y]


if __name__ == "__main__":

    listaSnake = []
    generateSnake()
    food = Food()
    listFood = food.generateFood()
    pg.init()
    pantalla = pg.display.set_mode(VIWEPORT_SIZE)
    Snake = pg.sprite.Group()
    for i in snakeList:
        s =  snake()
        s.rect.x = i["x"]
        s.rect.y = i["y"]
        Snake.add(s)
        listaSnake.append(s)
    
    # print((listaSnake[0].rect.x,listaSnake[0].rect.y))
    
    Food = pg.sprite.Group()
    food.rect.x = listFood[0]
    food.rect.y = listFood[1]
    Food.add(food)
    reloj = pg.time.Clock()
    fin = False
    direction = 1

    lm = createProblem(listaSnake, food, method, direction)
    
    while not fin:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fin = True

        if lm != []:

            mov = lm.pop()
            
            if mov == 'up':
                direction = 4
            if mov == 'down':
                direction = 2
            if mov == 'right':
                direction = 1
            if mov == 'left':
                direction = 3
                        
        hit = pg.sprite.spritecollide(listaSnake[0], Food, True)

        if hit:
            listaFood = food.generateFood()
            food.rect.x = listaFood[0]
            food.rect.y = listaFood[1]
            Food.add(food)
            listaSnake = moveSnake(direction, listaSnake)

            listaSnake = insertHead(direction, listaSnake)
            print("hittie")
            lm = createProblem(listaSnake, food, method, direction)
            while lm == False:
                listaSnake = moveSnake(direction, listaSnake)
                if direction == 4:
                    listaSnake = moveSnake(direction - 1, listaSnake)
                    listaSnake = moveSnake(direction - 1, listaSnake)

                listaSnake = moveSnake(direction + 1, listaSnake)
                pantalla.fill((255,255,255))
                Snake.draw(pantalla)
                Food.draw(pantalla)
                lm = createProblem(listaSnake, food, method, direction)

        else:
            listaSnake = moveSnake(direction, listaSnake)
        
        # collision = checkCollision(listaSnake)
        # if collision or listaSnake[0].rect.x < 0 or listaSnake[0].rect.x > 640 or listaSnake[0].rect.y < 0 or listaSnake[0].rect.y > 400:
        #     fin = True

        pantalla.fill((255,255,255))
        Snake.draw(pantalla)
        Food.draw(pantalla)
        pg.display.flip()
        reloj.tick(25)

        





# if __name__ == "__main__":
#         main()