class Temps(object):

    def __init__(self,h,m,s):
        if h<0:
            raise ValueError(h,"doit être positif")
        if m<0 or m>=60:
            raise ValueError(m,"doit être compris entre 0 et 60 exclus")
        if s<0 or s>=60:
            raise ValueError(s,"doit être compris entre 0 et 60 exclus")
        self.heures=h
        self.minutes=m
        self.secondes=s


    def afficher(self):
        print(self.heures,'h',self.minutes,'m',self.secondes,'s')

    def ajouter(self,t2):
        t=Temps(0,0,0)
        s=self.secondes+t2.secondes
        if s<60 :
            t.secondes=s
        else:
            t.secondes=s%60
        m=self.minutes+t2.minutes+s//60
        if m<60:
            t.minutes=m
        else:
            t.minutes=m%60
        t.heures=self.heures+t2.heures+m//60
        return t

    def egal(self,t2):
        return self.heures==t2.heures and self.minutes==t2.minutes and self.secondes==t2.secondes

    def maxi(self,t2):
        if self.heures>t2.heures:
            return self
        elif self.heures<t2.heures:
            return t2
        elif self.minutes>t2.minutes:
            return self
        elif self.minutes<t2.minutes:
            return t2
        elif self.secondes>t2.secondes:
            return self
        elif self.secondes<t2.secondes:
            return t2
        else :
            return self

    def soustraire(self,t2):
        t=Temps(0,0,0)
        r=0
        rr=0
        if self.egal(t2)==True:
            return t
        tt=self.maxi(t2)
        if t2.egal(tt)==True:
            raise ValueError(t2,"ne peut pas être soustrait")
        else :
            if self.secondes>t2.secondes:
                t.secondes=self.secondes-t2.secondes
            else :
                r=-1
                t.secondes=60+self.secondes-t2.secondes
            if self.minutes+r>t2.minutes:
                t.minutes=self.minutes+r-t2.minutes
            else :
                rr=-1
                t.minutes=60+self.minutes+r-t2.minutes
            t.heures=self.heures+rr-t2.heures
            return t
            
            

#tt=Temps(-5,52,4)



t2=Temps(8,42,55)
print(t2)
t1=Temps(12,30,10)
t3=t2.ajouter(t1)
t4=Temps(12,30,10)
t3.afficher()
f=t1.maxi(t4)
f.afficher()
t5=t3.soustraire(t1)
t5.afficher()

