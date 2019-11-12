import game_framework
from pico2d import *

import game_world
                             # 실제 새의 가로길이 143 pixel
PIXEL_PER_METER = (10.0 / 0.4)  # 1 pixel 당  4cm 새의 가로 길이 147 * 4 = 588cm 새의 세로높이 142 * 4 = 568
RUN_SPEED_KMPH = 30.0  # KM / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

image_Position = [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2],
                  [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
                  [0, 0], [1, 0], [2, 0], [3, 0]]

class Bird:
    global image_Position

    def __init__(self):
        self.x, self.y = 1600 // 2, 300
        self.image = load_image('bird_animation.png')
        #self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time

        if self.x >= 1460:
            self.velocity = -RUN_SPEED_PPS
        elif self.x <= 100:
            self.velocity = RUN_SPEED_PPS

        self.dir = clamp(-1, self.velocity, 1)
        pass

    def draw(self):
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        if self.dir is 1:
            self.image.clip_draw(image_Position[int(self.frame)][0] * 183, image_Position[int(self.frame)][1] * 168,
                                 179, 166, self.x, self.y)
        elif self.dir is -1:
            self.image.clip_composite_draw(image_Position[int(self.frame)][0] * 183, image_Position[int(self.frame)][1] * 168,
                                           179, 166, 0.0, 'h', self.x, self.y, 180, 166)

    def handle_event(self, event):
        pass
