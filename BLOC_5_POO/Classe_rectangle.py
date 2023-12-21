class Rectangle(object):

    def __init__(self,L,l):
        if L<0 or l<0:
            raise ValueError("La longueur et la largeur ne peuvent pas être négative")
        if L>=l :
            self.longueur=L
            self.largeur=l
        else:
            self.longueur=l
            self.largeur=L

    def aire(self):
        return self.longueur*self.largeur

    def perimetre(self):
        return 2*(self.longueur+self.largeur)


rect=Rectangle(10,6)
rect1=Rectangle(2,6)

print(rect.aire())
print(rect.perimetre())

print(rect1.longueur)
print(rect1.aire())
print(rect1.perimetre())
