from tkinter import*
class Balle(object):
    def __init__(self,canvas,color,Pos_X,Pos_Y):
        self.canvas=canvas
        self.pos=[Pos_X,Pos_Y,Pos_X+20,Pos_Y+20]
        self.objid=canvas.create_oval(self.pos,fill=color)
        self.dx=0
        self.dy=5
        self.bouge()

    def bouge(self):
        self.pos=self.canvas.coords(self.objid)
        if self.pos[3]>=……….:
            Self………….=-5
        ………………………………………………………………
        ………………………………………………………………
        self.canvas.move(self.objid,self.dx,self.dy)
        self.canvas.after(20,self.bouge)

tk=Tk()
tk.title("Jeu")
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()

Bouton_Quitter=Button(tk,text='Quitter',command=tk.destroy)
Bouton_Quitter.pack()
balle1=Balle(canvas,'red',0,10)

tk.mainloop()