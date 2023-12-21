import time
from random import*
from math import*
import pylab

def inserer(T,element,termine):
    i=termine
    while i>=0 and T[i]>element:
        T[i+1]=T[i]
        i=i-1
    T[i+1]=element
    return T

def tri_insertion(T):
    for i in range(1,len(T)):
        element=T[i]
        termine=i-1
        T=inserer(T,element,termine)
    return T

def tri_selection(T):
    for i in range(len(T)-1):
        minimum=i
        for j in range(i+1,len(T)):
            if T[j]<T[minimum]:
                minimum=j
        if minimum!=i:
            T[i],T[minimum]=T[minimum],T[i]
    return T

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
    return list(fusion(Tabg, Tabd))

def tri_bulle(L):
    n=len(L)
    for i in range (n-1):
        for j in range (n-i-1):
            if L[j]>L[j+1] :
                temp=L[j+1]
                L[j+1]=L[j]
                L[j]=temp
    return L

def tab_aleatoire(n,a,b):
    T=[a+randint(0,b-a) for i in range(n)]
    return T

#print(tab_aleatoire(10,-2,40))

Taille_echantillon=[]
Temps_insertion=[]
for i in range(10,16):
    n=2**i
    Taille_echantillon.append(n)
    T=tab_aleatoire(n,-100000,100000)
    t1=time.time()
    T=tri_insertion(T)
    t2=time.time()
    Temps_insertion.append(t2-t1)
print(Temps_insertion)


Temps_selection=[]
for i in range(10,16):
    n=2**i
    T=tab_aleatoire(n,-100000,100000)
    t1=time.time()
    T=tri_selection(T)
    t2=time.time()
    Temps_selection.append(t2-t1)
print(Temps_selection)


Temps_bulle=[]
for i in range(10,16):
    n=2**i
    T=tab_aleatoire(n,-100000,100000)
    t1=time.time()
    T=tri_bulle(T)
    t2=time.time()
    Temps_bulle.append(t2-t1)
print(Temps_bulle)

Temps_fusion=[]
for i in range(10,16):
    n=2**i
    T=tab_aleatoire(n,-100000,100000)
    t1=time.time()
    T=tri_fusion(T)
    t2=time.time()
    Temps_fusion.append(t2-t1)
print(Temps_fusion)


def trace(Lx,Li,Ls,Lb,Lf):
    pylab.clf()
    titre="Temps de tri en fonction de la taille de l'échantillon"
    pylab.title(titre)
    pylab.xlabel("Taille echantillon")
    pylab.ylabel("temps du tri")
    pylab.axis([-5,35000,-5,80])
    pylab.axhline(color='black')
    pylab.axvline(color='black')
    pylab.grid()
    pylab.plot(Lx,Li,'r')
    pylab.plot(Lx,Ls,'b')
    pylab.plot(Lx,Lb,'y')
    pylab.plot(Lx,Lf,'g')
    pylab.show()


#pylab.ion()
trace(Taille_echantillon,Temps_insertion,Temps_selection,Temps_bulle,Temps_fusion)
#pylab.ioff()


