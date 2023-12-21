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

T1=[1,1,4,5,6,6,7]
T2=[1,2,3,6,8,9,10]
print(fusion(T1,T2))

T=tab_aleatoire(20,-100,100)
print(T)
T=tri_fusion(T)
print(T)
