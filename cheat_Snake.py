import pygame
import random

pygame.init()

white=(255, 255, 255)
red=(255, 0, 0)
black=(0, 0, 0)

screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake Game")
pygame.display.update()
clock =pygame.time.Clock()
font=pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text=font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])



def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

def gameloop():
    exit_game= False
    game_over= False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    snk_list = []
    snk_length = 1
    with open ("high_Score.txt", "r") as f:
        high_Score =f.read()

    food_x= random.randint(20,screen_width/2)
    food_y= random.randint(20,screen_height/2)
    score=0
    snake_size=15
    fps=30
    while not exit_game:
        if game_over:
            with open("high_Score.txt", "w") as f:
                f.write(str(high_Score))
            gameWindow.fill(white)
            text_screen("Game Over ! Press Enter to Continue ", red, 100, 250)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                   if event.key==pygame.K_RETURN:
                    gameloop()       
        else:    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x=-5
                        velocity_y=0

                    if event.key==pygame.K_UP:
                        velocity_y=-5
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y=5
                        velocity_x=0

                    if event.key==pygame.K_q:
                        score +=5    
        
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score+= 10
                    
                food_x= random.randint(20,screen_width/2)
                food_y= random.randint(20,screen_height/2)
                snk_length+=5
                if score>int(high_Score):
                    high_Score=score

            gameWindow.fill(white)
            text_screen("Score : " + str(score) + "  High Score : " + str(high_Score), red, 5, 5)
            pygame.draw.rect(gameWindow, red , [food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                 

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()