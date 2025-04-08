class Point:
    def __init__(self): #this one is ignored always 
        '''
        creating a 2-d point at (0,0)
        '''
        self.x = 0
        self.y = 0
    def __init__(self,x: int,y:int): 
        '''
        create 2d point at x,y
        '''
        self.x = x
        self.y = y
###############################
p1 = Point(3,5)
print(p1.x,p1.y)