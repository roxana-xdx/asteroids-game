import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for object in updatable:
            object.update(dt)
            
        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return 0
            
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
        
        pygame.display.flip()
        
        #limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        

if __name__ == "__main__":
    main()
