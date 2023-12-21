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

def trace(Lx,Li,Ls):
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
    pylab.show()


#pylab.ion()
trace(Taille_echantillon,Temps_insertion,Temps_selection)
#pylab.ioff()

