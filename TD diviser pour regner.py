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



##print(tri_insertion(['4','9','2','8','14']))

##print(tri_selection(['4','9','2','8','14']))




def fusion(t1,t2):
    resultat=[]
    i1=0
    i2=0
    while i1 < len(t1) and i2 < len(t2):
        if t1[i1] <= t2[i2]:
            resultat.append(t1[i1])
            i1+=1
        else :
            resultat.append(t2[i2])
            i2 += 1
    if t1 != []:
        resultat.extend(t1[i1:])
    if t2 != []:
        resultat.extend(t2[i2:])

    return resultat

def tri_fusion(t):
    if len(t)<=1:
        return t
    m = len(t)//2
    t1=t[:m]
    t2=t[m:]
    t1=tri_fusion(t1)
    t2=tri_fusion(t2)
    return fusion(t1,t2)



##print(tri_fusion(['4','9','2','8','14']))

def tab_aleatoire(n,a,b):
    T=[a+randint(0,b-a) for i in range(n)]
    return T


def ex1():
    temps_fusion=[]
    for i in range(10,16):
        li=tab_aleatoire(2**i,-100000,100000)
        debut=time.time()
        T=tri_fusion(li)
        fin=time.time()
        temps_fusion.append(fin-debut)
    return temps_fusion




taille=tab_aleatoire(2**10,-100000,100000)


def ex3(Lx,Ly):

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
    pylab.show()

##print(ex1())
##ex3(longeur,ex2())




def ex4(Lx,Ly,temps_fusion, temps_insertion):
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
    pylab.plot(Lx,temps_fusion, 'b')
    pylab.plot(Lx,temps_insertion, 'g')

    pylab.show()

##ex4(longeur,ex1(),tri3(),tri4())



##Exercice 2 dichotomie:

def ex2_1(n,c,d):
    T=[randint(c,d) for i in range(n)]
    return T



def ex2_2(tableau):
    return tri_fusion(tableau)

t_ex=[3,100,23,80,14,69,5,100,40,60,67,24,95,43,84,34,51,92,65,83,3,9,100,85,86,19,77,3,62,16]

t_1=t_ex.sort()
liste_triee=tri_fusion(t_ex)

def recherche_dichotomique(t,x): ## recherche dichotomique
    deb = 0
    fin = len(t)
    while deb < fin-1:
        mil = (deb + fin) // 2
        if x < t[mil]:
            fin = mil
        else :
            deb = mil
    if x == t[deb]:
        return True
    else :
        return False




def recherche_naive(T,element):
    for i in range(len(T)):
        if T[i] == element :
            return True
    return False

def ex2_4(n,c,d,element):
    T=ex2_1(n,c,d)
    x=time.time()
    recherche_dichotomique(T,element)
    y=time.time()
    tps_dico= y-x
    print("le temps d'execution de la recherche dichotomique est de : " + str(tps_dico))

    x1=time.time()
    recherche_naive(T,element)
    y1=time.time()
    tps_naive= y1-x1
    print("le temps d'execution de la recherche naive est de : "+ str(tps_naive))

    return tps_dico,tps_naive






