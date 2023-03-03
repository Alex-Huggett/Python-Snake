import pygame
from random import randint
from copy import deepcopy as dc
import winsound as ws

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 10  # Set Duration of the sound

global slider_x
global slider2_x
slider_x = 0
slider2_x = 0

letters = {
    'A':[
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1]
    ],
    'L':[
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,0]
    ],
    'P':[
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0]    
    ],
    'Y':[
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]
    ],
    '0':[
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]
    ],
        
    '1':[
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0]
    ],

    '2':[
        [0,1,1,1,0],
        [1,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,1,0],
        [0,0,1,0,0],
        [0,1,0,0,0],
        [1,1,1,1,1]
    ],
    
    '3':[
        [0,1,1,1,0],
        [1,0,0,0,1],
        [0,0,0,0,1],
        [0,1,1,1,0],
        [0,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]
    ],

    '4':[
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,0,1]
    ],

    '5':[
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,0]
    ],

    '6':[
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]
    ],

    '7':[
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,1,0],
        [0,0,0,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]
    ],

    '8':[
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],

    '9':[
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
    ]
}

HighScore = 0

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
grey = pygame.Color(20, 20, 20)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
dark_green = pygame.Color(0, 190, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

PixelWidth = 20 # 5
snake_speed = 20 # 15

def DrawShapeList(shape : list, x, y, ps):
    for layer in range(0, len(shape)):
        for digit in range(0, len(shape[layer])):
            if shape[layer][digit] == 1:
                pygame.draw.rect(game_window, white, pygame.Rect(x+(ps*digit), y+(ps*layer), ps, ps))

def DrawDigit(character : str, x : int, y : int, ps):
    DrawShapeList(letters[character], x, y, ps)

def DrawString(text : str, x=0, y=0, size_multiplier = 1):
    for character in range(0, len(text)):
        ps=6*size_multiplier
        DrawDigit(text[character], x+2+((character*6)-(text[0:character].count('1')*4)-(text[0:character].count('L')))*ps, y+5, ps)

def DrawSquircle(button_dimensions,  x=0, y=0):
    pygame.draw.rect(game_window, grey, pygame.Rect(int(window_x/2)-button_dimensions[0]/2+x, int(window_y/2)-button_dimensions[1]/2-y, button_dimensions[0], button_dimensions[1]), border_radius=20)

def StopCrash():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()

def TestFactor(number:int):
    if window_x % number == 0:
        if window_y % number == 0:
            if number>0:
                return(True)
    return(False)

def GetRounded(number:int):
    repeats = 0
    while True:
        if repeats % 2 == 0:
            number += repeats
        else:
            number -= repeats

        repeats += 1

        if TestFactor(number):
            return(number)
        
        '''
        if the number of repeats is even, add it to the number
        else subtract it
        increment the counter
        [+0, -1, +2, -3, +4, -5, +6, -7, +8, -9, +10, -11]
        [0, -1, 1, -2, 2] etc in both directions
        if the number is a factor of both, return the number

        '''

def Slider(slider_x, ypos=-80, slider_dimensions=[180,40], temp_selected=False):
    DrawSquircle(slider_dimensions, y=ypos)
    pygame.draw.circle(game_window, red, (window_x/2+slider_x, window_y/2-ypos), 8)
    x,y = pygame.mouse.get_pos()

    if not pygame.mouse.get_pressed()[0]:
        temp_selected = False

    if not temp_selected:
        if abs(x-(window_x/2+slider_x))<10 and abs(y-(window_y/2-ypos))<10 and pygame.mouse.get_pressed()[0]:
            temp_selected = True

    if temp_selected:
        # window_x/2+slider_x = mouse.x
        # slider_x = mouse.x-window_x/2
        slider_x = x-window_x/2
        if slider_x>slider_dimensions[0]/2:
            slider_x = slider_dimensions[0]/2
        if slider_x<-slider_dimensions[0]/2:
            slider_x = -slider_dimensions[0]/2
    
    return(slider_x, temp_selected)

def Menu(Score, PixelWidth):
    global slider_x
    global slider2_x

    slider1Selected = False
    slider2Selected = False
    size_multiplier = 1

    slider_dimensions = [180, 20]
    while True:
        game_window.fill(black)
        DrawString(str(Score))
        button_dimensions = [180,80]
        x,y = pygame.mouse.get_pos()

        if window_x/2-button_dimensions[0]/2<x<window_x/2+button_dimensions[0]/2 and window_y/2-button_dimensions[1]/2<y<window_y/2+button_dimensions[1]/2:
            size_multiplier += (1.5-size_multiplier)/100
            if pygame.mouse.get_pressed()[0]:
                amount = round(PixelWidth)
                return(GetRounded(amount), ((slider2_x)+(slider_dimensions[0]/2)+25)/5)
                # we want to round it to the closest common factor of 720 and 480
        else:
            size_multiplier += (1-size_multiplier)/100

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            return(GetRounded(round(PixelWidth)), ((slider2_x)+(slider_dimensions[0]/2)+25)/5)

        if size_multiplier > 1.5:
            size_multiplier = 1.5
        elif size_multiplier < 1:
            size_multiplier = 1

        DrawSquircle([button_dimensions[0]*size_multiplier, button_dimensions[1]*size_multiplier])
        ps = 6*size_multiplier   # pixel size
        DrawString('PLAY', window_x/2-((6*ps*3)+(5*ps*1))/2, window_y/2-ps*3.9, round(size_multiplier, 3))
        #game_window.blit(Trophy, (window_x/2, 50))
        DrawString(str(HighScore), window_x/2-((6*len(str(HighScore)))-(4*str(HighScore).count('1')))/2, 30, 1)
        ####
        slider_dimensions = [180, 20]
        
        slider_x, slider1Selected = Slider(slider_x, -80, slider_dimensions, slider1Selected)
        PixelWidth = 1 + (slider_x + (slider_dimensions[0]/2))/10

        slider2_x, slider2Selected = Slider(slider2_x, -130, slider_dimensions, slider2Selected)

        pygame.draw.rect(game_window, red, pygame.Rect(window_x/2, window_y/2+100, PixelWidth, PixelWidth))

        pygame.display.update()
        StopCrash()

def Play():
    StopCrash()
    Dead = False
    Start = {
        'x' : window_x/2/PixelWidth,
        'y' : window_y/2/PixelWidth
    }
    snake = [
        Start,
        {'x' : Start['x']-1, 'y' : Start['y']},
        {'x' : Start['x']-2, 'y' : Start['y']}
    ]

    Direction = {
        'x' : 1,
        'y' : 0
    }

    Score = 0
    FruitPosition = {'x' : Start['x']+10, 'y' : Start['y']}
    while not Dead:
        change_to = dc(Direction)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = {'x' : 0, 'y' : -1}
                if event.key == pygame.K_DOWN:
                    change_to = {'x' : 0, 'y' : 1}
                if event.key == pygame.K_LEFT:
                    change_to = {'x' : -1, 'y' : 0}
                if event.key == pygame.K_RIGHT:
                    change_to = {'x' : 1, 'y' : 0}

        if not abs(change_to['x'] - Direction['x']) == 2:
            if not abs(change_to['y'] - Direction['y']) == 2:
                Direction = dc(change_to)

        back_segment = dc(snake[-1])

        for segment in range(1, len(snake)):
            snake[-segment] = dc(snake[-segment-1])

        snake[0]['x'] += Direction['x']
        snake[0]['y'] += Direction['y']

        if snake[0] == FruitPosition:
            while FruitPosition in snake:
                FruitPosition = {'x' : randint(1, window_x/PixelWidth-1), 'y' : randint(1, window_y/PixelWidth-1)}
            Score += 1
            ws.Beep(frequency, duration)
            snake.append(back_segment)

        game_window.fill(black)

        DrawString(str(Score))

        for segment in snake:
            pygame.draw.rect(game_window, green, pygame.Rect(segment['x']*PixelWidth, segment['y']*PixelWidth, PixelWidth, PixelWidth))

        pygame.draw.rect(game_window, red, pygame.Rect(FruitPosition['x']*PixelWidth, FruitPosition['y']*PixelWidth, PixelWidth, PixelWidth))
        #pygame.draw.rect(game_window, dark_green, pygame.Rect(FruitPosition['x']*PixelWidth+(PixelWidth/2-1.5), FruitPosition['y']*PixelWidth-1, 3, 3))

        if not 0<=snake[0]['x']<=window_x/PixelWidth-1:
            Dead = True
        if not 0<=snake[0]['y']<=window_y/PixelWidth-1:
            Dead = True
        if snake[0] in snake[1:]:
            Dead = True

        pygame.display.update()
        fps.tick(snake_speed)
    return(Score)

Score = 0

while True:
    PixelWidth, snake_speed = Menu(Score, PixelWidth)
    Score = Play()
    if Score>HighScore:
        HighScore = Score

    '''
    TODO:
    Quit button.
    Add more settings.
    2-Player
    Add an AI?
    '''