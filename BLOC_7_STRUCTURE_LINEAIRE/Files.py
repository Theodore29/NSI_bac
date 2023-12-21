class Chaînon(object):

    def __init__(self, v=None,s=None):
        self.val=v
        self.suiv=s

    def __str__(self):
        if self.val is None:
            return '--> Out'
        else:
            return str(self.val)+'-->'+str(self.suiv)

class File(object):

    def __init__(self):
        self.contenu=None


    def est_vide(self):
        if self.contenu is None:
            return True
        return False

    def add(self,element):
        self.contenu=Chaînon(element,self.contenu)

    def __str__(self):
        return str(self.contenu)

    def taille(self):
        if self.est_vide():
            return 0
        compt=1
        Cur=self.contenu
        while Cur.suiv is not None:
            compt=compt+1
            Cur=Cur.suiv
        return compt

    def take(self):
        if self.est_vide():
            raise IndexError("La file est vide")
        Cur=self.contenu
        a=None
        while Cur.suiv is not None:
            a=Cur
            Cur=Cur.suiv
        a.suiv=None
        return Cur.val

F=File()
print(F.est_vide())
F.add(4)
print(F.est_vide())
F.add(9)
F.add(5)
F.add(3)
print(F.taille())
print(str(F))
s=F.take()
print(str(F))
print("L'élément défilé est  : ",s)
print(F.taille())
    

