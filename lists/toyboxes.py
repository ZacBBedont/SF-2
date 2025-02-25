"""
given n unopened boxes with k number of figurines in each box. 
The boxes cannot have the order of the figurines changed
The box cannot be rotated
each figurine has a specified height
number of figurines in each box may vary (not empty)
we would like to organize each box so that they are arranged in increasing order (or same height) of figurine heights from left to right
not necessarily possible at all times

input:

first line: integer n representing no. of boxes
next n line(s): one for each box. Each line begins with k, followed by k integers giving the height from left to right separated by a space

ex:

2
3 4 5 7
2 6 8

output: no

ex2:

2
3 4 5 7
8 8

output:yes
"""
"""
top-down design: capturing main tasks of the solution
some tasks will not require much code, just solve it directly
other tasks may require you to write functions


Main program:

TODO: read input
TODO: check if each individual box is in order
TODO: obtain new list of boxes with only endpoints
TODO: sort the boxes according to the interval
TODO: output

"""
def readboxes(n):
    lst_boxes = []
    for i in range(n):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
        lst_boxes.append(box)
    return lst_boxes

def allBoxesOk(boxes):
    for box in boxes:
        if sorted(box) != box:
            return False
    return True

def boxIntervals(boxes):
    intervals = []
    for box in boxes:
        intervals.append([box[0],box[-1]])
    return intervals

def allIntervalsOk(intervals):
    for interval in range(len(intervals)-1):
        if intervals[interval][1] > intervals[interval+1][0]:
            return False
    return True

n = int(input())
boxes = readboxes(n)

if not allBoxesOk(boxes):
    print("No")
else:
    intervals = boxIntervals(boxes)
    intervals.sort()
    if allIntervalsOk(intervals):
        print("Yes")
    else:
        print("No")
