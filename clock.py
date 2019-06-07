from IPython.display import clear_output
import time
import winsound

class Clock():
    
    def __init__(self,hrs,mi,sec):
        self.hrs=hrs
        self.mi=mi
        self.sec=sec
     
        
    def clock(self,seco=10):
        x=0
        while True:
            print("%s:%s:%s"%(self.hrs,self.mi,self.sec))
            self.sec+=1
            if self.sec>=60:
                self.sec=0
                self.mi+=1
            if self.mi>=60:
                self.mi=0
                self.hrs+=1
            if self.hrs>=24:
                self.hrs=0
                self.mi=0
                self.sec=0
            time.sleep(1)
            clear_output()
            if x==seco:
                break
            else:
                x=x+1
                time.sleep(1)
                
            
            
    def show_time(self):
        print("%s:%s:%s"%(self.hrs,self.mi,self.sec))
        
        
    def alaram(self,x,repeat):
        for i in range(0,repeat):
            time.sleep(x)
            winsound.Beep(1000,1000)
        
        
def main():
    
    
    print(" Enter Time ")
    x=int(input("Hours   : "))
    y=int(input("Minutes : "))
    z=int(input("Seconds : "))
    c=Clock(x,y,z)
    c.clock(1)
    while True:
        print("Press 1 for Running Clock")
        print("Press 2 to set an Alaram")
        print("Press 3 for time only")
        x1=int(input("Enter Your Choice"))
        if x1==1:
            clear_output()
            s=int(input("Enter time in second for running clock: "))
            c.clock(s)
        elif x1==2:
            clear_output()
            print("Enter Time")
            x2=int(input("Hours   : "))
            y2=int(input("Minutes : "))
            z2=int(input("Seconds : "))
            x3=x2*60*60
            y3=y2*60
            z3=x3+y3+z2
            repeat=int(input("Enter times of repestition: "))
            c.alaram(z3,repeat)
        elif x1==3:
            c.show_time()
        else:
            print("Wrong Input!!!!!")
            
        g=input("Want to do more y/n: ")
        if g=='y':
            clear_output()
            continue
        elif g=='n':
            break    
            
main()