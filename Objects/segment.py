from __future__ import annotations
from point import Point
from functools import total_ordering

@total_ordering
class Segment:
    '''
    line segments
    '''
    def __init__(self,p1:Point,p2:Point):
        '''
        create segments between p1 and p2
        '''
        self.p1 = p1
        self.p2 = p2
    def translate(self,dx:int,dy:int):
        '''
        move segment by dx horizontally and dy vertically
        '''
        self.p1.translate(dx,dy)
        self.p2.translate(dx,dy)
    def length(self)-> float:
        return self.p1.distance(self.p2)
    def __lt__(self, other_segment:Segment) -> bool:
        return isinstance(other_segment,Segment) and self.length() < other_segment.length()
    def __eq__(self, other_segment:Segment):
        return isinstance(other_segment,Segment) and self.length() == other_segment.length()
    def __repr__(self):
        return f'segment between {self.p1} and {self.p2}'
#########

p1 = Point(3,4)
p2 = Point(0,0)
seg1 = Segment(p1,p2)
seg1.translate(3,5)
seg2 = Segment(p2,p1)
print(seg1.length())
print(seg1< seg2)
print(seg1>= seg2)
print(seg1 > seg2)
print(seg1 == seg2)

