def area ():
   l=int(input("enter the length of the wall : \n"))
   b= int(input("enter the breath of the wall : \n"))
   area = l*b
   print(f" area of the wall is {area}sq. unit")

area()
def canRequied():
   paint=5
   number_of_cans=area/paint
   print(f"number of cans required is {number_of_cans.__round__()}")

canRequied()


import math


def paint_cal (height, width, cover):
    # height=input("Enter the height of the wall: ")
    # width= input(" Enter the width of the wall: ")
    # cover=input("What ")
    area=height*width
    number_of_cans=math.ceil(area/cover)
    print(f"You'll need {number_of_cans} cans of paint")

test_h= int (input("Height of the wall : "))
test_w=int(input("Width of the wall :   "))
coverage=5 #area covered in 1 can
paint_cal(test_h,test_w,coverage)