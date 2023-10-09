import sys 
import pygame
from pygame.locals import * 
  
# Global Variables for the game
window_width = 400
window_height = 711
  
# set height and width of window
window = pygame.display.set_mode((window_width, window_height))   
elevation = window_height * 0.8
game_images = {}      
framepersecond = 32
background_image = 'img/background.jpg'
polednice_image = 'img/kata2.png'

def polednice():
    ground = 50
    vertical = 0
    polednice_velocity_y = -9
    polednice_Max_Vel_Y = 10
    poledniceAcceleration = 2.5
    polednice_flap_velocity = -8

    polednice_flapped = False

    while True:
        # Handling the key pressing events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if vertical > 0:
                    polednice_velocity_y = polednice_flap_velocity
                    polednice_flapped = True
            if event.type == KEYDOWN and event.key == K_1:
                game_images['polednice'] = pygame.image.load(f"img/kata2.png").convert_alpha()
            if event.type == KEYDOWN and event.key == K_2:
                game_images['polednice'] = pygame.image.load(f"img/kata1.png").convert_alpha()
            if event.type == KEYDOWN and event.key == K_3:
                game_images['polednice'] = pygame.image.load(f"img/iveta1.png").convert_alpha()
            if event.type == KEYDOWN and event.key == K_4:
                game_images['polednice'] = pygame.image.load(f"img/jana1.png").convert_alpha()
            if event.type == KEYDOWN and event.key == K_5:
                game_images['polednice'] = pygame.image.load(f"img/blanka2.png").convert_alpha()
            if event.type == KEYDOWN and event.key == K_6:
                game_images['polednice'] = pygame.image.load(f"img/matej1.png").convert_alpha()
            if event.type == KEYDOWN and event.key == K_7:
                game_images['polednice'] = pygame.image.load(f"img/lenka1.png").convert_alpha()
            if event.type == KEYDOWN and event.key == K_8:
                game_images['polednice'] = pygame.image.load(f"img/irena1.png").convert_alpha()
            if event.type == KEYDOWN and event.key == K_9:
                game_images['polednice'] = pygame.image.load(f"img/blanka1.png").convert_alpha()
            if event.type == KEYDOWN and event.key == K_0:
                game_images['polednice'] = pygame.image.load(f"img/libu1.png").convert_alpha()
        
        if polednice_velocity_y < polednice_Max_Vel_Y and not polednice_flapped:
            polednice_velocity_y += poledniceAcceleration

        if polednice_flapped:
            polednice_flapped = False
        
        vertical = vertical + min(polednice_velocity_y, elevation - vertical)

        if vertical > ground:
            vertical = ground
        
        # Lets blit our game images now
        window.blit(game_images['background'], (0, 0))
        window.blit(game_images['polednice'], (horizontal, vertical))

        pygame.display.update()
        framepersecond_clock.tick(framepersecond)


if __name__ == "__main__":          
      
    # For initializing modules of pygame library
    pygame.init()  
    framepersecond_clock = pygame.time.Clock()
      
    # Sets the title on top of game window
    pygame.display.set_caption('POLE-dnice')      
  
    # Load all the images which we will use in the game
    # images for displaying score

    game_images['background'] = pygame.image.load(background_image).convert_alpha()                  
    game_images['polednice'] = pygame.image.load(polednice_image).convert_alpha()
    print("WELCOME TO POLE-DNICE")
    print("Press space or enter to start the game")


    while True:
        horizontal = 17
        vertical = 0

        while True:
            for event in pygame.event.get():
    
                # if user clicks on cross button, close the game
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    
                    # Exit the program
                    sys.exit()   

                # If the user presses space or up key,
                # start the game for them
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    polednice()
                else:
                    window.blit(game_images['background'], (0, 0))
                    window.blit(game_images['polednice'], (horizontal, vertical))
                    
                    # Just Refresh the screen
                    pygame.display.update()        
                    
                    # set the rate of frame per second
                    framepersecond_clock.tick(framepersecond)
