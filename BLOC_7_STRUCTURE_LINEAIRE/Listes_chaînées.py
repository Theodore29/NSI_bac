class Chaînon(object):

    def __init__(self, v=None,s=None):
        self.val=v
        self.suiv=s

    def __str__(self):
        if self.val is None:
            return str(self.val)
        else:
            return str(self.val)+'--'+str(self.suiv)

class Liste_chaînée(object):

    def __init__(self):
        self.tete=None

    def ajouter_debut(self,element):
        self.tete=Chaînon(element,self.tete)

    def __str__(self):
        return str(self.tete)

    def est_vide(self):
        if self.tete is None:
            return True
        return False

    def ajouter_fin(self,element):
        C=Chaînon(element)
        if self.est_vide() :
            self.tete=C
        else:
            Cur=self.tete
            while Cur.suiv is not None :
                Cur=Cur.suiv
            Cur.suiv=C

    def supprimer_tete(self):
        if self.est_vide():
            raise IndexError("La liste est vide")
        self.tete=self.tete.suiv

    def supprimer_queue(self):
        if self.est_vide():
            raise IndexError("La liste est vide")
        Cur=self.tete
        a=None
        while Cur.suiv is not None:
            a=Cur
            Cur=Cur.suiv
        a.suiv=None
        

    def taille(self):
        if self.est_vide():
            return 0
        compt=1
        Cur=self.tete
        while Cur.suiv is not None:
            compt=compt+1
            Cur=Cur.suiv
        return compt

    def get_dernier_chaînon(self):
        if self.est_vide():
            return None
        else :
            Cur=self.tete
            while Cur.suiv is not None:
                Cur=Cur.suiv
        return Cur.val
        
    def get_chaînon_indice(self,i):
        if self.taille()<i+1:
            raise IndexError("La liste n'a pas d'élémént d'indice i")
        j=0
        Cur=self.tete
        while j<i:
            Cur=Cur.suiv
            j=j+1
        return Cur.val

    def inserer_indice(self,element,i):
        C=Chaînon(element)
        if self.taille()<i:
            raise IndexError("La liste n'a pas d'élémént d'indice i")
        if i==0:
            self.ajouter_debut(element)
        else:
            j=0
            Cur=self.tete
            while j<i-1:
                Cur=Cur.suiv
                j=j+1
            C.suiv=Cur.suiv
            Cur.suiv=C

    def supprimer_indice(self,i):
        if self.taille()<i+1:
            raise IndexError("La liste n'a pas d'élémént d'indice i")
        if i==0:
            self.tete=self.tete.suiv
        else:
            j=0
            Cur=self.tete
            while j<i-1:
                Cur=Cur.suiv
                j=j+1
            Cur.suiv=Cur.suiv.suiv

    def concatener(self,L):
        if self.est_vide():
            self.tete=L.tete
            return self
        if L.est_vide():
            return self
        Cur=self.tete
        while Cur.suiv is not None:
            Cur=Cur.suiv
        Cur.suiv=L.tete
        return self
            

LLL=Liste_chaînée()
LL=Liste_chaînée()
L=Liste_chaînée()

L.ajouter_debut(6)
L.ajouter_debut(5)
L.ajouter_debut(2)
L.ajouter_fin(9)

LL.ajouter_debut(3)
LL.ajouter_debut(7)
LL.ajouter_debut(10)
LL.ajouter_fin(23)
'''
print(str(L))
print(str(LL))
print(L.taille())
print(LL.taille())
print(L.est_vide())
print(LL.est_vide())
print(LLL.est_vide())
print(str(L.get_dernier_chaînon()))     
print(str(LL.get_dernier_chaînon()))
print(str(L.get_chaînon_indice(1)))
print(str(LL.concatener(L)))
L.inserer_indice(45,4)
print(str(L))
L.supprimer_indice(0)
print(str(L))
'''
print(str(L))
print(L.taille())
L.supprimer_queue()
print(str(L))
print(L.taille())
print(str(L.get_dernier_chaînon())) 
