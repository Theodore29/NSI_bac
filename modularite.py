from random import *

##help(random)
###Il faut entrer un nombre X dans l'intervalle [0,1)
##
##for i in range(10):
##    print(random())

class Nb_complexes(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return str(self.a) + "+" + str(self.b)+ "i"


    def __add__(self,c):
        return Nb_complexes((self.a + c.a ),(self.b + c.b))

    def __sub__(self,c):
        return Nb_complexes((self.a - c.a ),(self.b - c.b))

    def __mul__(self,c):





a=1
b=3
c=4

n1=Nb_complexes(a,b)
n2=Nb_complexes(a,c)

print(n1.__add__(n2))