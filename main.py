import random
import pygame

from smoke import Smoke

pygame.init()


class SmokeSimulation:

    def __init__(self, width, height):

        self.height = height
        self.width = width

        self.smoke_x = 1

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("smoke_simulation")

        self.smoke = []
        self.add_smoke()

        self.run = True

        self.clock = pygame.time.Clock()
        self.FPS = 120

    def add_smoke(self):

        self.smoke_x = -50

        while True:

            random_size = random.randint(80, 130)
            random_y_speed = random.uniform(5, 30)
            random_rotation = random.randint(-180, 180)
            random_alpha = random.randint(30, 40)

            self.smoke.append(Smoke(random_size, random_size, self.smoke_x, self.height - 10, 0, random_y_speed, self,
                                    random_rotation, random_alpha))

            self.smoke_x += random.randint(50, 80)

            if self.smoke_x > self.width:
                break

    def main(self):

        while self.run:

            self.add_smoke()
            self.check_if_close_game()
            self.draw_and_update()

            self.clock.tick(self.FPS)
            pygame.display.flip()

    def check_if_close_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                break

    def draw_and_update(self):

        self.window.fill((0, 0, 0))

        for i in self.smoke:
            i.update()
            i.draw()


if __name__ == '__main__':

    simulation = SmokeSimulation(600, 400)
    simulation.main()
