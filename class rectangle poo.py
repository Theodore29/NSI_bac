from math import *
class Rectangle(object):
    def __init__(self,L,l):
        if L==0 or l==0:
            raise ValueError("veuillez entreé des longeurs et largeurs différentes de 0")
        if L < l :
            self.longueur = l
            self.largeur = L
        else :
            self.longueur = L
            self.largeur = l

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * self.largeur + 2* self.longueur

r1=Rectangle(4,9)
print(r1.aire())
print(r1.perimetre())

#exercice 3 :

class Angle(object):
    def __init__(self,angle):
        if angle > 360 or angle < 0 :
            raise ValueError("entrez un angle compris entre 0 et 1")
        else : self.angle = angle

    def __str__(self):
        return str(self.angle) + " degrés"


    def ajouter(self,angle1):
        x= self.angle + angle1.angle
        return x%360

    def rad(self):
        return self.angle*pi/180


    def cos(self,angle_conv):
        return cos(self.rad)

    def sin(self,angle_conv):
        return sin(self.rad)



a1 = Angle(60)
a2 = Angle(80)
print(str(a1))
print(a1.ajouter(a2))
print(a1.cos(a1))

