import sys, pygame, random
from pygame.locals import *


pygame.init()
screen_info = pygame.display.Info()

#1. Set up our screen - what we're going to be drawing on
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)

#2. Set up a clock to control the refresh rate of our game
clock = pygame.time.Clock()

color = (93, 23, 182)

sprite_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()

def main():
  game_over = False
  global screen
    #main game loop - this constantly updates our game
  while True:
        #controls refresh rate of our game
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
              if event.key == K_f:
                pygame.display.set_mode(size, FULLSCREEN)
              if event.key == K_ESCAPE:
                pygame.display.set_mode(size)
        
        #to actually make this show up
        screen.fill(color)
        platforms.draw(screen)
        sprite_list.draw(screen)
        pygame.display.flip()
       

if __name__ == '__main__':
    main()