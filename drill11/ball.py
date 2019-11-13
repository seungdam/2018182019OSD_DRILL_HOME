import random
from pico2d import *
import game_world
import game_framework


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600 - 1), 60, 0
        self.collide_Brick = False

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    # fill here for def stop
    def stop(self):
        self.fall_speed = 0


# fill here
class BigBall(Ball):
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200  # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600 - 1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)
        self.collide_Brick = False

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def late(self, a):
        if self.y < a.y - 20 and (self.x < a.x or self.x > a.x):
            self.y = a.y + 50

        if a.dir is 1:
            self.x += a.speed * game_framework.frame_time
        elif a.dir is -1:
            self.x -= a.speed * game_framework.frame_time


class Brick:
    image = None

    def __init__(self):
        if Brick.image is None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y = random.randint(0, 1600 - 1), 200
        self.dir = 1
        self.speed = 100

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.dir is 1:
            if self.x >= 1600 - 90:
                self.dir = -1
            self.x += self.speed * game_framework.frame_time

        elif self.dir is -1:
            if self.x <= 0 + 90:
                self.dir = 1
            self.x -= self.speed * game_framework.frame_time
