class File(object):

    def __init__(self):
        self.contenu=[]

    def __str__(self):
        a="In -->"
        for i in range(len(self.contenu)):
            
            a=a+str(self.contenu[-i-1])+"-->"
        return a

    def add(self, element):
        self.contenu.append(element)

    def est_vide(self):
        return len(self.contenu)==0

    def taille(self):
        return len(self.contenu)


    def take(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        a=self.contenu[0]
        del(self.contenu[0])
        return a


F=File()
print(F.est_vide())
F.add(4)
print(F.est_vide())
print(str(F))
F.add(9)
print(str(F))
F.add(5)
print(str(F))
F.add(3)
print(str(F))
print(F.taille())
print(str(F))
s=F.take()
print(str(F))
print("L'élément défilé est  : ",s)
print(F.taille())

        

    
