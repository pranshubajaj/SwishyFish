import random # For generating random numbers
import sys # We will use sys.exit to exit the program
import pygame
from pygame.locals import * # Basic pygame imports


# can refer pygame.org/docs for seeing commands of pygame


# Global Variables for the game

FPS = 32 
# frames per second : basically 32 images per sec will be shown on screen
# user will not be able to tell that it is just a collection  of images 
SCREENWIDTH = 289
SCREENHEIGHT = 511

# initialise a window or screen for display
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

GROUNDY = SCREENHEIGHT * 0.88
GAME_SPRITES = {}
GAME_SOUNDS = {}
# PLAYER = 'gallery/sprites/bird.png'
PLAYER = 'gallery/sprites/Fish.png'
PLAYER_BLUR = 'gallery/sprites/FishBlur.png'
# BACKGROUND = 'gallery/sprites/background.png'
BACKGROUND = 'gallery/sprites/o2.png'
BACKGROUND_BLUR = 'gallery/sprites/o2Blur.png'
PIPE = 'gallery/sprites/pipe.png'
PIPE_P = 'gallery/sprites/pipeP.png'
PIPE_G= 'gallery/sprites/pipeG.png'
PIPE_BLUR = 'gallery/sprites/pipeBlur.png'
# PAUSE = 'gallery/sprites/pauseBlur.png'
PAUSE = 'gallery/sprites/pause.png'
GET_READY = 'gallery/sprites/getready.png'
GAME_OVER = 'gallery/sprites/gameover.png'
PLAY = 'gallery/sprites/play.png'
HIGHSCORE = 'gallery/sprites/highscore.png'
BOX = 'gallery/sprites/box.png'
SWISHY_FISH = 'gallery/sprites/swishyfish.png'

HighScore = 0


def welcomeScreen():
    """
    Shows welcome images on the screen
    """
    pygame.mixer.music.load('gallery/audio/begin.mp3')
    pygame.mixer.music.play(-1)
    # top left corner:(0,0)
    # specifying x coordinate for blitting(top left corner of image will be displayed from this position )
    sfx = int(SCREENWIDTH/10) - 17
    # specifying y coordinate for blitting
    sfy = int(SCREENHEIGHT/10) - 50
    # messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    # messagey = int(SCREENHEIGHT*0.13)
    hsX = int(SCREENWIDTH/3) - 17
    hsY = int(SCREENHEIGHT/1.5) 
    
    boxX = int(SCREENWIDTH/4) - 28
    boxY = int(SCREENHEIGHT/1.2) - 20

    hisc=open("highscore.txt","r+")
    h=hisc.read()
    global HighScore
    HighScore = int(h)
    hisc.close()

    myDigits = [int(x) for x in list(str(HighScore))]
    width = 0
    for digit in myDigits:
        width += 15
    

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            # QUIT: x button
            # KEYDOWN: key is pressed
            # K_ESCAPE: esc key 
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit() # deactivates pygame library
                sys.exit() # exit the program

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                pygame.mixer.music.stop()
                return
            else:
                # blit: display image on screen
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                # SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['swishyFish'], (sfx, sfy))    
                # SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))   
                SCREEN.blit(GAME_SPRITES['highScore'], (hsX, hsY))   
                SCREEN.blit(GAME_SPRITES['box'], (boxX, boxY))
                Xoffset = (SCREENWIDTH - width)/2 - 4# centre krne ke liye   
                for digit in myDigits:
                    SCREEN.blit(pygame.transform.scale(GAME_SPRITES['numbers'][digit], (15,25)), (Xoffset, SCREENHEIGHT/1.2 + 22))
                    Xoffset += 15
                # SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
 # pygame.display.update(): the screen will be updated only after this fnction has run
                pygame.display.update()# Update portions of the screen for software displays
                FPSCLOCK.tick(FPS) # update the clock, control fps



def startGame():
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/2)
    
    readyX = int(SCREENWIDTH/5)
    readyY = int(SCREENHEIGHT/5) - 20

    playX = int(SCREENWIDTH/3.2)
    playY = int(SCREENHEIGHT/3.5) -20

    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit() # deactivates pygame library
                sys.exit() # exit the program
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return # return and start game by entering mainGame
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['getReady'], (readyX, readyY))    
                SCREEN.blit(GAME_SPRITES['play'], (playX, playY))    
                  
                # SCREEN.blit(GAME_SPRITES['base'], (0, GROUNDY))    
 # pygame.display.update(): the screen will be updated only after this fnction has run
                pygame.display.update()# Update portions of the screen for software displays
                FPSCLOCK.tick(FPS) # update the clock, control fps



def pauseF(playerx, playery, upperPipes, lowerPipes, score):
    pygame.mixer.music.pause()
    pauseX = (SCREENWIDTH - GAME_SPRITES['pause'].get_width())/2
    pauseY = (SCREENHEIGHT - GAME_SPRITES['pause'].get_height())/2
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit() # deactivates pygame library
                sys.exit() # exit the program
            elif event.type==KEYDOWN and event.key==K_s:
                pygame.mixer.music.unpause()
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                    if upperPipe['c'] == 1:
                        SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                        SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
                    elif upperPipe['c'] == 2:
                        SCREEN.blit(GAME_SPRITES['pipeP'][0], (upperPipe['x'], upperPipe['y']))
                        SCREEN.blit(GAME_SPRITES['pipeP'][1], (lowerPipe['x'], lowerPipe['y']))
                    elif upperPipe['c'] == 3:
                        SCREEN.blit(GAME_SPRITES['pipeG'][0], (upperPipe['x'], upperPipe['y']))
                        SCREEN.blit(GAME_SPRITES['pipeG'][1], (lowerPipe['x'], lowerPipe['y']))

                # SCREEN.blit(GAME_SPRITES['base'], (0, GROUNDY))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['pause'], (pauseX, pauseY))
                # for displaying score: 
                myDigits = [int(x) for x in list(str(score))]
                width = 0
                for digit in myDigits:
                    width += GAME_SPRITES['numbers'][digit].get_width()
                Xoffset = (SCREENWIDTH - width)/2 # centre krne ke liye

                for digit in myDigits:
                    SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                    Xoffset += GAME_SPRITES['numbers'][digit].get_width()
                pygame.display.update()# Update portions of the screen for software displays
                FPSCLOCK.tick(FPS) # update the clock, control fps



def mainGame():
    pygame.mixer.music.load('gallery/audio/ocean.mp3')
    pygame.mixer.music.play(-1)
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe(score)
    newPipe2 = getRandomPipe(score)

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y'], 'c': newPipe1[0]['c']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y'],'c': newPipe2[0]['c'] }
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y'], 'c': newPipe1[1]['c']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y'], 'c': newPipe2[1]['c']}
    ]

    # velocity of pipe 
    pipeVelX = -4 # left 

    playerVelY = -9 # up
    playerMaxVelY = 10 #  maximum velocity in downward direction
    playerMinVelY = -8
    playerAccY = 1 # acceleration in downward direction

    playerFlapAccv = -8 # velocity while flapping( up )
    playerFlapped = False # It is true only when the bird is flapping


    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['swish'].play()
            elif event.type == KEYDOWN and event.key == K_p: # for pause
                pauseF(playerx, playery, upperPipes, lowerPipes, score)

        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            global HighScore
            if score > HighScore:
                hisc=open("highscore.txt","w+")
                hisc.write(str(score))                
                hisc.close()    
            GAME_SOUNDS['die'].play()
            return     

        # check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                # print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()
       


        # if the player doesnt flap we increase its velocity in downward direction
        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY


        if playerFlapped:
            playerFlapped = False 
                       
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, SCREENHEIGHT - playery - playerHeight)

        # move pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe(score)
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < - GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        
        
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                if upperPipe['c'] == 1:
                    SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                    SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
                elif upperPipe['c'] == 2:
                    SCREEN.blit(GAME_SPRITES['pipeP'][0], (upperPipe['x'], upperPipe['y']))
                    SCREEN.blit(GAME_SPRITES['pipeP'][1], (lowerPipe['x'], lowerPipe['y']))
                elif upperPipe['c'] == 3:
                    SCREEN.blit(GAME_SPRITES['pipeG'][0], (upperPipe['x'], upperPipe['y']))
                    SCREEN.blit(GAME_SPRITES['pipeG'][1], (lowerPipe['x'], lowerPipe['y']))

        # SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

        # for displaying score: 
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2 # centre krne ke liye

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)





def isCollide(playerx, playery, upperPipes, lowerPipes):
    # bird hits roof or ground
    if playery> GROUNDY - 25  or playery<0:
        pygame.mixer.music.stop()
        GAME_SOUNDS['hit'].play()
        return True
    if playery> SCREENHEIGHT - 25  or playery<0:
        pygame.mixer.music.stop()
        GAME_SOUNDS['hit'].play()
        return True
    
    # bird hits upperpipe
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['player'].get_width()-2):
            pygame.mixer.music.stop()
            GAME_SOUNDS['hit'].play()
            return True

    # bird hits lowerpipe
    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']-3.5 and abs(playerx - pipe['x']) < GAME_SPRITES['player'].get_width()-2):
            pygame.mixer.music.stop()
            GAME_SOUNDS['hit'].play()
            return True

    return False






def getRandomPipe(score):
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    # offset = SCREENHEIGHT/3
    offset = SCREENHEIGHT/2.65
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - 1.6 * offset))
    pipeX = SCREENWIDTH + 10 # not used ig
    y1 = pipeHeight - y2 + offset - (2 * score)
    r = random.randint(1,3)
    # '2 * score' is kinda increasing the diffculty level as it is reducing the gap between the 2 pipes as the score gets higher
    pipe = [
        {'x': pipeX, 'y': -y1, 'c': r}, #upper Pipe
        {'x': pipeX, 'y': y2, 'c': r} #lower Pipe
    ]
    return pipe






if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Swishy Fish by Pranshu')
    

    # convert_alpha: function that optimises image for game
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['baseBlur'] =pygame.image.load('gallery/sprites/baseBlur.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )
    GAME_SPRITES['pipeP'] =(pygame.transform.rotate(pygame.image.load( PIPE_P).convert_alpha(), 180), 
    pygame.image.load(PIPE_P).convert_alpha()
    )
    GAME_SPRITES['pipeG'] =(pygame.transform.rotate(pygame.image.load( PIPE_G).convert_alpha(), 180), 
    pygame.image.load(PIPE_G).convert_alpha()
    )
    GAME_SPRITES['pipeBlur'] =(pygame.transform.rotate(pygame.image.load( PIPE_BLUR).convert_alpha(), 180), 
    pygame.image.load(PIPE_BLUR).convert_alpha()
    )

    # Game sounds
    # could change for mac
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    # GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
    GAME_SOUNDS['swish'] = pygame.mixer.Sound('gallery/audio/swish.mp3')
    # GAME_SOUNDS['ocean'] = pygame.mixer.Sound('gallery/audio/ocean.mp3')

    # convert: used for quick blitting
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['backgroundBlur'] = pygame.image.load(BACKGROUND_BLUR).convert()
    GAME_SPRITES['playerBlur'] = pygame.image.load(PLAYER_BLUR).convert_alpha()
    GAME_SPRITES['pause'] = pygame.image.load(PAUSE).convert_alpha()
    GAME_SPRITES['getReady'] = pygame.image.load(GET_READY).convert_alpha()
    GAME_SPRITES['gameOver'] = pygame.image.load(GAME_OVER).convert_alpha()
    GAME_SPRITES['play'] = pygame.image.load(PLAY).convert_alpha()
    
    
    GAME_SPRITES['swishyFish'] = pygame.image.load(SWISHY_FISH).convert_alpha()



    GAME_SPRITES['highScore'] = pygame.transform.scale(pygame.image.load(HIGHSCORE).convert_alpha(), (120,100))
    GAME_SPRITES['box'] = pygame.transform.scale(pygame.image.load(BOX).convert_alpha(),(190,110))
    

    welcomeScreen() # Shows welcome screen to the user until he presses a button

    while True:
        # welcomeScreen() # Shows welcome screen to the user until he presses a button
        startGame()
        mainGame() # This is the main game function

        # blitting gameover image 
        goX = int(SCREENWIDTH/5) - 20
        goY = int(SCREENHEIGHT/3)  
        SCREEN.blit(GAME_SPRITES['gameOver'], (goX, goY))
        pygame.display.update()# Update portions of the screen for software displays
        FPSCLOCK.tick(FPS)  
        
        
