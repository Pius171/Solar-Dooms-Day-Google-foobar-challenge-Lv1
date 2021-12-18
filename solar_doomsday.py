## when you square root a number 'A' it gives
## the root of the number and that number
## acan serve as the area of square since
## both side of a square are equal
## but when the number 'A'is not a perfect
## and you find it root it gives you a decimal
## number but the whole number part is the closet
## number that when square would give a perfect square
## The code below works on this priciple
##
## Find the perfect square or the closer perfect square
## to the number given, take only the whole number part
## , suare it and add it to a list,if there is still a
## reminder of areas to fill, get the reminder and repeat
## the process again on the remainder, continue to do this
## until the sum of the contents in the list equals the given area

#import math as m

def solution(area_of_rect):
    import math as m
    squares=[] # list to store area of squares
    area=area_of_rect
    area_left= area_of_rect
    while True:
        
        area = m.sqrt(area)
        area=int(area)**2
        squares.append(area)
        area=area_left-area # get reminder of areas to fill
        area_left = area
        if sum(squares) == area_of_rect:
            break

    return squares

while True:
    try:
        print(solution(int(input("Type in the area of the wall: "))))

    except:
        print("integers only");
