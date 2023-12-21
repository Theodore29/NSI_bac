class Outil(object):
    def __init__(self,code_barre=-1,categorie="",marque="",ref="",prix=0,qte=0):

        self._code_barre = code_barre
        self._categorie = categorie
        self._marque = marque
        self._ref = ref
        self._prix = prix
        self._qte = qte

    def _get_code_barre(self):
        return self._code_barre

    def _set_code_barre(self,code_barre):
        self._code_barre = code_barre



    def _get_categorie(self):
        return self._categorie

    def _set_categorie(self,categorie):
        self._categorie = categorie



    def _get_marque(self):
        return self._marque

    def _set_marque(self,marque):
        self._marque = marque



    def _get_ref(self):
        return self._ref

    def _set_ref(self,ref):
        self._ref = ref


    def _get_prix(self):
        return self._ref

    def _set_prix(self,prix):
        self._prix = prix


    def _get_qte(self):
        return self._qte

    def _set_qte(self,qte):
        self._qte = qte


    code_barre = property(_get_code_barre,_set_code_barre)
    categorie = property(_get_categorie,_set_categorie)
    marque = property(_get_marque,_set_marque)
    ref = property(_get_ref,_set_ref)
    prix = property(_get_prix,_set_prix)
    qte = property(_get_qte,_set_qte)



    def saisie(self):
        self.code_barre=int(input("entrez un code barre "))
        self.categorie=input("entrez une catégorie d'objet")
        self.marque = input("entrez une marque")
        self.ref = input("entrez une référence")
        self.prix=int(input("entrez un prix"))
        self.qte = int(input("entrez une quantité"))


    def affiche(self):
        print("l'objet a comme attributs : ", self.code_barre, self.categorie, self.marque, self.ref, self.prix, self.qte)


    def Entrer_stock(self):
        self.qte += 1

    def Sortir_stock(self):
        self.qte += -1


outils = Outil()




class ListeOutils(object):
    def __init__(self):
        self._liste=[]
    def ajout_outils(self, Pion):
        self._liste.append(Pion)

    def Affiche(self):
        s="La liste des outils est : "
        print(s)

        for outils in self._liste :
            outils.affiche()

    def Supprime_outil(self,p):
        self._liste.remove(p)

    def Vente_outil(self,code):
        for outil in self._liste:
            if outil.code_barre==code :
                outil.Sortir_stock()

outils_li = ListeOutils()

outils1=Outil(123456789," perceuse", "makita", "54FDE28", 159, 20)
outils2=Outil(987654321,"rabot", "bosch", "88SA255", 99, 15)
outils3=Outil(78456123,"ponceuse", "metabo", "899HJU4", 199, 12)
outils2.affiche()
outils_li.ajout_outils(outils1)
outils_li.ajout_outils(outils2)
outils_li.ajout_outils(outils3)
outils_li.Affiche()

##outils_li.Supprime_outil(outils2)
##outils_li.Affiche()

outils_li.Vente_outil(123456789)
outils_li.Affiche()
