from math import*

class Angle(object):

    def __init__(self,a):
        self.angle=a%360

    def __str__(self):
        return str(self.angle)+" degrés"

    def ajouter(self,angle2):
        return (self.angle+angle2.angle)%360

    def radian(self):
        return self.angle*pi/180

    def cos(self):
        return cos(self.radian())


    def sin(self):
        return sin(self.radian())

    def cos1(self):
        a=self.angle*pi/180
        b=cos(a)
        return b


ang=Angle(60)
ang1=Angle(390)

print(str(ang))
print(str(ang1))

print(ang.ajouter(ang1))
print(ang.radian())
print(ang.cos1())
print(ang.sin())

print(str(ang1))
print(ang1.radian())
print(ang1.cos1())
print(ang1.sin())

