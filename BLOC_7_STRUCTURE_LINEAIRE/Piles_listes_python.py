class Pile(object):

    def __init__(self):
        self.contenu=[]

    def __str__(self):
        a=""
        for i in range(len(self.contenu)):
            
            a=a+"|--"+str(self.contenu[-i-1])+"--|"+'\n'+"|-----|"+'\n'
        return a

    def push(self, element):
        self.contenu.append(element)

    def est_vide(self):
        return len(self.contenu)==0

    def taille(self):
        return len(self.contenu)

    def sommet(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        return self.contenu[-1]

    def pop(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        a=self.contenu[-1]
        del(self.contenu[-1])
        return a



P=Pile()
print(P.est_vide())
P.push(4)
print(P.est_vide())
P.push(9)
P.push(5)
P.push(3)
print(P.taille())
print(str(P))
print(P.sommet())
s=P.pop()
print(str(P))
print("l'élément dépiler est : ",s)
print(P.est_vide())
print(P.taille())
print(P.sommet())


        

    
