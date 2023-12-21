from random import*
import pylab
import time

def fusion(Tabg,Tabd):
    resultat = []
    index_g= 0
    index_d = 0
    while index_g < len(Tabg) and index_d < len(Tabd):
        if Tabg[index_g] <= Tabd[index_d]:
            resultat.append(Tabg[index_g])
            index_g += 1
        else:
            resultat.append(Tabd[index_d])
            index_d += 1
    if Tabg !=[]:
        resultat.extend(Tabg[index_g:])
    if Tabd !=[]:
        resultat.extend(Tabd[index_d:])
    return resultat

def tri_fusion(Tab):
    if len(Tab) <= 1:
        return Tab
    milieu = len(Tab) // 2
    Tabg = Tab[:milieu]
    Tabd = Tab[milieu:]
    Tabg = tri_fusion(Tabg)
    Tabd = tri_fusion(Tabd)
    return fusion(Tabg, Tabd)


def tab_aleatoire(n,a,b):
    T=[a+randint(0,b-a) for i in range(n)]
    return T

def dichotomie(T,element):
    if len(T)==0:
        raise ValueError("Le tableau est vide")
    index_min=0
    index_max=len(T)-1
    while index_min<=index_max:
        milieu=(index_min+index_max)//2
        if element==T[milieu]:
            return True
        else:
            if element>T[milieu]:
                index_min=milieu+1
            else:
                index_max=milieu-1
    return False

def recherche_naïve(T,element):
    for i in range(len(T)):
        if T[i]==element:
            return True
    return False




T=tab_aleatoire(30,0,100)
T=tri_fusion(T)
print(T)
element=int(input("Quel est l'élément cherché ? "))
print(dichotomie(T,element))
print(recherche_naïve(T,element))

Taille_echantillon=[]
Temps_dichotomie=[]
Temps_recherche_naïve=[]
for i in range(15,21):
    n=2**i
    Taille_echantillon.append(n)
    T=tab_aleatoire(n,-10000000,10000000)
    element=T[n-8]
    t1=time.time()
    p=dichotomie(T,element)
    t2=time.time()
    Temps_dichotomie.append(t2-t1)
    t1=time.time()
    p=recherche_naïve(T,element)
    t2=time.time()
    Temps_recherche_naïve.append(t2-t1)
print(Temps_dichotomie)
print(Temps_recherche_naïve)

def trace(Lx,Li,Ls):
    pylab.clf()
    titre="Temps de tri en fonction de la taille de l'échantillon"
    pylab.title(titre)
    pylab.xlabel("Taille echantillon")
    pylab.ylabel("temps de recherche")
    pylab.axis([29000,1100000,0.00001,0.1])
    pylab.axhline(color='black')
    pylab.axvline(color='black')
    pylab.grid()
    pylab.plot(Lx,Li,'r')
    pylab.plot(Lx,Ls,'b')
    pylab.show()


##pylab.ion()
trace(Taille_echantillon,Temps_dichotomie,Temps_recherche_naïve)
##pylab.ioff()
