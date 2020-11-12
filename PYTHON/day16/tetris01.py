import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 960

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pos_x = 200
pos_y = 200


block2D =[
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]
];
stack2D =[
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[11,11,11,11,0,0,0,0,0,0]
];
print2D =[
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]
];


class Block:
    def __init__(self):
        self.kind = 5
        self.status = 0
        self.i = 2
        self.j = 4

    def __str__(self):
        return "kind : {} / status : {} / i : {} / j : {}".format(self.kind ,self.status,self.i,self.j )
    
    
        
        
block = Block();

def isCrash():
    for i in range(len(print2D)):
        for j in range(len(print2D[i])):
            if block2D[i][j] > 0 and stack2D[i][j] >0:
                return True
         
    return False


def show2D(p2D):
    for i in p2D:
        print(i)

def setPrint2DByBlockStack():
    for i in range(len(print2D)):
        for j in range(len(print2D[i])):
         
            if stack2D[i][j] > 0:
                print2D[i][j] = stack2D[i][j];
         
            if block2D[i][j] > 0:
                print2D[i][j] = block2D[i][j];


b1 = (128,128,128) 
b2 = (128,128,128) 
b3 = (128,128,128) 
b4 = (128,128,128) 
b5 = (128,128,128) 
b6 = (128,128,128) 
b7 = (128,128,128) 


s1 = (0,0,255) 
s2 = (0,0,255) 
s3 = (0,0,255) 
s4 = (0,0,255) 
s5 = (0,0,255) 
s6 = (0,0,255) 
s7 = (0,0,255) 
                    
def myrender():
    screen.fill(black)
    for i in range(23):
        for j in range(10):
            if print2D[i][j] == 0 : pygame.draw.rect(screen, white, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 1 : pygame.draw.rect(screen, b1, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 2 : pygame.draw.rect(screen, b2, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 3 : pygame.draw.rect(screen, b3, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 4 : pygame.draw.rect(screen, b4, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 5 : pygame.draw.rect(screen, b5, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 6 : pygame.draw.rect(screen, b6, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 7 : pygame.draw.rect(screen, b7, (30*j, 30*i,29,29),0 )
                
            if print2D[i][j] == 11 :pygame.draw.rect(screen, s1, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 12 :pygame.draw.rect(screen, s2, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 13 :pygame.draw.rect(screen, s3, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 14 :pygame.draw.rect(screen, s4, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 15 :pygame.draw.rect(screen, s5, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 16 :pygame.draw.rect(screen, s6, (30*j, 30*i,29,29),0 )
            if print2D[i][j] == 17 :pygame.draw.rect(screen, s7, (30*j, 30*i,29,29),0 )
         
         
    
    pygame.display.update()
    

def changeStatus():
    if block.kind == 1 :
        pass
    if block.kind == 2 or block.kind ==3 or block.kind == 4 :
        if block.status==0:
            block.status = 1
        elif block.status == 1:
            block.status = 0
    if block.kind == 5 or block.kind == 6 or block.kind == 7:
        if block.status == 0:
            block.status = 1
        elif block.status == 1:
            block.status = 2
        elif block.status == 2:
            block.status = 3
        elif block.status == 3:
            block.status = 0


def setBlock2DByBlock():
    for i in range(len(print2D)):
        for j in range(len(print2D[i])):
            print2D[i][j] = 0;
            block2D[i][j] = 0;
    
    if block.kind == 5:
        if block.status == 0 :
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i      ][block.j-1   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
        elif block.status == 1:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
        elif block.status == 2:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i      ][block.j-1 ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
            block2D[block.i+1   ][block.j   ] = block.kind;
        elif block.status == 3:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j   ] = block.kind;
            block2D[block.i      ][block.j-1   ] = block.kind;
     
    elif block.kind == 1:
        block2D[block.i      ][block.j   ] = block.kind;
        block2D[block.i      ][block.j+1   ] = block.kind;
        block2D[block.i+1   ][block.j   ] = block.kind;
        block2D[block.i+1   ][block.j+1   ] = block.kind;
    
    elif block.kind == 2:
        if block.status == 0:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i      ][block.j-1   ] = block.kind;
            block2D[block.i+1   ][block.j-1   ] = block.kind;
        elif block.status == 1:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j-1   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
        
    elif block.kind == 3:
        if block.status == 0:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
            block2D[block.i+1   ][block.j+1   ] = block.kind;
        elif block.status == 1:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
            block2D[block.i+1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j-1   ] = block.kind;   
        
    elif block.kind == 4 :
        if block.status == 0:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-2   ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j   ] = block.kind;
        elif block.status == 1:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i      ][block.j-2   ] = block.kind;
            block2D[block.i      ][block.j-1   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
            
    elif block.kind == 6:
        if block.status == 0:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j-1   ] = block.kind;
        elif block.status == 1:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i      ][block.j-1   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
            block2D[block.i-1   ][block.j+1   ] = block.kind;
        elif block.status == 2:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j+1   ] = block.kind;
        elif block.status == 3:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
            block2D[block.i      ][block.j-1   ] = block.kind;
            block2D[block.i+1   ][block.j-1   ] = block.kind;
    elif block.kind == 7:
        if block.status == 0:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j+1   ] = block.kind;
        elif block.status == 1:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i      ][block.j-1   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
            block2D[block.i+1   ][block.j+1   ] = block.kind;
        elif block.status == 2:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i-1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j   ] = block.kind;
            block2D[block.i+1   ][block.j-1   ] = block.kind;
        elif block.status == 3:
            block2D[block.i      ][block.j   ] = block.kind;
            block2D[block.i      ][block.j+1   ] = block.kind;
            block2D[block.i      ][block.j-1   ] = block.kind;
            block2D[block.i-1   ][block.j-1   ] = block.kind;


clock = pygame.time.Clock()
while True:
    clock.tick(60)
    flag_render = False
    
    flagDown = False
    pre_i      = block.i
    pre_j      = block.j
    pre_status = block.status
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        block.j -= 1
        flag_render = True
        
    if key_event[pygame.K_RIGHT]:
        block.j += 1
        flag_render = True

    if key_event[pygame.K_UP]:
        changeStatus()
        flag_render = True

    if key_event[pygame.K_DOWN]:
        block.i += 1
        flag_render = True
    
    if key_event[pygame.K_d]:
        show2D(stack2D)
        print("----")
        show2D(block2D)
        print("----")
        show2D(print2D)
        print(block)
    
   
    if flag_render:
        
        flagOut = False
        
        try:
            block.j -=10
            setBlock2DByBlock()
            block.j +=10
            setBlock2DByBlock()
        except:
            flagOut = True
            pass
        
        flagCrash = isCrash()
        
        if flagOut or flagCrash:
            block.i       = pre_i
            block.j       = pre_j
            block.status    = pre_status
            setPrint2DByBlockStack()
            
        setPrint2DByBlockStack()
        myrender();
        
        
        
        print(block)
        
       
    

    