
'''
# program to reverse a number
class demo:
def __init__ (s):
    s.rrev=0
def accept(s):
    s.n=int(input("enter the value"))
def process(s):
    while s.n>0:s.r=s.n%10
        s.rev=s.rev*10+s.r
        s.n=s.n//10
    print(s.rev)
d=demo()
d.accept()
d.process()
 '''
''''
# program to check given number is palindrome or not
class demo:
    def __init__(self):
        self.rev=0
    def accept (self):
        self.n=int(input("enter the value"))
        self.num=self.n
    def process(self):
        while self.num>0:
            self.r=self.num%10
            self.rev=self.rev*10+self.r
            self.num=self.num//10
        if self.rev==self.n:
           print("palindrom")
        else :
            print("not a palindrom")
d=demo()
d.accept()
d.process()
'''
'''
#program to find sum of squares of a given number
class Demo:
    def __init__ (self):
        self.sum=0
    def accept (self):
        self.n=int(input("enter the value"))
    def process(self):
        while self.n>0:
            self.r=self.n%10
            self.sum=self.sum+self.r**2
            self.n=self.n//10
        print(self.sum)    

d=Demo()
d.accept()
d.process()
'''
'''
#program to find no of digits
class Demo:
    def __init__(self):
        self.count=0
    def accept (self):
        self.n=int(input("enter the cvalue"))
    def process (self):
        while self.n>0:
            self.count=self.count+1
            self.n=self.n//10
        print(self.count)
d=Demo()
d.accept()
d.process()
'''
'''
#program to find the power p(b**p) of a number
class Demo:
    def __init__(s):
        s.res=1
        s.count=1
    def accept (s):
        s.b=int(input("enter the value"))
        s.p=int(input("enter the value"))
    def process(s):
        while s.count<=s.p:
              s.res=s.res*s.b
              s.count=s.count+1
        print(s.res)
d=Demo()
d.accept()
d.process()
'''
'''
# program to find amrstrong number
class demo:
    def __init__ (s):
        s.count=0
        s.sum=0
    def accept (s):
        s.n=int(input("enter the value"))
        s.num=s.n
        s.x=s.n
    def process (s):
        while s.n!=0:
            s.n=s.n//10
            s.count=s.count+1
        while s.num!=0:
            s.r=s.num%10
            s.sum=s.sum+s.r**s.count
            s.num=s.num//10
        if s.sum==s.x:
            print("armsto")
        else:
            print("not arm")
d=demo()
d.accept()
d.process()
'''
'''
#program to find factorial of a number (using while loop)
class demo:
    def __init__(s):
        s.count=1
        s.fact=1
    def accept(s):
        s.n=int(input("enter th value"))
    def process(s):
        while s.count<=s.n:
            s.fact=s.fact*s.count
            s.count=s.count+1
        print(s.fact)
d=demo()
d.accept()
d.process()
'''
'''
#program to find factorialof a number(using for loop)
class demo:
    def __init__(s):
        s.fact=1
    def accept(s):
        s.n=int(input("enter the value"))
    def process(s):
        for i in range(1,s.n+1):
            s.fact=s.fact*i
        print(s.fact)
d=demo()
d.accept()
d.process()
'''
'''
# program to print mathe table(tables)(at given range)
class demo:
    def __init__(s):
        s.fact=1
    def accept(s):
        s.n=int(input("enter the value"))
    def process(s):
        for i in range(1,11):
            s.fact=s.n*i
        print(s.fact)
        i=i+1
        
d=demo()
d.accept()
d.process()
'''
'''
#program to print mathe table(nth table)
class demo:
    def __init__(s):
        s.count=1
        s.fact=1
    def accept(s):
        s.n=int(input("enter th value"))
    def process(s):
        while s.count<=10:
            s.fact=s.count*s.n
            s.count=s.count+1
            print("{}*{}={}".format(s.n,s.count,s.fact))
d=demo()
d.accept()
d.process()
'''
'''
# program to check given number is prime or not
class demo:
    def __init__(s):
        s.c=2
        s.r=1
    def accept(s):
        s.n=int(input("enter the value"))
    def process(s):
        while s.c<=s.n/2 and s.r!=0:
            s.r=s.n%s.c
            s.c=s.c+1
        if s.r!=0:
            print("prime")
        else:
            print("not prime")
d=demo()
d.accept()
d.process()
'''
'''
# program to find GCD of two numbers
class demo:
    def __init__(s):
        pass
    def accept(s):
        s.a=int(input("enter the a value"))
        s.b=int(input("rnter b value"))
    def process(s):
        while s.a!=s.b:
            if s.a>s.b:
                s.a=s.a-s.b
            else:
                s.b=s.b-s.a
        print("a",s.a)        
d=demo()
d.accept()
d.process()                
'''
'''
#program for another form to find the GCD
class demo:
    def __init__(s):
        pass
    def accept(s):
        s.a=int(input("enter the value"))
        s.b=int(input("enter the value of b"))
    def process(s):
        while s.b!=0:
            r=s.a%s.b
            s.a=s.b
            s.b=r
        print(s.a)
d=demo()
d.accept()
d.process()
'''
'''
# program to find fibanocci ser
class demo:
    def __init__(s):
        s.a=0
        s.b=1
        s.c=1
    def accept(s):
        pass
    def process(s):
        while s.c<=100:
            s.c=s.a+s.b
            s.a=s.b
            s.b=s.c
            print(s.a)    
d=demo()
d.accept()
d.process()
'''
'''
# program to find n fibanocci series
class demo:
    def __init__ (s):
        s.a=0
        s.b=1
        s.i=1
    def accept(s):
        s.n=int(input("enter the value"))
    def process(s):
        while s.i<=s.n:
            s.c=s.a+s.b
            s.a=s.b
            s.b=s.c
            s.i=s.i+1
            print(s.a)
d=demo()
d.accept()
d.process()
'''
'''
# to print the seris
class demo:
    def __init__ (s):
        s.sum=0
        s.i=1
    def accept(s):
        s.n=int(input("enter the value"))
    def process(s):
        while s.i<=s.n:
            s.sum=s.sum+1/s.i
            s.i=s.i+1
            print("s.sum",s.sum)
d=demo()
d.accept()
d.process()            
'''
'''
#programe to print 1-(1/2)+(1/3)
class demo:
    def __init__ (s):
        s.sum=0
        s.i=1
    def accept(s):
        s.n=int(input("enter the value"))
    def process(s):
        while s.i<=s.n:
            if s.i%2==0:
                s.sum=s.sum-(1/s.i)
                print('-','1/',s.i,end=' ')
            else :
                s.sum=s.sum+(1/s.i)
                print('+','1/',s.i,end=' ')
            s.i=s.i+1            
d=demo()
d.accept()
d.process()
'''
'''
# programe to find factorial of a given number
class demo:
    def __init__(s):
        s.fact=1
        s.i=1
        s.sum=1
    def accept(s):
        s.n=int(input("enter the value"))
    def process(s):
        while s.n>=s.i:
             s.fact=s.fact*s.i
             s.sum=s.sum+(s.i/s.fact)
             s.i=s.i+1
        print(s.sum)
             
             
             
d=demo()
d.accept()
d.process()
'''
'''
#programe to find sum of two numbers(without using expression)
class demo:
    def __init__ (s):
        pass
    def accept(s):
        s.a=int(input("enter a value"))
        s.b=int(input("enter b value"))
    def process(s):
        while s.b>0:
            s.a=s.a+1
            s.b=s.b-1
        print(s.a)
d=demo()
d.accept()
d.process()
''''''
#programe to find sub of two numbers(without using expression)
class demo:
    def __init__ (s):
        pass
    def accept(s):
        s.a=int(input("enter a value"))
        s.b=int(input("enter b value"))
    def process(s):
        while s.b>0:
            s.a=s.a-1
            s.b=s.b-1
        print(s.a)    
d=demo()
d.accept()
d.process()
''''''
#programe to find mul of two numbers(without using expression)
class demo:
    def __init__ (s):
        s.c=1
        s.pro=1
    def accept(s):
        s.a=int(input("enter a value"))
        s.b=int(input("enter b value"))
    def process (s):
        while s.b>0:
            s.pro=s.a*s.c
            s.c=s.c+1
            s.b=s.b-1
            print(s.pro)
d=demo()
d.accept()
d.process()
'''
'''
#programe to find mul of two numbers(without using expression)
class demo:
    def __init__ (s):
        s.pro=0
    def accept(s):
        s.a=int(input("enter a value"))
        s.b=int(input("enter b value"))
    def process (s):
        while s.b>0:
           s.pro=s.pro+s.a
           s.b=s.b-1
        print(s.pro)
d=demo()
d.accept()
d.process()
'''
'''
# program using nested while loop
class demo:
    def __init__ (s):
        s.i=1
    def accept(s):
        pass
    def process(s):
        while s.i<=5:
            s.j=1
            while s.j<=6:
                print(s.j,end=" ")
                s.j=s.j+1
            s.i=s.i+1
            print()
d=demo()
d.accept()
d.process()
''''

'''
# program to print mathe table
class demo:
    def __init__(s):
        s.p=1
    def accept (s):
        s.a=int(input("enter a value"))
        s.b=int(input("enter b value"))
    def process(s):
        while s.a<=s.b:
            s.c=1
            while s.c<=10:
                s.p=s.a*s.c
                print("{}*{}={}".format(s.a,s.c,s.p))
                s.c=s.c+1
            s.a=s.a+1    
d=demo()
d.accept()
d.process()
'''
'''
# program to print perfect number
class demo:
    def __init__(s):
        pass
    def accept (s):
        s.i=int(input("enter a value"))
        s.f=int(input("enter b value"))
    def process(s):
        while s.i<=s.f:
            s.c=1
            s.sum=0
            while s.c<=s.i/2:
                s.r=s.i%s.c
                if s.r=0:
                    s.sum=s.sum+s.c
                s.c=s.c+1
            if s.i=s.sum:
                print(s.i)
        
d=demo()
d.accept()
d.process()
'''
'''
 #perfect number
class demo:
    def __init__(s):
        pass
    def accept (s):
        s.i=int(input("enter a value"))
        s.f=int(input("enter b value"))
    def process(s):
        while s.i<=s.f:
            s.c=1
            s.sum=0    
            while s.c<=s.i/2:
                s.r=s.i%s.c
                if s.r==0:
                    s.sum=s.sum+s.c
                s.c=s.c+1
            if s.i==s.sum:
                print(s.i)
            s.i=s.i+1
        
d=demo()
d.accept()
d.process()
''''
        
       









            
        
     
            
    


            




















