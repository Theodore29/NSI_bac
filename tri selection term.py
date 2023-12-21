from random import randint
import time
import pylab

a=20
b=100

T=[a + randint(0,b-a) for i in range(10)]




n=2**10
c=-100000
d=100000
def aleatoire(n,c,d):
    T=[randint(c,d)for i in range(n)]
    return T


##Fonction par tri par selection
def inserer(T,element,termine):
    i=termine
    while i>=0 and element < T[i]:
        T[i+1] = T[i]
        i=i-1
    T[i+1] = element
    return T

##Fonction par tri par selection
def tri_insertion(T):
    for i in range(1,len(T)):
        element=T[i]
        termine=i-1
        T=inserer(T, element, termine)

    return T

##Fonction du tri par selection

def tri_selection(T):
    for i in range(len(T)-1):
        minimun=i

        for j in range(i+1, len(T)):
            if T[j]<T[minimun]:
                minimun=j

    if minimun !=i:
        T[i],T[minimun]= T[minimun],T[i]

    return T

##Fonction qui mesure le temps de tri d'une liste de 2^10 chosiis aléatoirement entre -100000 et 100000
p=aleatoire(n,c,d)
def tri2(T):
    x=time.time()
    t=tri_insertion(T)
    y=time.time()
    tps= y-x
    print("le temps d'excution est : " , (y-x))
    return tps

##Fonction par tri par insertion, avec calcul du temps
def tri3():
    temps_insertion=[]
    for i in range(10,16):
        li=aleatoire(2**i, c,d)
        debut=time.time()
        T=tri_insertion(li)
        fin=time.time()
        temps_insertion.append(fin-debut)
    return temps_insertion

##Fonction par tri par selection, avec  calcul du temps
def tri4():
    temps_selection=[]
    for i in range(10,16):
        li=aleatoire(2**i, c,d)
        debut=time.time()
        T=tri_selection(li)
        fin=time.time()
        temps_selection.append(fin-debut)
    return temps_selection


longeur=[2**10,2**11,2**12,2**13,2**14,2**15]

def trace(Lx, Ly, Lp):

    pylab.clf()

    titre="Temps de tri en fonction de la taille de l'échantillon"
    pylab.title(titre)

    pylab.xlabel("Taille échantillon")
    pylab.ylabel("temps de tri")

    pylab.axis([-5,35000, -5,80])
    pylab.axhline(color='black')
    pylab.axvline(color='black')

    pylab.grid()

    pylab.plot(Lx,Ly, 'r')
    pylab.plot(Lx,Lp, 'b')
    pylab.show()




print(tri_insertion(['4','9','2','8','14']))

print(tri_selection(['4','9','2','8','14']))