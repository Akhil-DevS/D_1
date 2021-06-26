
    #this is a program for calaulator

def sub(a):
        b=input("enter the second number")
        sub=int(a)-int(b)
        return(sub)

def add(a):
        b=input("enter the second number")
        add=int(a)+int(b)
        return(add)

def multi(a):
        b=input("enter the second number")
        multi=int(a)*int(b)
        return(multi)

def div(a):
        b=input("enter the second number")
        if(int(b)==0):
            print("divided by zero error")
            return(0)
        else:
            div=int(a)/int(b)
        return(div)

    #main body
print("\t\t CALCULATOR")
num1=input("\nenter the 1st number")

while(True):
    op=input("\nenter the operation(+,-,*,/)")
    if(op=='+'):
       ans=add(num1)
    elif(op=='-'):
        ans=sub(num1)
    elif(op=='*'):
        ans=multi(num1)
    elif(op=='/'):
        ans=div(num1)
        if(ans==0):
            break
    else:
        print('***invalid input***')
        break
    x=input('\n Do more operations on the result?(y/n)')
    if(x=='y' or x=='Y'):
        num1=ans
    elif(x=='n' or x=='N'):
        anstr=str(ans)
        print("\nSolution="+anstr)
        break
    else:
        anstr = str(ans)
        print("invalid input\n Solution till now= "+anstr)
        break
        
