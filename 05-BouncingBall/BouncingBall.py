import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.radius = random.randint(5, 50)
        self.x = random.randint(self.radius, self.screen.get_width()-self.radius)
        self.y = random.randint(self.radius, self.screen.get_height()-self.radius)
        self.speed_x = random.randint(1, 10)
        self.speed_y = random.randint(1, 10)
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x
        if self.y - self.radius < 0:
            self.speed_y *= -1
        if self.y + self.radius > self.screen.get_height():
            self.speed_y *= -1
        if self.x - self.radius < 0:
            self.speed_x *= -1
        if self.x + self.radius > self.screen.get_width():
            self.speed_x *= -1
    def draw(self):
        pygame.draw.circle(self.screen, (self.color), (self.x, self.y), self.radius)



def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    balls = [] #More balls
    for k in range(100):
        balls.append(Ball(screen))
    #ball1 = Ball(screen)
    # TODO: Create an instance of the Ball class called ball1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        # TODO: Draw the ball
        #ball1.draw()
        #ball1.move()
        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
