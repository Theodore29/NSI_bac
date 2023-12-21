class Chainon(object):
    def __init__(self,v=None,s=None):
        self.val=v
        self.suivant=s
    def __str__(self):
        if self.val is None:
            return str(self.val)
        else:
            return '|--' + str(self.val)+'--| \n'+str(self.suivant)

class piles(object):
    def __init__(self):
        self.contenu=None
    def push(self,element):
        self.contenu=Chainon(element,self.contenu)
    def __str__(self):
        return str(self.contenu)
    def pop(self):
        if self.est_vide():
            raise IndexError('la liste est vide')
        a=self.contenu.val
        self.contenu=self.contenu.suivant
        return a
    def est_vide(self):
        if self.contenu is None:
            return True
        return False
    def sommet(self):
        if self.est_vide():
            raise IndexError('la liste est vide')
        a=self.contenu.val
        return a

    def taille(self):
        if self.est_vide():
            return 0
        compt=1
        Cur=self.contenu
        while Cur.suivant is not None:
            compt=compt+1
            Cur=Cur.suivant
        return compt


##liste=piles()
##liste.push(4)
##liste.push(5)
##liste.push(6)
##print(liste.est_vide())
##print(liste.sommet())
##print(liste.taille())
##print(liste.pop())
##print(liste)

class Chainon2(object):
    def __init__(self,v=None,s=None):
        self.val=v
        self.suivant=s
    def __str__(self):
        if self.val is None:
            return str(self.val)
        else:
            return str(self.val)+' ---> '+str(self.suivant)
class files(object):
    def __init__(self):
        self.contenu=None
    def add(self,element):
        self.contenu=Chainon2(element,self.contenu)
    def __str__(self):
        return str(self.contenu)
    def est_vide(self):
        if self.contenu is None:
            return True
    def take(self):
        if self.est_vide():
            raise IndexError("La liste est vide")
        Cur=self.contenu
        a=None
        while Cur.suivant is not None:
            a=Cur
            Cur=Cur.suivant
        a.suivant=None
    def taille(self):
        if self.est_vide():
            return 0
        compt=1
        Cur=self.contenu
        while Cur.suivant is not None:
            compt=compt+1
            Cur=Cur.suivant
        return compt

##liste_file=files()
##liste_file.add(4)
##liste_file.add(5)
##
##liste_file.take()
##print(liste_file)
##print(liste_file.taille())

class Pile(object):
    def __init__(self):
        self.contenu = []

    def push(self, element):
        self.contenu.insert(0,element)

    def __str__(self):
        return '\n'.join([f'|--{str(e)}--|' for e in self.contenu])

    def pop(self):
        if self.est_vide():
            raise IndexError('La pile est vide')
        return self.contenu.pop(0)

    def est_vide(self):
        return len(self.contenu) == 0

    def sommet(self):
        if self.est_vide():
            raise IndexError('La pile est vide')
        return self.contenu[0]

    def taille(self):
        return len(self.contenu)


##pile_liste = Pile()
##pile_liste.push(1)
##pile_liste.push(2)
##pile_liste.push(3)
##
##print(pile_liste)
##print(pile_liste.taille())
##pile_liste.pop()
##print(pile_liste.sommet())
##print(pile_liste)


class File(object):
    def __init__(self):
        self.contenu = []

    def add(self, element):
        self.contenu.insert(0,element)

    def __str__(self):
        return ''.join([f'{str(e)}--->' for e in self.contenu])+"None"

    def est_vide(self):
        return len(self.contenu) == 0

    def take(self):
        if self.est_vide():
            raise IndexError("La liste est vide")
        self.contenu.remove(self.contenu[-1])

    def taille(self):
        return len(self.contenu)


##liste_fi = File()
##liste_fi.add(1)
##liste_fi.add(2)
##liste_fi.add(3)
##
##print(liste_fi)
##print(liste_fi.taille())
##liste_fi.take()
##print(liste_fi)

class File_de_piles(object):
    def __init__(self):
        self.entrée=Pile()
        self.sortie=Pile()

    def __str__(self):
        entree_inserse=list(reversed(self.entrée.contenu))
        sortie_liste=list(self.sortie.contenu)
        contenu_str=', '.join(map(str,entree_inserse+sortie_liste))
        return f"File:[{contenu_str}]"

    def est_vide(self):
        return self.entrée.est_vide() and self.sortie.est_vide()

    def ajouter(self,element):
        self.entrée.push(element)

    def retirer(self):
        if self.sortie.est_vide() and self.entrée.est_vide():
            raise IndexError('La liste est vide')
        if not self.sortie.est_vide():
            return self.sortie.pop()
        if self.sortie.est_vide():
            while not self.entrée.est_vide():
                self.sortie.push(self.entrée.pop())
            return self.sortie.pop()

    def taille(self):
        return self.entrée.taille()+self.sortie.taille()

file_de_pile=File_de_piles()
file_de_pile.ajouter(1)
file_de_pile.ajouter(2)
file_de_pile.ajouter(3)

print(file_de_pile)
print(file_de_pile.taille())
print(file_de_pile.retirer())
print(file_de_pile)
print(file_de_pile.taille())