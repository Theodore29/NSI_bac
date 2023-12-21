from turtle import *



##t=Turtle()
##pendown()
##fd(100)
##left(60)
##fd(100)
##right(120)
##fd(100)
##left(60)
##fd(100)



def courbeVk(n,l):

    pendown()
    if n == 0:
        fd(l)
    else :
        courbeVk(n-1,l/3)
        left(60)
        courbeVk(n-1,l/3)
        right(120)
        courbeVk(n-1,l/3)
        left(60)
        courbeVk(n-1,l/3)











fenetre=Screen()
penup()
goto(200,100)
speed(1000)

def flocon(n,l):
    for i in range(3):
        courbeVk(n,l)
        right(120)


flocon(5,500)

fenetre.exitonclick()










