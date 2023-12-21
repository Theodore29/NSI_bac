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

Tab=[2,5,1,8,6,4,11,9,13]
Tab1=[13,21,4,9,11,1,25,15,3,18]

print(tri_insertion(Tab))
print(tri_insertion(Tab1))
