# C-Graphics-To-python-convertor
It converts a C graphics code to its equivalent python graphics code in pygame.
import pygame
from math import pi
from tkinter import *
from time import *
import time

master = Tk()   #It opens a tkinter window 
w=Canvas(master,width=1000,height=500)

y=""
textBox=Text(master, height=40, width=100)
textBox.grid(row=1)      
def new():      #to write a new C++ code to convert
    l=Label(master,text="new file")
    l.grid(row=0)
    
def open2():   #to open an already existing .cpp file
    root=Toplevel(master)
    
    def o1():   #to open the open box to write the address of existing C++ file
        k=entry.get()
        l=Label(master,text=k)
        l.grid(row=0)
        print(k)
        ob=open(k,'r')
        
        p=ob.read()
        ob.close()
        
        textBox.insert(INSERT,p)
        root.destroy()
    
    label=Label(root,text="Enter the full address of .cpp file",height=3)
    label.grid(row=0)
    entry=Entry(root)
    entry.grid(row=1,column=0)
    button=Button(root,text="open",command = o1)
    button.grid(row=1,column=1)
    l=Label(root)
    l.grid(row=2)


def abc():     #the convertor function it will read the C graphics code character by character and convert it to python code 
        x=""
        lines=0
        words=0
        characters = 0
        y=textBox.get("1.0","end-1c")
        textBox.grid(row=2,column=0)
        obj=open('Test3.txt','w')
        obj.write(y)
        obj.close()
        
        obj=open('Test3.txt','r')
        x=obj.read()
           
        obj.close()
        characters=len(x)         
        pygame.init()
        time.sleep(2)
        abc = [639,470]
        screen = pygame.display.set_mode(abc)
                  
        WHITE = (255,255,255) 

        BLACK = (0,0,0)
        t=0

        l=""
        m=""
        n=""
        o=""
        p=""
        q=""

        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        tt=0

        ctr = 0

        screen.fill(BLACK)

        file = open('Source Code.txt','w')
        file.write("import pygame\n")
        file.write("import time\n")
        file.write("from math import pi\n\n")
        file.write("time.sleep(2)\n\n")
        file.write("abc = [639,470]\nscreen = pygame.display.set_mode(abc)\n\n")
        file.write("WHITE = (255,255,255) \nBLACK = (0,0,0)\n\n")

        def run(str1):      #to find whether the input in graphics function by user contains an interger or not
            regex=re.compile('[~`!@#$%^&*()_+=|\}{:;><,?/abcdefghijklmnopqrstuvwxyz]')
            if(regex.search(str1)==None): 
                return float(str1)
            else : 
                print("Error code c: Character entered, int or float required")
                return '*'
                ctr=1
        
        def run2(str2):     #to find whether the input in graphics function by user contains an interger or not
            regex=re.compile('[~`!@#$%^&*()_+=|\}{:;><,?/abcdefghijklmnopqrstuvwxyz.]')
            if(regex.search(str2)==None): 
                return int(str2)
            else : 
                print("Error code c: Character or float entered, int required")
                return '*'
                ctr=1
        
  
        for i in range (0,characters+1):
           if(x[i:i+8]=="drawpoly"):
               t=i+9

               while x[t] != ",":
                   o=o+x[t]
                   t=t+1
               t=t+1
               pp=0
               while x[t] !=")":
                   p=p+x[t]
                   t=t+1
                   pp=pp+1
               a=run2(o)
               if(a=='*'): continue
               if(p[0]>='0' and p[0]<='9'): 
                   print("Variable name not possible")
           
               lst=[0]*(2*(a))
       
               q="int "+p+ "[]={"
               l="int "+p+ "[] ={"
               m="int "+p+ "[] = {"
               n="int "+p+ "[]= {"
       
               for ptr in range (0,characters):
                   if(x[ptr:ptr+pp+8]==q): 
                        tt=ptr+pp+8
                        l=""
                        ii=0
                        for ii in range (0,(2*a)):
                          while x[tt] !=",":
                            if(x[tt]=="}"): break
                            l=l+x[tt]
                            tt=tt+1
                             
                          lst[ii]=run(l)
                          if(lst[ii]=='*'): 
                              lst[ii]=0
                              break
                          tt=tt+1   
                          l=""  
        
                        ii=ii+1
                        tt=0
                        ppt=0
                        jjj= a - 3
                        while(ppt<=(a+jjj)):
                            pygame.draw.line(screen,WHITE,[lst[ppt],lst[ppt+1]],[lst[(ppt)+2],lst[(ppt)+3]],2)
                            file.write("pygame.draw.line(screen,WHITE,["
                                       +str(lst[ppt])+","+str(lst[ppt+1])+"],["
                                       +str(lst[ppt+2])+","+str(lst[ppt+3])+"],2)\n"
                                       )
                            ppt=ppt+2

                   elif(x[ptr:ptr+pp+9]==l or x[ptr:ptr+pp+9]==n):
                        tt=ptr+pp+9
                        l=""
                
                        for ii in range (0,(2*a)):
                          while x[tt] !=",":
                            if(x[tt]=="}"): break
                            l=l+x[tt]
                            tt=tt+1
                                
                          tt=tt+1   
                          lst[ii]=float(l)
                          l=""  
                          print(lst[ii]," ")
                        ii=ii+1
                        tt=0
                        pp=0
                        while(pp<=(a+1)):
                            pygame.draw.line(screen,WHITE,[lst[pp],lst[pp+1]],[lst[(pp)+2],lst[(pp)+3]],2)
                            file.write("pygame.draw.line(screen,WHITE,["+str(lst[ppt])+","+str(lst[ppt+1])+"],["+str(lst[ppt+2])+","+str(lst[ppt+3])+"],2\n")
                            pp=pp+2
                            

                   elif(x[ptr:ptr+pp+10]==m):
                        tt=ptr+pp+10
                        l=""
                
                        for ii in range (0,(2*a)):
                          while x[tt] !=",":
                            if(x[tt]=="}"): break
                            l=l+x[tt]
                            tt=tt+1
                                
                          tt=tt+1   
                          lst[ii]=float(l)
                          l=""  
                          print(lst[ii]," ")
                        ii=ii+1
                        tt=0
                        ppt=0
                        while(ppt<=(a+1)):
                            pygame.draw.line(screen,WHITE,[lst[ppt],lst[ppt+1]],[lst[(ppt)+2],lst[(ppt)+3]],2)
                            file.write("pygame.draw.line(screen,WHITE,["
                                       +str(lst[ppt])+","+str(lst[ppt+1])+"],["
                                       +str(lst[ppt+2])+","+str(lst[ppt+3])+"],2\n"
                                       )
                            ppt=ppt+2
                            
                            #else:
                   #    print("You have not defined the coordinate variable")
                   #    break
           
               l=""
               m=""
               n=""
               o=""
               p=""
               q=""

               a=0
               b=0
               c=0
               d=0
               e=0
               f=0

           elif(x[i:i+4] == "line"): 
               t=i+5
               while x[t] !=",":
                  l=l+x[t]
                  t=t+1
               t=t+1
               while x[t] !=",":
                   m=m+x[t]
                   t=t+1
               t=t+1
               while x[t] !=",":
                   n=n+x[t]
                   t=t+1
               t=t+1
               while x[t] !=")":
                   o=o+x[t]
                   t=t+1
               a=run(l)
               b=run(m)
               c=run(n)
               d=run(o)
       
               if(a=='*' or b=='*' or c=='*' or d=='*'):
                   a=0
                   b=0
                   c=0
                   d=0

               pygame.draw.line(screen,WHITE,[a, b],[c, d],2)
               file.write("pygame.draw.line(screen,WHITE,[")
               file.write(str(a))
               file.write(",")
               file.write(str(b))
               file.write("],[")
               file.write(str(c))
               file.write(",")
               file.write(str(d))
               file.write("],2)\n")
               l=""
               m=""
               n=""
               o=""
               p=""
               q=""
   
           elif(x[i:i+3] == "arc"):
               t=i+4
               while x[t] !=",":
                   l=l+x[t]
                   t=t+1
               t=t+1
               while x[t] !=",":
                   m=m+x[t]
                   t=t+1
               t=t+1
               while x[t] !=",":
                   n=n+x[t]
                   t=t+1
               t=t+1
               while x[t] !=",":
                   o=o+x[t]
                   t=t+1
               t=t+1
       
               while x[t] !=")":
                   q=q+x[t]
                   t=t+1
               a=run(l)
               b=run(m)
               c=run(n)
               d=run(o)
               f=run(q)
        
               if(a=='*' or b=='*' or c=='*' or d=='*' or f=='*'):
                   a=0
                   b=0
                   c=0
                   d=0
                   f=0

               else:
                pygame.draw.arc(screen,WHITE,[a-f,b-f,2*f,2*f],(c*pi)/180,(d*pi)/180,2)
                file.write("pygame.draw.arc(screen,WHITE,[")
                file.write(str(a-f))
                file.write(",")
                file.write(str(b-f))
                file.write(",")
                file.write(str(2*f))
                file.write(",")
                file.write(str(2*f))
                file.write("],")
                file.write(str((c*pi)/180))
                file.write(",")
                file.write(str((d*pi)/180))
                file.write(",2)  \n")
       
               l=""
               m=""
               n=""
               o=""
               p=""
               q=""
       
   
           elif(x[i:i+9]=="rectangle"):
               t=i+10
               while x[t] !=",":
                  l=l+x[t]
                  t=t+1
               t=t+1
               while x[t] !=",":
                  m=m+x[t]
                  t=t+1
               t=t+1
               while x[t] !=",":
                  n=n+x[t]
                  t=t+1
               t=t+1
               while x[t] !=")":
                  o=o+x[t]
                  t=t+1
       
               a=run(l)
               b=run(m)
               c=run(n)
               d=run(o)
      
               if(a=='*' or b=='*' or c=='*' or d=='*'):
                   a=0
                   b=0
                   c=0
                   d=0

               else:#pygame.draw.rect(screen,WHITE,[a,b,c-a,d-b],2)
               
                file.write("pygame.draw.rect(screen,WHITE,[")
                file.write(str(a))
                file.write(",")
                file.write(str(b))
                file.write(",")
                file.write(str(c-a))
                file.write(",")
                file.write(str(d-b))
                file.write("],2)\n")
               l=""
               m=""
               n=""
               o=""
               p=""
               q=""
       
   
           elif(x[i:i+7]=="ellipse"):
               t=i+8
               while x[t] !=",":
                   l=l+x[t]
                   t=t+1
               t=t+1
               while x[t] !=",":
                   m=m+x[t]
                   t=t+1
               t=t+1
               while x[t] !=",":
                   n=n+x[t]
                   t=t+1
               t=t+1
               while x[t] !=",":
                   o=o+x[t]
                   t=t+1
               t=t+1
               while x[t] !=",":
                   p=p+x[t]
                   t=t+1
               t=t+1
               while x[t] !=")":
                   q=q+x[t]
                   t=t+1
       
               a=run(l)
               b=run(m)
               c=run(n)
               d=run(o)
               e=run(p)
               f=run(q)
           
       
               if(a=='*' or b=='*' or c=='*' or d=='*' or e=='*' or f=='*'):
                  pygame.draw.ellipse(screen,BLACK,[100,100,20,20],2)
               elif(c==0.0 and d==360.0):
                  pygame.draw.ellipse(screen,WHITE,[a-e,b-f,2*e,2*f],2)
                  file.write("\npygame.draw.ellipse(screen,WHITE,[")
                  file.write(str(a-e))
                  file.write(",")
                  file.write(str(b-f))
                  file.write(",")
                  file.write(str(2*e))
                  file.write(",")
                  file.write(str(2*f))
                  file.write("],")
                  file.write("2)  \n")
          
               elif(c!=0 or d!=360):
                  pygame.draw.arc(screen, WHITE, [a-e,b-f,2*e,2*f],(c*pi)/180,(d*pi)/180,2)
                  file.write("\npygame.draw.arc(screen,WHITE,[")
                  file.write(str(a-f))
                  file.write(",")
                  file.write(str(b-f))
                  file.write(",")
                  file.write(str(2*e))
                  file.write(",")
                  file.write(str(2*f))
                  file.write("],")
                  file.write(str((c*pi)/180))
                  file.write(",")
                  file.write(str((d*pi)/180))
                  file.write(",2)  \n") 
       
               l=""
               m=""
               n=""
               o=""
               p=""
               q=""
       
           elif(x[i:i+6]=="circle"):
               t=i+7
               while x[t] != ",":
                   o=o+x[t]
                   t=t+1
               t=t+1
               while x[t] !=",":
                   p=p+x[t]
                   t=t+1
               t=t+1
               while x[t] !=")":
                   q=q+x[t]
                   t=t+1
       
               d=run(o)
               e=run(p)
               f=run(q)

               if(d=='*' or e=='*' or f=='*'):
                   d=0
                   e=0
                   f=0
       
       
               pygame.draw.arc(screen,WHITE,[d-f,e-f,2*f,2*f],0,2*pi,2)
               l=""
               m=""
               n=""
               o=""
               p=""
               q=""

               file.write("\npygame.draw.arc(screen,WHITE,[")
               file.write(str(d-f))
               file.write(",")
               file.write(str(e-f))
               file.write(",")
               file.write(str(2*f))
               file.write(",")
               file.write(str(2*f))
               file.write("],")
               file.write(str(0))
               file.write(",")
               file.write(str(2*pi))
               file.write(",2)  \n")
           
      
        pygame.display.flip()
        
        file.write("\n\npygame.display.flip()\ntime.sleep(10)")
        file.close()

     
def quit2():
    master.destroy()
    
def donothing():
   filewin = Toplevel(master)
   button = Button(filewin, text="Do nothing button")
   button.pack()


def ss():
    t=textBox.get("1.0","end-1c")
          
def pquit():
    pygame.quit()

menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open2)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=quit2)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_separator()

other = Menu(menubar, tearoff=0)
other.add_command(label="Execute", command=abc)
other.add_command(label="Stop",command=pquit)
menubar.add_cascade(label="Execution", menu=other)
master.config(menu=menubar)

master.mainloop()
