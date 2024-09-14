import pygame
pygame.init()

win=pygame.display.set_mode((870,480))
pygame.display.set_caption("Dungeon Deities")



walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock=pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.JumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0
    def draw(self,win):
        if self.walkCount+1>27:
            self.walkCount=0

        if self.left:
            win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        elif self.right:
            win.blit(walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        else:
            win.blit(char,(self.x,self.y))

def redrawGameWindow():
    win.blit(bg,(0,0))
    savaricBlc.draw(win)
    pygame.display.update()

    
#mainloop
savaricBlc=player(50,350,64,64)
run=True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and savaricBlc.x!=0:
        savaricBlc.x-=savaricBlc.vel
        savaricBlc.left=True
        savaricBlc.right=False
    elif keys[pygame.K_RIGHT] and savaricBlc.x!=820:
        savaricBlc.x+=savaricBlc.vel
        savaricBlc.right=True
        savaricBlc.left=False
    else:
        savaricBlc.right=False
        savaricBlc.left=False
        savaricBlc.walkCount=0
        
    if not(savaricBlc.isJump):
        if keys[pygame.K_SPACE]:
            savaricBlc.isJump=True
            savaricBlc.right=False
            savaricBlc.left=False
            savaricBlc.walkCount=0
    else:
        neg=1
        if savaricBlc.JumpCount<0:
            neg=-1
        if savaricBlc.JumpCount>=-10:
            savaricBlc.y-=(savaricBlc.JumpCount ** 2)*0.5*neg
            savaricBlc.JumpCount-=1
        else:
            savaricBlc.isJump=False
            savaricBlc.JumpCount=10
    redrawGameWindow()
    

pygame.quit()
