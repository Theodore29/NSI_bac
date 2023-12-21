class Chaînon(object):

    def __init__(self, v=None,s=None):
        self.val=v
        self.suiv=s

    def __str__(self):
        if self.val is None:
            return str(self.val)
        else:
            return '|--'+str(self.val)+'--|'+'\n'+'|-----|'+'\n'+str(self.suiv)

class Pile(object):

    def __init__(self):
        self.contenu=None


    def est_vide(self):
        if self.contenu is None:
            return True
        return False

    def push(self,element):
        self.contenu=Chaînon(element,self.contenu)


    def __str__(self):
        return str(self.contenu)


    def pop(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        a=self.contenu.val
        self.contenu=self.contenu.suiv
        return a

    def taille(self):
        if self.est_vide():
            return 0
        compt=1
        Cur=self.contenu
        while Cur.suiv is not None:
            compt=compt+1
            Cur=Cur.suiv
        return compt

    def sommet(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        a=self.contenu.val
        return a

class File(object):

    def __init__(self):
        self.entree=Pile()
        self.sortie=Pile()

    def add(self,element):
        self.entree.push(element)

    def est_vide(self):
        return self.entree.est_vide() and self.sortie.est_vide()

    def __str__(self):
        a=str(self.entree)+'\n'+'######'+'\n'+str(self.sortie)
        return a

    def taille(self):
        return self.entree.taille()+self.sortie.taille()

    def take(self):
        if self.est_vide():
            raise ValueError("La files est vide")
        if not self.sortie.est_vide():
            return self.sortie.pop()
        else:
            while not self.entree.est_vide():
                a=self.entree.pop()
                self.sortie.push(a)
            return self.sortie.pop()

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
F.add(8)
F.add(6)
print(str(F))
print(F.taille())
s=F.take()
print(str(F))
print("L'élément défilé est  : ",s)
s=F.take()
print(str(F))
print("L'élément défilé est  : ",s)
s=F.take()
print(str(F))
print("L'élément défilé est  : ",s)
s=F.take()
print(str(F))
print("L'élément défilé est  : ",s)






            






