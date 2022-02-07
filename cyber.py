from decimal import *
class Sausage:
    def __init__(self,word="pork!",sz="1"):
        self.sz=int(eval(str(sz))*12)
        self.strsz=str(sz)
        self.exi=1
        if eval(str(sz))<=0:
            self.exi=0
            self.sz=0
            self.strsz='0'
        else:
            if eval(str(sz))<=1/12:
                self.sz=0
        self.up='/'
        self.body='|'
        self.word=word
        for i in range(self.sz):
            if i%12==0 and i!=0:
                self.up=self.up+'\\/'
                self.body=self.body+'||'
            self.up=self.up+'-'
            self.body=self.body+self.word[((i%12)%len(self.word))]
        if self.sz%12!=0: self.up=self.up+'|'
        else:
            if self.sz!=0: self.up=self.up+'\\'
            else:
                self.up=self.up+'|'
        self.body=self.body+'|'        
        self.down=''
        for i in range(len(self.up)): 
            if self.up[i]=='/': self.down=self.down+'\\'
            else:
                if self.up[i]=='\\': self.down=self.down+'/'
                else:
                    if self.up[i]=='|': self.down=self.down+'|'
                    else:
                        self.down=self.down+'-'        
                        

                              
        

    def __bool__(self):
        if self.exi==0: return False
        if self.exi==1: return True

    def __str__(self):
        return self.up+'\n'+(self.body+'\n')*3+self.down  

    def __radd__(self,other):
        return Sausage(self.word,str(self.strsz)+'+'+str(other.strsz))
    def __add__(self,other):
        return Sausage(self.word,str(self.strsz)+'+'+str(other.strsz)) 
    def __rsub__(self,other):  
        return Sausage(self.word,str(self.strsz)+'-'+str(other.strsz)) 
    def __sub__(self,other):  
        return Sausage(self.word,str(self.strsz)+'-'+str(other.strsz))       
    def __mul__(self,value):
        return Sausage(self.word,str(self.strsz)+'*'+str(value))
    def __rmul__(self,value):
        return Sausage(self.word,str(self.strsz)+'*'+str(value))
    def __truediv__(self,value:int):
        return Sausage(self.word,str(self.strsz)+'/'+str(value))        
    def __abs__(self):
        ans=list((eval('('+self.strsz+')*12')).as_integer_ratio())
        ans[1]=ans[1]*12
        if ans[0]==0: return '0'
        if ans[0]>ans[1]:
            k=ans[0]
        else:
            k=ans[1]
        while k!=1:
            if ans[0]%k==0 and ans[1]%k==0:
                return str(ans[0]//k)+'/'+str(ans[1]//k) 
            else:
                k=k-1
        return str(ans[0])+'/'+str(ans[1])
