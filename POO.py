class Temps(object):

    def __init__(self,h,m,s):
        if h<0:
            raise ValueError(h,"doit etre positif")
        if m<0 or m>=60:
            raise ValueError(m,"doit etre compris entre 0 et 60 exclus")
        if s<0 or s>=60:
            raise ValueError(s,"doit etre compris entre 0 et 60 exclus")

        self.heures=h
        self.minutes=m
        self.secondes=s


    def afficher(self):
        print(self.heures,'h',self.minutes,'m',self.secondes,'s')
        return str(self.heures)+'h'+str(self.minutes)+'m'+str(self.secondes)+'s'

    def ajouter(self,t2):
        t=Temps(0,0,0)
        s=self.secondes+t2.secondes
        if s<60:
            t.secondes=s
        else:
            t.secondes=s%60
        m=self.minutes+t2.minutes+s//60
        if m<60:
            t.minutes=m
        else :
            t.minutes=m%60
        t.heures=self.heures+t2.heures+m//60
        return t



    def egal(self, t1):
        return self.secondes == t1.secondes and self.minutes == t1.minutes and self.heures == t1.heures

    def maxi(self, t1):
        if self.egal(t1):
            return 'elle sont égale'
        else :
            if self.heures > t1.heures :
                return self
            elif t1.heures > self.heures :
                return t1
            elif self.minutes > t1.minutes:
                return self
            elif t1.minutes > self.minutes:
                return t1
            elif self.secondes > t1.seconde:
                return self
            elif t1.secondes > self.secondes:
                return t1




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




t1=Temps(5,7,11)
t2=Temps(3,40,38)
t3=t2.ajouter(t1)
t3.afficher()
t1.maxi(t2).afficher()


