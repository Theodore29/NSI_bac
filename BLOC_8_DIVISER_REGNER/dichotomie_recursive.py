from random import*


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

def dichotomie_recursive(T,element):
    if len(T)<1:
        return False
    index_min=0
    index_max=len(T)-1
    milieu=(index_min+index_max)//2
    print(T[milieu])
    if element==T[milieu]:
            return True
    else:
        if element>T[milieu]:
            T=T[milieu+1:]
            return dichotomie_recursive(T,element)
            
        else:
            T=T[:milieu]
            return dichotomie_recursive(T,element)
    

                



T=tab_aleatoire(30,0,100)
T=tri_fusion(T)
print(T)
element=int(input("Quel est l'élément cherché ? "))
print(dichotomie_recursive(T,element))
print(dichotomie(T,element))
