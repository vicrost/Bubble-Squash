
import pygame
import random
import time
import threading
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



class Player(pygame.sprite.Sprite):
    # This class will represent the player whom will be playing as a hand

    def __init__(self):
        # Constructor

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Creates an image for the player

        # image width = 60 image height = 31
        self.image = pygame.image.load('hand.png').convert()

        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()


        # make the default location the passed in values
        self.rect.x = 700 /2
        self.rect.y = 400 /2


    def update(self) -> object:
        """ Find a new position for the player"""

        pos = pygame.mouse.get_pos()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Bubbles(pygame.sprite.Sprite):
    # This class represents the bubbles in the game

    def __init__(self ,x ,y):
        # constructor

        # Call the parent class (Sprite) constructor
        super().__init__()

        # load an image of the bubble

        # image width = 70  height  = 63
        
        self.image = pygame.image.load('Bubble.png').convert()
        
        # Set background color to be transparent
        self.image.set_colorkey(WHITE)

        # start a timer for the bubble
        threading.Timer(1 ,self.remove).start()
        


        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        
    def check_click(self ,mouse):
        if self.rect.collidepoint(mouse):
            return True

    def remove(self):
        self.kill()

    
        
            

    

def main():

    # initialize pygame
    pygame.init()
 
    # Set the width and height of the screen [width, height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Bubble Squash")

    # interval between each bubble(milliseconds)
    interval = 600
    # bubble lifespan(milliseconds)
    life = 500
    # number of bubbles spawned
    bubble_num = 0

    # This is a list of bubble sprites. All Bubbles generated will be added to this list
    bubble_list = pygame.sprite.Group()
    # This is a list of every sprite
    all_sprites_list = pygame.sprite.Group()

    # creates the player
    player = Player()
    all_sprites_list.add(player)

    # loads the background
    background_image = pygame.image.load('ocean_background.png').convert()
    # set positions of background
    background_position = [0 ,0]

 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('', 25, True, False)

    # starts timer for bubbles
    now = pygame.time.get_ticks()

    # stores the score of the player
    current_score = 0

    # starts game timer
    start_time = 30
    frame_count = 0
    frame_rate = 60

    # stops the game if True
    game_over = False
    
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over == False:
                # check if any bubble has been hit
                for bubble in bubble_list:
                    if bubble.check_click(event.pos )==True:
                        # add 1 to the score
                        current_score += 1
                        # remove the bubble
                        bubble_list.remove(bubble)
                        all_sprites_list.remove(bubble)

        # number of seconds since variable 'now' was initiated
        time_diff = pygame.time.get_ticks() - now

        # if 0.5 seconds have passed and the timer hasn't reached zero
        # create another bubble
        if time_diff >= interval and game_over == False:
            bubble = Bubbles(random.randrange(600) ,random.randrange(400))
            bubble_list.add(bubble)
            all_sprites_list.add(bubble)
            bubble_num += 1

            # reset the timer
            now = pygame.time.get_ticks()

        # updates all the sprites
        all_sprites_list.update()
    
        screen.fill(WHITE)

        # draws the background
        screen.blit(background_image ,background_position)
    
        # Draw all the spites
        all_sprites_list.draw(screen)

        score = font.render("Score: " +str(current_score), True, BLACK)

        # draws the score on the screen
        screen.blit(score, [10, 10])

        # calculate total seconds
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0
            game_over = True  # timer has reached 0
        # number of minutes
        minutes = total_seconds // 60
        # number of seconds
        seconds = total_seconds % 60
        # calculates time left
        output_string = "Time Left : {0:02}:{1:02}".format(minutes, seconds)
        # renders the timer
        text = font.render(output_string, True, BLACK)
        # blits the timer unto the screen
        screen.blit(text, [320, 10])
        # countsdown
        frame_count += 1

        # shows game over page if timer hits zero
        if game_over:
            screen.fill(BLACK)
            over_text = font.render("GAME OVER", True, WHITE)
            over_text_rect = over_text.get_rect()
            text_x = screen.get_width() / 2 - over_text_rect.width / 2
            text_y = screen.get_height() / 2 - over_text_rect.height / 2
            screen.blit(over_text, [text_x, text_y])

        # update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(frame_rate)

    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    main()
