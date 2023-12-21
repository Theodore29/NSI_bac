from tkinter import *
 



Mafenetre = Tk()
Mafenetre.title('Jeu de Dame')
Mafenetre.geometry('650x715+20+20')
Largeur = 480
Hauteur = 480
couleur1 = "snow"

Canevas=Canvas(Mafenetre, width=Largeur, height=Hauteur, bg=couleur1 )

message=StringVar()
message.set("Quel pion voulez vous déplacer ?")
Label(Mafenetre, textvariable=message).pack(padx=1,pady=1)
nombre0=StringVar()
saisie0=Entry(Mafenetre)
saisie0.configure(textvariable=nombre0,width=2)
saisie0.pack()

message1=StringVar()
message1.set("Colonne : ")
Label(Mafenetre, textvariable=message1).pack(padx=1,pady=1)
nombre1=StringVar()
saisie1=Entry(Mafenetre)
saisie1.configure(textvariable=nombre1,width=2)
saisie1.pack()

message2=StringVar()
message2.set("Ligne : ")
Label(Mafenetre, textvariable=message2).pack(padx=1,pady=1)
nombre2=StringVar()
saisie2=Entry(Mafenetre)
saisie2.configure(textvariable=nombre2,width=2)
saisie2.pack()



def jouer():
    n0=int(nombre0.get())
    n1=int(nombre1.get())
    n2=int(nombre2.get())
    print(n0,"et",n1,"et",n2)
    #Liste.listedeplacer(n0,n1,n2)
    #Liste.listeprendre(n0,n1,n2)
    #Liste.changedame()
    initialisation()
    #Liste.affiche()
    #Liste.description()

def initialisation() :
    

    Canevas.create_rectangle(0, 0, Largeur, Hauteur, fill=couleur1)
    Canevas.create_line(Largeur/8, 0,Largeur/8, Hauteur, fill="black")
    Canevas.create_line(2*Largeur/8, 0,2*Largeur/8, Hauteur, fill="black")
    Canevas.create_line(3*Largeur/8, 0,3*Largeur/8, Hauteur, fill="black")
    Canevas.create_line(4*Largeur/8, 0,4*Largeur/8, Hauteur, fill="black")
    Canevas.create_line(5*Largeur/8, 0,5*Largeur/8, Hauteur, fill="black")
    Canevas.create_line(6*Largeur/8, 0,6*Largeur/8, Hauteur, fill="black")
    Canevas.create_line(7*Largeur/8, 0,7*Largeur/8, Hauteur, fill="black")

    Canevas.create_line(0,Largeur/8, Largeur, Largeur/8, fill="black")
    Canevas.create_line(0,2*Largeur/8,Largeur, 2*Largeur/8, fill="black")
    Canevas.create_line(0,3*Largeur/8,Largeur, 3*Largeur/8, fill="black")
    Canevas.create_line(0,4*Largeur/8,Largeur, 4*Largeur/8, fill="black")
    Canevas.create_line(0,5*Largeur/8,Largeur, 5*Largeur/8, fill="black")
    Canevas.create_line(0,6*Largeur/8,Largeur, 6*Largeur/8, fill="black")
    Canevas.create_line(0,7*Largeur/8,Largeur, 7*Largeur/8, fill="black")

    C=60
    Canevas.create_rectangle(0, 0, C, C ,fill="black")
    Canevas.create_rectangle(2*C, 0, C+2*C, C ,fill="black")
    Canevas.create_rectangle(4*C, 0, C+4*C, C ,fill="black")
    Canevas.create_rectangle(6*C, 0, C+6*C, C ,fill="black")


    Canevas.create_rectangle(0, 2*C, C, 2*C+C ,fill="black")
    Canevas.create_rectangle(2*C, 2*C, C+2*C, 2*C+C ,fill="black")
    Canevas.create_rectangle(4*C, 2*C, C+4*C, 2*C+C ,fill="black")
    Canevas.create_rectangle(6*C, 2*C, C+6*C, 2*C+C ,fill="black")

    Canevas.create_rectangle(0, 4*C, C, 4*C+C ,fill="black")
    Canevas.create_rectangle(2*C, 4*C, C+2*C, 4*C+C ,fill="black")
    Canevas.create_rectangle(4*C, 4*C, C+4*C, 4*C+C ,fill="black")
    Canevas.create_rectangle(6*C, 4*C, C+6*C, 4*C+C ,fill="black")

    Canevas.create_rectangle(0, 6*C, C, 6*C+C ,fill="black")
    Canevas.create_rectangle(2*C, 6*C, C+2*C, 6*C+C ,fill="black")
    Canevas.create_rectangle(4*C, 6*C, C+4*C, 6*C+C ,fill="black")
    Canevas.create_rectangle(6*C, 6*C, C+6*C, 6*C+C ,fill="black")

    Canevas.create_rectangle(C, C, 2*C, 2*C ,fill="black")
    Canevas.create_rectangle(2*C+C, C, C+3*C, C+C ,fill="black")
    Canevas.create_rectangle(4*C+C, C, C+5*C, C+C ,fill="black")
    Canevas.create_rectangle(6*C+C, C, C+7*C, C+C ,fill="black")

    Canevas.create_rectangle(C, 3*C, C+C, C+3*C ,fill="black")
    Canevas.create_rectangle(2*C+C, 3*C, C+3*C, C+3*C ,fill="black")
    Canevas.create_rectangle(4*C+C, 3*C, C+5*C, C+3*C ,fill="black")
    Canevas.create_rectangle(6*C+C, 3*C, C+7*C, C+3*C ,fill="black")

    Canevas.create_rectangle(C, 5*C, C+C, C+5*C ,fill="black")
    Canevas.create_rectangle(2*C+C, 5*C, C+3*C, C+5*C ,fill="black")
    Canevas.create_rectangle(4*C+C, 5*C, C+5*C, C+5*C ,fill="black")
    Canevas.create_rectangle(6*C+C, 5*C, C+7*C, C+5*C ,fill="black")

    Canevas.create_rectangle(C, 7*C, C+C, C+7*C ,fill="black")
    Canevas.create_rectangle(2*C+C, 7*C, C+3*C, C+7*C ,fill="black")
    Canevas.create_rectangle(4*C+C, 7*C, C+5*C, C+7*C ,fill="black")
    Canevas.create_rectangle(6*C+C, 7*C, C+7*C, C+7*C ,fill="black")






initialisation()



#Liste.description()
#Liste.affiche()



BoutonJouer=Button(Mafenetre, text='Jouer', fg ='red', command=jouer)
BoutonJouer.pack(padx=10, pady=10)


BoutonQuitter=Button(Mafenetre, text='Quitter', fg = 'red' ,command = Mafenetre.destroy)
Canevas.pack(padx=10, pady=10) ;


BoutonQuitter.pack(side=RIGHT, padx=10, pady=10)
Mafenetre . mainloop ( )


