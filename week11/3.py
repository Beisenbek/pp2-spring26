import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

step = 1
dx = step
dy = 0

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
                dy = -step
                dx = 0
        if pressed[pygame.K_DOWN]:
                dy = step
                dx = 0
        if pressed[pygame.K_LEFT]: 
                dx = -step
                dy = 0
        if pressed[pygame.K_RIGHT]: 
                dx = step
                dy = 0

        x = x + dx
        y = y + dy
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        clock.tick(60)