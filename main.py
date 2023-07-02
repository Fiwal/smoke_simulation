import pygame
from smoke_simulation import SmokeSimulation

pygame.init()


class Program:

    def __init__(self, width, height):

        self.height = height
        self.width = width

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("smoke_simulation")

        self.run = True

        self.clock = pygame.time.Clock()
        self.FPS = 150

        self.smoke_simulation = SmokeSimulation(self, -50, self.width, self.height - 10)

    def check_if_close_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                break

    def main(self):

        while self.run:

            self.check_if_close_game()

            self.smoke_simulation.update_and_draw()

            self.clock.tick(self.FPS)
            pygame.display.flip()


program = Program(600, 400)
program.main()
