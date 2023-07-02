import pygame


class Smoke:

    def __init__(self, height, width, x, y, x_speed, y_speed, program, rotation, alpha):

        self.program = program

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel_x = x_speed
        self.vel_y = y_speed
        self.alpha = alpha

        self.rotation = rotation

        self.img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('smoke.png'),
                                                                  (self.width, self.height)), self.rotation)
        self.img.set_alpha(self.alpha)

    def draw(self):

        self.program.window.blit(self.img, (self.x, self.y))
        self.alpha -= 1
        self.img.set_alpha(self.alpha)

    def update(self):

        self.vel_y *= 0.93
        self.vel_x *= 0.95

        self.y -= self.vel_y
        self.x += self.vel_x

        if self.vel_y < 0.1:

            self.program.smoke.pop(self.program.smoke.index(self))
