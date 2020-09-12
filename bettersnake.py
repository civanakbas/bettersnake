import pygame
import random
from sys import exit
import algorithms


class Node(object):
    def __init__(self,row,col,width):       
        self.row = row
        self.col = col
        self.width = width
        self.color = "white"
        self.distance = 1000
        self.parent = None
        self.any_body = False
        
        
#Makes a grid of size 30*30's for any width    
def make_grid(width,gridSize):

    grid = []
    rows = width//gridSize
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,gridSize)
            grid[i].append(node)
            
    
    return grid


#Body of the snake
class body(object):
    def __init__(self,start,width,gridSize,dirx=1, diry=0, color=(0, 255, 0)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.rows = width//gridSize
        self.color = color
        
        
    #A move function for each body piece
    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0]+self.dirx, self.pos[1]+self.diry)
    
    #Draws each body piece,is called by snake class with a for loop  ######
    def draw(self, surface,gridSize):
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*gridSize+1, j*gridSize+1, gridSize-1, gridSize-1))




#Head of the snake
class snake(object):
    body = []
    turns = {}
    def __init__(self,color,pos,width,gridSize):
        self.color = color
        self.head = body(pos,width,gridSize)
        self.body.append(self.head)
        self.dirx = 1
        self.diry = 0
        self.add_body(width, gridSize)
        self.add_body(width, gridSize)
        
        
        
        
    def move(self,width,gridSize,path):
        
        
        if(self.head.pos[0] > path[0][0]):
            direction = 0
        if(self.head.pos[0] < path[0][0]):
            direction = 1
        if(self.head.pos[1] > path[0][1]):
            direction = 2
        if(self.head.pos[1] < path[0][1]):
            direction = 3
            
        
        if direction == 0:      #Checks for key presses
            self.dirx = -1
            self.diry = 0           
            self.turns[self.head.pos[:]] = [self.dirx, self.diry] #This line and the other 3 elif's below
                                                              #simply takes the position and sends it
                                                              #to turns dictionary for later use
        elif direction == 1:
            self.dirx = 1
            self.diry = 0
            self.turns[self.head.pos[:]] = [self.dirx, self.diry]
                

        elif direction == 2:
            self.dirx = 0
            self.diry = -1
            self.turns[self.head.pos[:]] = [self.dirx, self.diry]
            

        elif direction == 3:
            self.dirx = 0
            self.diry = 1
            self.turns[self.head.pos[:]] = [self.dirx, self.diry]
        
            
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           #Closes the game if user quits
                pygame.quit()                       
                exit()
               
         
                
        
                
        for i,body in enumerate(self.body): # Loop through each body piece 
            position = body.pos[:] #Take the current body pieces position
            if position in self.turns:#If the bodys current position is where the head turned 
                turn = self.turns[position]#Get the direction we should turn
                body.move(turn[0],turn[1])#Move to that direction
                
                if i == len(self.body)-1: #If the body piece is the last piece,remove that position from our dictionary
                    self.turns.pop(position)
            else: #If we are not turning right now
                if ((body.dirx == -1 and body.pos[0] <= 0) or (body.dirx == 1 and body.pos[0] >= (body.rows)-1)
                    or (body.diry == 1 and body.pos[1] >= body.rows-1) or (body.diry == -1 and body.pos[1] <= 0)): #İf we crashed to a wall,reset
                    snk.reset((10, 10),width,gridSize)
                else:
                    body.move(body.dirx, body.diry)  #Move the snake
                
    
    
    
    def reset(self,pos,width,gridSize):
        self.head = body(pos,width,gridSize)
        self.body = []
        self.body.append(self.head)
        self.add_body(width, gridSize)
        self.add_body(width, gridSize)
        self.turns = {}
        self.dirx = 1
        self.diry = 0    
      
        
    def add_body(self,width,gridSize):
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry
        if dx == 1 and dy == 0:
            self.body.append(body((tail.pos[0]-1, tail.pos[1]),width,gridSize))
        elif dx == -1 and dy == 0:
            self.body.append(body((tail.pos[0]+1, tail.pos[1]),width,gridSize))
        elif dx == 0 and dy == 1:
            self.body.append(body((tail.pos[0], tail.pos[1]-1),width,gridSize))
        elif dx == 0 and dy == -1:
            self.body.append(body((tail.pos[0], tail.pos[1]+1),width,gridSize))
            
        self.body[-1].dirx = dx
        self.body[-1].diry = dy
        
                    
        
                    
        
            
        
        
        
        
    #A simple for loop that calls each body pieces draw function   #######
    def draw(self, surface,gridSize):
        for body in self.body:
            body.draw(surface,gridSize)
        
        
        
        
        
        
        
    


            
#Draws the grid,but independent from the grid variable,only for showing the grid.
def draw_grid(surface,width,gridSize):
    rows = width//gridSize
    for i in range(rows):
        pygame.draw.line(surface,(255,255,255),(0,i*gridSize),(width,i*gridSize))
        for j in range(rows):
            pygame.draw.line(surface,(255,255,255),(j*gridSize,0),(j*gridSize,width))
    


#This function draws & redraws screen
def update_screen(surface,width,gridSize,snk,food):
    surface.fill((0,0,0))
    #draw_grid(surface,width,gridSize)
    snk.draw(surface,gridSize)
    food.draw(surface,gridSize)
    pygame.display.update()
    


def random_food(rows,snk):
    positions = snk.body
    
    while True:
        x = random.randrange(rows-10)
        y = random.randrange(rows-10)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:            
            break
        
    return(x,y)
    



def main():
    #Grid variables
    global snk
    width = 600
    gridSize= 30
    snk = snake((0,255,0),(10,10),width,gridSize)
    
    rows = width//gridSize
    #Declarations etc.
    surface = pygame.display.set_mode((width,width))
    
    
    food = body(random_food(rows, snk),width,gridSize, color=(255, 0, 0))
    clock = pygame.time.Clock()
    running = True
   
    
    
    
    
    #GAME LOOP
    while running :
        print(clock.get_fps(), snk.body[0].pos)
        pygame.time.delay(0)
      
        clock.tick(10)
        grid = make_grid(width, gridSize)
        
        if snk.body[0].pos == food.pos:
            snk.add_body(width,gridSize)
            food = body(random_food(rows, snk),width,gridSize,color=(255, 0, 0))
        
        for x in range(len(snk.body)):
            if snk.body[x].pos in list(map(lambda z: z.pos, snk.body[x+1:])):
                snk.reset((10,10),width,gridSize)
                break
        
        start = snk.head.pos  #take head coord.
        
        for i in snk.body:
           grid[i.pos[0]][i.pos[1]].any_body = True
           
        
        
        while True:
            if(algorithms.BFS(grid,grid[start[0]][start[1]],food.pos) == 0) :#her loop ta yılanın kafasının koordinatını BFS ye yolla
                path = algorithms.print_path(grid, grid[start[0]][start[1]], grid[food.pos[0]][food.pos[1]])
                break
        
        
        
        snk.move(width,gridSize,path)
        update_screen(surface,width,gridSize,snk,food)
    
   
    
    
    
    
    










if __name__ == "__main__":
    main()