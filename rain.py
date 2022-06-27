import pygame as py
from random import randrange


class Rain:
    def __init__(self, x, y=0):
        self.x = x
        self.y = y
        self.breadth = randrange(3, 7)
        self.length = self.breadth * 10 // 3
        self.vel = self.breadth * 1.5

    def show(self, surface):
        py.draw.rect(surface, (150, 40, 150),
                     py.Rect(self.x - self.breadth, self.y - self.length, self.breadth, self.length))

    def update(self):
        self.y += self.vel
        if self.y > height:
            self.y = 0
            self.x = randrange(width)


py.init()

width, height = 600, 400
window = py.display.set_mode((width, height))

acceleration = 0.1
water_drops = [Rain(randrange(width))]

running = True
clock = py.time.Clock()
frame_rate = 60
frames = 0

while running:
    window.fill((255, 255, 255))
    clock.tick(frame_rate)
    frames = (frames + 1) % 19

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    if len(water_drops) < 100 and frames == 0:
        water_drops.append(Rain(randrange(width)))

    for rain in water_drops:
        rain.show(window)
        rain.update()

    py.display.update()
