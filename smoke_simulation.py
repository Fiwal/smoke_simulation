import random
from smoke import Smoke


class SmokeSimulation:

    def __init__(self, pygame_program, start_x, end_x, y):

        self.program = pygame_program
        self.window = self.program

        self.smoke_x = 1

        self.start_x = start_x
        self.end_x = end_x

        self.y = y

        self.smoke = []
        self.add_smoke()

    def add_smoke(self):

        self.smoke_x = self.start_x

        while True:

            random_size = random.randint(80, 130)
            random_y_speed = random.uniform(5, 35)
            random_rotation = random.randint(-180, 180)
            random_alpha = random.randint(30, 40)

            self.smoke.append(Smoke(random_size, random_size, self.smoke_x, self.y, 0, random_y_speed,
                                    self.program, random_rotation, random_alpha, self))

            self.smoke_x += random.randint(50, 80)

            if self.smoke_x > self.end_x:
                break

    def update_and_draw(self):

        self.add_smoke()

        self.program.window.fill((0, 0, 0))

        for i in self.smoke:
            i.update()
            i.draw()