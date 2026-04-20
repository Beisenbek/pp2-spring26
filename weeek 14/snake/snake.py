import pygame

from food import Food
from wall import Wall
from worm import Worm

tile_width = 20

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width

done = False

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

worm = Worm(tile_width)
food = Food(tile_width)
wall = Wall(tile_width)

while not done:
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            else:
                filtered_events.append(event)


        worm.process_input(filtered_events)
        worm.move()

        pos = food.can_eat(worm.points[0])
        
        if(pos != None):
            worm.increase(pos)
            food = Food(tile_width)
            if len(worm.points) % 2 == 0:
                wall.next_level()
        
        create_background(screen, 400, 300)

        worm.draw(screen)
        food.draw(screen)
        wall.draw(screen)

        pygame.display.flip()
        clock.tick(5)