import math
import random
a=input("enter the messsege: ")
print(a)
bit=int(input("Enter the bit= ")) 
d=pow(10, bit-1)
z=pow(10, bit)-1
print(d)
print(z)

#Generate the prime
f=0
while f!=2:
    v=random.randrange(d+1,z,2)
    print("randam number=",v)


    w=int(math.sqrt(v))

    for j in range(2,w ):
            if (v % j == 0):
                r = 1
                break
            else:
                r=0
     
    if r==0:
        print(" prime") 
        
        f=f+1
        if f==1:
            p1=v
        else:
 
           q1=v

print("first prime=",p1)
print("Second prime=",q1)

# find n, phai, e,d
n= p1*q1
phai=(p1-1)*(q1-1)
print("Multiplication of p and q=", n)
print("Phai=", phai)

# find  e

f=0
while f!=1:
    for i in range(2,phai,1):
     y=math.gcd(phai,i)
     if y==1:
         f=f+1
         e=i
         break

print("E= ",e)
t=int(phai/e)
print("T= ",t)

# find  d


    
for i in range(t,phai*phai,1):

 y=(e*i) 
 y=y%phai
     
 if y==1:
   f=f+1
   d=i
   break



print("D= ",d)



#for x in a[0]:
if a[0]== 'A':
  b="00"
    
elif a[0]== 'B':
    
    b="01"
elif a[0]== 'C':
    
    b="02"
elif a[0]== 'D':
    
    b="03"
elif a[0]== 'E':
    
    b="04"
elif a[0]== 'F':
    
    b="05"
elif a[0]== 'G':
    
    b="06"

elif a[0]== 'H':
    
    b="07"
elif a[0]== 'I':
    
    b="08"

elif a[0]== 'J':
    
    b="09"
elif a[0]== 'K':
    
    b="10"
elif a[0]== 'L':
    
    b="11"
elif a[0]== 'M':
    
    b="12"
elif a[0]== 'N':
    
    b="13"
elif a[0]== 'O':
    
    b="14"
elif a[0]== 'P':
    
    b="15"

elif a[0]== 'Q':
    
    b="16"
elif a[0]== 'R':
    
    b="17"
elif a[0]== 'S':
    
    b="18"
elif a[0]== 'T':
    
    b="19"
elif a[0]== 'U':
    
    b="20"
elif a[0]== 'V':
    
    b="21"
elif a[0]== 'W':
    
    b="22"
elif a[0]== 'X':
    
    b="23"
elif a[0]== 'Y':
    
    b="24"
elif a[0]== 'Z':
    
    b="25"
else:
    
    b="26"

  

for x in range(1,len(a),1):
    if a[x]== 'A':
       c="00"
       b=b+c
    
    elif a[x]== 'B':
    
      c="01"
      b=b+c

    elif a[x]== 'C':
    
        c="02"
        b=b+c
    elif a[x]== 'D':
    
       c="03"
       b=b+c
    elif a[x]== 'E':
    
       c="04"
       b=b+c
    elif a[x]== 'F':

        c="05"
        b=b+c
    elif a[x]== 'G':
        
        c="06"
        b=b+c

    elif a[x]== 'H':
        
        c="07"
        b=b+c
    elif a[x]== 'I':
        
        c="08"
        b=b+c

    elif a[x]== 'J':
        
        c="09"
        b=b+c
    elif a[x]== 'K':
        
        c="10"
        b=b+c
    elif a[x]== 'L':
        
        c="11"
        b=b+c
    elif a[x]== 'M':
        
        c="12"
        b=b+c
    elif a[x]== 'N':
        
        c="13"
        b=b+c
    elif a[x]== 'O':
        
        c="14"
        b=b+c
    elif a[x]== 'P':
        
        c="15"
        b=b+c

    elif a[x]== 'Q':
        
        c="16"
        b=b+c
    elif a[x]== 'R':
        
        c="17"
        b=b+c
    elif a[x]== 'S':
        
        c="18"
        b=b+c
    elif a[x]== 'T':
        
        c="19"
        b=b+c
    elif a[x]== 'U':
        
        c="20"
        b=b+c
    elif a[x]== 'V':
        
        c="21"
        b=b+c
    elif a[x]== 'W':
        
        c="22"
        b=b+c
    elif a[x]== 'X':
        
        c="23"
        b=b+c
    elif a[x]== 'Y':
        
        c="24"
        b=b+c
    elif a[x]== 'Z':
        
        c="25"
        b=b+c
    else:
        
        c="26"
        b=b+c

b=int(b)

print(b)

x=1
for i in range(0,e):
    x=x*b


C=x%n
print("Cyphir=",C)

x=1
for i in range(0,d):
    x=x*C


D=x%n
print("decrept=",D)

a=str(D)
print("a= "+a)
si=len(a)
b= ' '
if si%2!=0:
    a='0'+a
for x in range(0,si,2):
    if a[x]== '0' and a[x+1]== '0' :
       c="A"
       b=b+c
    
    elif  a[x]== '0' and a[x+1]== '1':
    
      c="B"
      b=b+c

    elif  a[x]== '0' and a[x+1]== '2':
    
        c="C"
        b=b+c
    elif  a[x]== '0' and a[x+1]== '3':
    
       c="D"
       b=b+c
    elif  a[x]== '0' and a[x+1]== '4':
    
       c="E"
       b=b+c
    elif  a[x]== '0' and a[x+1]== '5':

        c="F"
        b=b+c
    elif a[x]== '0' and a[x+1]== '6':
        
        c="G"
        b=b+c

    elif  a[x]== '0' and a[x+1]== '7':
        
        c="H"
        b=b+c
    elif a[x]== '0' and a[x+1]== '8':
        
        c="I"
        b=b+c

    elif  a[x]== '0' and a[x+1]== '9':
        
        c="J"
        b=b+c
    elif  a[x]== '1' and a[x+1]== '0':
        
        c="K"
        b=b+c
    elif  a[x]== '1' and a[x+1]== '1':
        
        c="L"
        b=b+c
    elif  a[x]== '1' and a[x+1]== '2':
        
        c="M"
        b=b+c
    elif  a[x]== '1' and a[x+1]== '3':
        
        c="N"
        b=b+c
    elif  a[x]== '1' and a[x+1]== '4':
        
        c="O"
        b=b+c
    elif a[x]== '1' and a[x+1]== '5':
        
        c="P"
        b=b+c

    elif a[x]== '1' and a[x+1]== '6':
        
        c="Q"
        b=b+c
    elif a[x]== '1' and a[x+1]== '7':
        
        c="R"
        b=b+c
    elif a[x]== '1' and a[x+1]== '8':
        
        c="S"
        b=b+c
    elif a[x]== '1' and a[x+1]== '9':
        
        c="T"
        b=b+c
    elif a[x]== '2' and a[x+1]== '0':
        
        c="U"
        b=b+c
    elif a[x]== '2' and a[x+1]== '0':
        
        c="V"
        b=b+c
    elif a[x]== '2' and a[x+1]== '0':
        
        c="W"
        b=b+c
    elif a[x]== '2' and a[x+1]== '0':
        
        c="X"
        b=b+c
    elif a[x]== '2' and a[x+1]== '0':
        
        c="Y"
        b=b+c
    elif a[x]== '2' and a[x+1]== '0':
        
        c="Z"
        b=b+c
    else:
        
        c=" "
        b=b+c
print("Real txt is "+b)

    

