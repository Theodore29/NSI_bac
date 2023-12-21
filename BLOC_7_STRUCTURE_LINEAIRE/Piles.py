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

P=Pile()
print(P.est_vide())
P.push(4)
print(P.est_vide())
P.push(9)
P.push(5)
P.push(3)
print(P.taille())
print(str(P))
s=P.pop()
print(str(P))
print("l'élément dépiler est : ",s)
print(P.est_vide())
print(P.taille())
print(P.sommet())
    


    


    
