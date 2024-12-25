import pygame
import sys
import random
import math
#importing all necessary liberaries
pygame.init()

width = 600
height = 400
#dimensions of the window

screen = pygame.display.set_mode((width,height)) #creating main screen
pygame.display.set_caption("flappy bird")

clock = pygame.time.Clock()

score = 0
gravity  = 1
jump = -1
speed = 1

birdy_size = 20
birdy_speed = 1
birdy_position = pygame.Rect(100,200,birdy_size,birdy_size)
towers = []

def add_tower():
    tower_width = 10
    gap = 100
    random_gap = random.randint(gap,height-gap)
    top_tower = pygame.Rect(width,0,tower_width,random_gap)
    bottom_tower = pygame.Rect(width,random_gap+gap,tower_width,height-random_gap-gap)
    towers.append(top_tower)
    towers.append(bottom_tower)

def move_tower():
    for tower in towers:
        tower.x -= 2

def draw_tower():
    for tower in towers:
        pygame.draw.rect(screen,white,tower)

def generate_new():
    if towers[0].right<0:
        towers.pop(0)
        towers.pop(0)
def tower_count():
    if len(towers)<2:
        add_tower()
def collisions():
    if birdy_position.collidelist(towers)!= -1:
        return True
    if birdy_position.top <=0 or birdy_position.bottom >= height:
        return True
    return False

def display_message(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    
    screen.blit(text, text_rect)
    pygame.display.flip()

    pygame.time.delay(2000)  # Display the message for 2000 milliseconds (2 seconds)



add_tower()
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            birdy_position.y -=20
        


    
    birdy_position.y += birdy_speed
    move_tower()
    generate_new()
    tower_count()
    

    if birdy_position.bottom>height:
        birdy_position.bottom = height
        birdy_speed = 0
    elif birdy_position.top<0:
        birdy_position.top = 0
    
    if collisions():
        message = "Game Over, Score : "
        message = message + str(score//280)
        display_message(message) 
        pygame.quit()
        sys.exit()
    else:
        score += 1


    screen.fill(black)
    pygame.draw.rect(screen,red,birdy_position)
    draw_tower()
    
    pygame.display.flip()
    clock.tick(60)

