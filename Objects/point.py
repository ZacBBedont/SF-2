from __future__ import annotations
import math

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
    def translate(self,dx:int,dy:int):
        '''
        move point d horizontally and dy vertically
        '''
        self.x += dx
        self.y += dy
    def distance(self,other_point:Point) -> float:
        '''
        return distance between this point and other point
        '''
        a = (other_point.x-self.x) ** 2
        b = (other_point.y - self.y) ** 2
        return math.sqrt(a+b)
    def __repr__(self)-> str:
        '''
        return x,y coords as tuple
        '''
        return f'({self.x},{self.y})'
    def __lt__(self,other_point:Point)-> bool:
        '''
        return True if this point and other point are of type Point,
        and x,y coords of this point are less than xy coords of other point
        '''
        return isinstance(other_point,Point) and self.x < other_point.x and self.y < other_point.y
    def __eq__(self, other_point:Point)-> bool:
        return isinstance(other_point,Point) and self.x == other_point.x and self.y == other_point.y
###############################
if __name__ == 'main':
    p1 = Point(2,7)

    p1.translate(1,4)

    p2 = Point(9,5)
    p1.distance(p2)

    print(p1<p2)
    print(p1 == p2)