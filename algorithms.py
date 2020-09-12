
import random




def random_direction():
    direction = random.randint(0, 3)
    return direction


def BFS(grid,start,destination):
    
 
    
    start.color = "gray"
    
    start.distance = 0
    
    gray_queue = []
    gray_queue.append(start)
    adjacents = []
    
    food = grid[destination[0]][destination[1]] #foodun bulunduğu grid
    while(gray_queue):
        u = gray_queue.pop()
        
        
        if (u.row == food.row and u.col == food.col): #yemi bulduk
            #print("BULDUK")
            return 0
        
        try:
            #u nun komşuları body olmayan
            if (grid[u.row+1][u.col].any_body == False and (u.row != 19)):
                adjacents.append(grid[u.row+1][u.col])
            if (grid[u.row-1][u.col].any_body == False and (u.row != 0)):
                 adjacents.append(grid[u.row-1][u.col])
            if (grid[u.row][u.col+1].any_body == False and (u.col != 19)):
                  adjacents.append(grid[u.row][u.col+1])
            if (grid[u.row][u.col-1].any_body == False and (u.col != 0)):
                  adjacents.append(grid[u.row][u.col-1])
         
        except:
            #print("HATA")
            pass
        
        for v in adjacents:
            
            if v.color == "white" and v: #komşu'nun rengi beyazsa ve komşu mevcutsa(v köşelerde olabilir)
                v.color = "gray"
               
                v.distance = u.distance + 1
                v.parent = u
                #print(v.distance)
                gray_queue.append(v)
        
        u.color = "black"


    return 1

def print_path(grid,s,v):
    path = []
    if v.row == s.row and v.col == s.col:
        #print(s.row,s.col)
        path.append((s.row,s.col))
    elif not v.parent:
        print("Yol yok")
    else:
        print_path(grid, s, v.parent)
        #print(v.row,v.col)
        path.append((v.row,v.col))

        return path
        
        
        
            
       
    
    

