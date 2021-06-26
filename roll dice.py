import random as rd
def dice_roll():
    x=True
    print('\t\t\nRolling dice')
    y=rd.randint(1,6)
    i=1
    print('dice roll '+str(i)+' = '+str(y))
    while(x==True):
        print('Do you want to continue?(y/n)')
        ans=input('answer ').lower().strip()
        if(ans=='y'):
            y=rd.randint(1,6)
            i+=1
            print('dice roll '+str(i)+' = '+str(y))
        elif(ans=='n'):
            x=False
            print('thankyou')
        else:
            print('invalid input, try again')



