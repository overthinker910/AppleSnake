import pygame
import time
import random#to get random apple position
pygame.init()
black=(0,0,0)#rgb value
grey=(72,72,72)
dgrey=(36,37,38)
white=(255,255,255)
coral=(219,119,141)
pink=(254,127,156)
red =(202,0,42)
green=(50,205,50)
purple=(177, 156, 217)
lumber=(255,223,211)#yellow pastel
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))#making the base screen
pygame.display.set_caption('Slither')#game title
icon=pygame.image.load('apple.png')
img=pygame.image.load('snakehead.png')#snake head image
appleimg=pygame.image.load('apple.png')#apple
pygame.display.set_icon(icon)#set apple as logo 
clock=pygame.time.Clock()
AppleThickness=30
#smallfont=pygame.font.SysFont(None,25)#font type,sysfont is system font
smallfont=pygame.font.SysFont("comicsansms",15)
medfont=pygame.font.SysFont("comicsansms",30)
largefont=pygame.font.SysFont("comicsansms",50)

block_size=20
FPS=10
direction ="right"#for snake head position

def score(score):
    text=smallfont.render("Score:"+str(score),True,purple)
    gameDisplay.blit(text,[0,0])

    


def randApplegen():
    randAppleX=random.randrange(0,(display_width-AppleThickness))#random coord of x,y for apple
    randAppleY=random.randrange(0,(display_height-AppleThickness))#-apple thickness so part of apple doesnt get printed out of the block at times
    randAppleX=round(randAppleX)#/10.0)*10.0 
    randAppleY=round(randAppleY)#/10.0)*10.0
    return randAppleX,randAppleY


def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#if user clicks on cross
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:#clicks on c
                    intro=False
                if event.key==pygame.K_q:#clicks on q
                    pygame.quit()
                    quit()        
            
        gameDisplay.fill(grey)
        message_to_screen("Welcome to Slither",purple,0,"medium")
        
        message_to_screen("The more apples you eat ,the longer you get",lumber,-40,"small")
        message_to_screen("IF you run into yourself or the edges you die",lumber,-70,"small")
        message_to_screen("Press c to play and q to quit ",lumber,30,"small")

        pygame.display.update()
        clock.tick(15)#stays for 15 sec

        
def snake(block_size,snakelist):
    if(direction=="right"):#chsanging head dirc acc to the direc we go to 
        head=pygame.transform.rotate(img,270)
    if(direction=="left"):
        head=pygame.transform.rotate(img,90)
    if(direction=="up"):
        head=img
    if(direction=="down"):
        head=pygame.transform.rotate(img,180)
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][-1]))#head will be the last element of the snakelist
    
    for XnY in snakelist[:-1]:#everything before the head(body).. adding the body
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])#block/snake


def text_objects(text,color,size):#to centre the text
    if size=="small":
        textSurface=smallfont.render(text,True,color)
    if size=="medium":
        textSurface=medfont.render(text,True,color)
    if size=="large":
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()
    

def message_to_screen(msg,color,y_displace=0,size="small"):#making function to display text on screen,displace var to print the text at diff positions,size is for font size
    textSurf,textRect=text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)
    
    #screen_text=font.render(msg,True,color)
    #gameDisplay.blit(screen_text,[display_width/2,display_height/2])


def gameLoop():
    global direction #making direction var globle
    direction='right'#direction of snake head when we start the game
    gameExit=False
    gameOver=False#if player wants to play again
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=10
    lead_y_change=0
   
    snakeList=[]#making it empty
    snakeLength=1
    randAppleX,randAppleY=randApplegen()
    
    while not gameExit:#while false
        while gameOver==True:
            gameDisplay.fill(dgrey)
            message_to_screen("Game over" ,pink,-50,size="large")
            
            message_to_screen("press C to play again or Q to quit",lumber,50,size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.type==pygame.QUIT:
                        gameExit=True
                        gameOVer=False
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():#it has everything we do like move the cursor or press some button etc
            if event.type==pygame.QUIT:#if user clicks on cross and wants to exit 
                gameExit=True
            #print(event) to analyse what event happens
            if event.type==pygame.KEYDOWN:
                
                if event.key==pygame.K_LEFT:#left arrow
                    direction="left"
                    lead_x_change=-block_size
                    lead_y_change=0#otherwise it will move diagonally
                elif event.key==pygame.K_RIGHT:#right arrow
                    direction="right"
                    lead_x_change=block_size
                    lead_y_change=0 
                elif event.key==pygame.K_UP:#up arrow
                    direction="up"
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:#down arrow
                    direction="down"
                    lead_y_change=block_size
                    lead_x_change=0
                    
        if(lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0):#so it doesnt go out of the screen
                gameOver=True
            
        lead_x+=lead_x_change
        lead_y+=lead_y_change

        gameDisplay.fill(grey)#background colour
        
        #pygame.draw.rect(gameDisplay,dgrey,[50,50,800,600])#where,colour,[top left coord,b,l]
        #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])#to get apple
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)#list in a list
        if len(snakeList)>snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=True
        
        snake(block_size,snakeList)
        score((snakeLength-1)*10)#snake length starts at 1 but score we want from 0
        pygame.display.update()


     
##        if lead_x>=randAppleX and lead_x<=randAppleX+AppleThickness:#checking if the snake crosses the apple when apple is bigger
##            if lead_y>=randAppleY and lead_y<=randAppleY+AppleThickness:
##                randAppleX=random.randrange(0,(display_width-block_size))#random coord of x,y for apple
##                randAppleY=random.randrange(0,(display_height-block_size))
##                randAppleX=round(randAppleX)#/10.0)*10.0 
##                randAppleY=round(randAppleY)#/10.0)*10.0
##                snakeLength+=1
#function randApplegen() does this so we dont have to type this again and again
        


        if lead_x>randAppleX and lead_x<randAppleX+AppleThickness or lead_x+block_size >randAppleX and lead_x+block_size<randAppleX+AppleThickness:
            if lead_y>randAppleY and lead_y<randAppleY+AppleThickness:
                    randAppleX,randAppleY=randApplegen()
                    snakeLength+=1
            elif lead_y+block_size>randAppleY and lead_y+block_size<randAppleY+AppleThickness:
                    randAppleX,randAppleY=randApplegen()
                    snakeLength+=1
                    
                    
                
                        
            
           
        clock.tick(FPS)#frames per second kind of like the no of times loops run in a sec



    #message_to_screen("You Lose,go outisde you fool ",coral)#to print text render,blit in fuction then outside display and update
    #pygame.display.update()
    #time.sleep(3)#text should stay for 3 sec ..without this it will just come and go 
    pygame.quit()
    quit()
game_intro()
gameLoop()
