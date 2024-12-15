import pygame
import os 

pygame.init() # initializes pygame

width = 800  # sets width of game window
height = 600  # sets height of game window
FPS = 60 # sets frames per second
white = (255, 255, 255) #creates white color option
black = (0, 0, 0) # creates black color option

# window stuff
window = pygame.display.set_mode((width, height)) # creates game window
pygame.display.set_caption("game boi") # sets title of game window

# font stuff
font = pygame.font.SysFont('Arial', 30) # sets font
game_over_font = pygame.font.SysFont('Arial', 60) # sets font for end screen
button_font = pygame.font.SysFont('Arial', 40) # button fonts

# timer variables
counter = 10
score = 0
pygame.time.set_timer(pygame.USEREVENT, 1000) # sets timer

# apple settings
apple_size = 60  # sets apple size
apple_pos = [400, 300] # sets apple position
apple_speed = [5, 5] # sets apple speed

APPLE_IMAGE = pygame.image.load(os.path.join('assets', 'apple.png')) # loads apple image
APPLE = pygame.transform.scale(APPLE_IMAGE, (apple_size, apple_size)) # sets size of apple image

# button stuff
button_width = 200 #button width
button_height = 50 # button height
play_again_button_rect = pygame.Rect(300, 350, button_width, button_height) # play again button size
quit_button_rect = pygame.Rect(300, 420, button_width, button_height) # quit button size


# game over screen
def game_over_screen(score): 
    window.fill(black) #resets background to black without apple or timer
    game_over_text = game_over_font.render("GAME OVER", True, white)
    score_text = font.render(f"Score: {score}", True, white)
    window.blit(game_over_text, (225, 200)) # displays game over text and sizes it
    window.blit(score_text, (350, 300)) #displays score text and sizes it

    # play again button
    pygame.draw.rect(window, (0, 255, 0), play_again_button_rect) # replay button
    play_again_text = button_font.render("Play Again", True, black) 
    window.blit(play_again_text, (play_again_button_rect.x + 7, play_again_button_rect.y + 3)) # text spacing in play again button

    # quit button
    pygame.draw.rect(window, (255, 0, 0), quit_button_rect)
    quit_text = button_font.render("Quit", True, black)
    window.blit(quit_text, (quit_button_rect.x + 60, quit_button_rect.y + 3)) # text spacing in quit button

    pygame.display.flip() 

# main loop
def main():
    global apple_pos, apple_speed, counter, score 
    run = True
    game_over = False
    clock = pygame.time.Clock() #game speed
    
    while run: # game loop
        for event in pygame.event.get(): # loops through events
            if event.type == pygame.QUIT: # checks if player quits game
                run = False # ends game

            if event.type == pygame.USEREVENT and not game_over: #check the time left on the counter
                counter -= 1
                if counter <= 0: #if no time left game over is true 
                    game_over = True
            
            if game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if play_again_button_rect.collidepoint(mouse_pos):
                        counter = 10 #reset counter
                        apple_pos = [400, 300] #reset positon of apple
                        apple_speed = [5, 5] #reset apple speed
                        game_over = False
                        score = 0
                    if quit_button_rect.collidepoint(mouse_pos):
                        run = False

            # press esc key to quit
            if event.type == pygame.KEYDOWN: # checks if key is pressed
                if event.key == pygame.K_ESCAPE: # checks if escape key is pressed
                    pygame.quit() # ends game
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_pos = event.pos #checks if apple has been clicked
                if (apple_pos[0] <= mouse_pos[0] <= apple_pos[0]+ apple_size and apple_pos[1] <= mouse_pos[1] <= apple_pos[1]+apple_size): #checks if the mouse click is in the space the apple occupies 
                    score += 1 #adds a point to the score
        
        if not game_over:
            window.fill(black) # window color to clear screen
            time_text = f"Time: {str(counter).rjust(3)}" 
            score_text = f"Score: {str(score).rjust(3)}" 
            window.blit(font.render(time_text, True, white), (32, 47)) # sets time text
            window.blit(font.render(score_text, True, white), (32, 20)) # sets score text
            window.blit(APPLE, apple_pos) # draws apple image

       
        if counter > 0:
            apple_pos[0] += apple_speed[0] # moves apple
            apple_pos[1] += apple_speed[1] # moves apple
            if apple_pos[0] < 0 or apple_pos[0] + apple_size > width: # checks if apple hits side wall
                apple_speed[0] = -apple_speed[0] # reverses apple speed side to side
            if apple_pos[1] < 0 or apple_pos[1] + apple_size > height: # checks if apple hits top or bottom wall
                apple_speed[1] = -apple_speed[1] # reverses apple speed up and down
        else:
            apple_speed = [0, 0] #the apple stops

        if game_over:
            game_over_screen(score)

        pygame.display.flip() # update game window
        clock.tick(FPS) # screen refresh rate
            
    pygame.quit() # ends game

if __name__ == "__main__":
    main()
