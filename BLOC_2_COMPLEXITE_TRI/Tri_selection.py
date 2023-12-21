def tri_selection(T):
    for i in range(len(T)-1):
        minimum=i
        for j in range(i+1,len(T)):
            if T[j]<T[minimum]:
                minimum=j
        if minimum!=i:
            T[i],T[minimum]=T[minimum],T[i]
    return T

Tab=[2,8,4,6,9,7,11,5,24,16]
Tab1=[13,21,4,9,11,1,25,15,3,18]
print(tri_selection(Tab))
print(tri_selection(Tab1))
