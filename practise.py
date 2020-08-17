import pygame
import random
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color,pos):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]






def main():
     
    # Initialize Pygame
    pygame.init()
 
    # Set the height and width of the screen
    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])
    

    done = False
    
    block_counter = 0
    block_list = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    clock = pygame.time.Clock()

    s_time = pygame.time.get_ticks()


    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        


        time_diff = pygame.time.get_ticks() - s_time
        if time_diff >= 1000:
            block = Block(BLACK,[random.randrange(600),random.randrange(440)])
            all_sprites.add(block)

            #reset
            s_time = pygame.time.get_ticks()
        all_sprites.update()

        screen.fill(BLUE)
        all_sprites.draw(screen)
        #timer_surface = font.render(str(time_difference/1000), True, pg.Color('yellow'))
        #screen.blit(timer_surface, (20, 20))

        pygame.display.flip()
        clock.tick(30)



if __name__ == "__main__":
    main()
        
        
            
    
