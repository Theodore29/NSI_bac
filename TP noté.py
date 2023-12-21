test=[1,3,4,2,4,6,3,0]
x=["1","2","3","4"]

def recherche_indices_classement(elt, tab):
    l1=[]
    for j in range(len(tab)):
       if tab[j] < elt:
        l1.append(j)



    l2=[]
    for j in range(len(tab)):
       if tab[j]==elt:
        l2.append(j)


    l3=[]
    for j in range(len(tab)):
       if tab[j] > elt:
        l3.append(j)

    return l1,l2,l3




res = {'Dupont': {
        'DS1': [15.5,4],
        'DM1': [14.5,4],
        'DS2': [15.5,4],
        'PROJET1': [15.5,4],
        'DS3': [15.5,4],
        },

    }

def moyenne(nom, dico_result):
    if nom in dico_result:
        notes= dico_result[nom]
        total_points=0
        total_coefficients=0
        for valeurs in notes.values():
            note,coefficient = valeurs
            total_points= total_points + note*coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1)
    else :
        return -1
