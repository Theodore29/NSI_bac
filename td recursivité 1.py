from sys import *

setrecursionlimit(4000)

def nième_nombre_pair(n):
    if n==0:
        return 0
    return nième_nombre_pair(n-1)+2



def mystere(l):
    if len(l) == l:
        return[0]
    else :
        return mystere(l[1:]) +l[0]



def multiple_de_treize(n):
    if n == 0:
        return True

    elif n < 0 :
        return False
    else :
        return multiple_de_treize(n-13)


def somme_recursive(n):
    if n == 0:
        return False

    else :
        return somme_recursive(n-1)+n


def fibo_recursif(n):
    if n == 1 or n==2:
        return 1

    return fibo_recursif(n-1)+fibo_recursif(n-2)


def multiplication_russe(x,y):
    p=0
    while x>0:
        if x%2 == 1:
            p=p+y
        x=x//2
        y=y+y
    return p


def multiplicaton_russe_recursive(x,y):
    if x== 0:
        return 0

    if x>0:
        if x%2==1:
            return multiplicaton_russe_recursive(x//2.2*y)+y

        return multiplicaton_russe_recursive(x//2,y*2)



def coef_bin(n,p):
    if p==0 or n==p:
        return 1

    return coef_bin(n-1,p) + coef_bin(n-1,p-1)





for n in range(0,10):
    l=[]
    for p in range(0,n+1):
        l.append(coef_bin(n,p))

    print(l)





