import pygame
from logger import log_state
from constants import *
from player import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)



    player = Player(x, y)

    


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateable.update(dt)
        
        for d in drawable:
            d.draw(screen)

        player.draw(screen)
        

        pygame.display.flip()
        clock.tick(60)

        dt = clock.tick(60)
        


if __name__ == "__main__":
    main()
