import random as rd
x=rd.randint(1,100)
print(x)
points=10
print('\tthis game selects a random number from 1-100.\n\tGuess the number')
guess=input('enter the number\n')
if(int(guess)==x):
    print('\nCorrect guess\n\t\b10 Points')
elif(int(guess)<50):
    print('\n\t you answer is wrong\n Clue1-the value is less than 50')
    guess=input('Enter the second guess\n')
    if (int(guess) == x):
        print('\nCorrect guess\n\t\b8 Points')
    elif(x%2==0):
        print('\n\t you answer is wrong\n Clue1-the value divisiable by 2 ')
        guess=input('Enter third guess\n')
        if (int(guess)==x):
            print('\nCorrect guess\n\t\b6 Points')
        elif(x%3==0):
            print('\n\t you answer is wrong\n Clue2-the value divisiable by 3 ')
            guess=input('Enter forth guess\n')
            if (int(guess)==x):
                print('\nCorrect guess\n\t\b4 Points')
            elif (x%5==0):
                print('\n\t you answer is wrong\n Clue1-the value divisiable by 5 ')
                guess=input('Enter final guess\n')
                if (int(guess)==x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was '+str(x))
            else:
                print('\n\t you answer is wrong\n Clue1-the value not divisiable by 5 ')
                guess=input('Enter final guess\n')
                if (int(guess)==x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was '+str(x))
        else:
            print('\n\t you answer is wrong\n Clue2-the value not divisiable by 3 ')
            guess = input('Enter forth guess\n')
            if (int(guess) == x):
                print('\nCorrect guess\n\t\b4 Points')
            elif (x % 5 == 0):
                print('\n\t you answer is wrong\n Clue1-the value divisiable by 5 ')
                guess = input('Enter final guess\n')
                if (int(guess) == x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was ' + str(x))
            else:
                print('\n\t you answer is wrong\n Clue1-the value not divisiable by 5 ')
                guess=input('Enter final guess\n')
                if (int(guess)==x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was '+str(x))
    else:
        print('\n\t you answer is wrong\n Clue1-the value not divisiable by 2 ')
        guess = input('Enter third guess\n')
        if (int(guess)==x):
            print('\nCorrect guess\n\t\b6 Points')
        elif (x % 3 == 0):
            print('\n\t you answer is wrong\n Clue2-the value divisiable by 3 ')
            guess = input('Enter forth guess\n')
            if (int(guess) == x):
                print('\nCorrect guess\n\t\b4 Points')
            elif (x % 5 == 0):
                print('\n\t you answer is wrong\n Clue1-the value divisiable by 5 ')
                guess = input('Enter final guess\n')
                if (int(guess) == x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was ' + str(x))
        else:
            print('\n\t you answer is wrong\n Clue2-the value not divisiable by 3 ')
            guess = input('Enter forth guess\n')
            if (int(guess) == x):
                print('\nCorrect guess\n\t\b4 Points')
            elif (x % 5 == 0):
                print('\n\t you answer is wrong\n Clue1-the value divisiable by 5 ')
                guess = input('Enter final guess\n')
                if (int(guess) == x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was ' + str(x))
            else:
                print('\n\t you answer is wrong\n Clue1-the value not divisiable by 5 ')
                guess=input('Enter final guess\n')
                if (int(guess)==x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was '+str(x))
elif(int(guess)>=50):
    print('\n\t you answer is wrong\n Clue1-the value is greater than or equal than 50')
    guess=input('Enter the second guess\n')
    if (int(guess) == x):
        print('\nCorrect guess\n\t\b8 Points')
    elif(x%2==0):
        print('\n\t you answer is wrong\n Clue1-the value divisiable by 2 ')
        guess=input('Enter third guess\n')
        if (int(guess)==x):
            print('\nCorrect guess\n\t\b6 Points')
        elif(x%3==0):
            print('\n\t you answer is wrong\n Clue2-the value divisiable by 3 ')
            guess=input('Enter forth guess\n')
            if (int(guess)==x):
                print('\nCorrect guess\n\t\b4 Points')
            elif (x%5==0):
                print('\n\t you answer is wrong\n Clue1-the value divisiable by 5 ')
                guess=input('Enter final guess\n')
                if (int(guess)==x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was '+str(x))
            else:
                print('\n\t you answer is wrong\n Clue1-the value not divisiable by 5 ')
                guess=input('Enter final guess\n')
                if (int(guess)==x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was '+str(x))
        else:
            print('\n\t you answer is wrong\n Clue2-the value not divisiable by 3 ')
            guess = input('Enter forth guess\n')
            if (int(guess) == x):
                print('\nCorrect guess\n\t\b4 Points')
            elif (x % 5 == 0):
                print('\n\t you answer is wrong\n Clue1-the value divisiable by 5 ')
                guess = input('Enter final guess\n')
                if (int(guess) == x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was ' + str(x))
            else:
                print('\n\t you answer is wrong\n Clue1-the value not divisiable by 5 ')
                guess=input('Enter final guess\n')
                if (int(guess)==x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was '+str(x))
    else:
        print('\n\t you answer is wrong\n Clue1-the value not divisiable by 2 ')
        guess = input('Enter third guess\n')
        if (int(guess)==x):
            print('\nCorrect guess\n\t\b6 Points')
        elif (x % 3 == 0):
            print('\n\t you answer is wrong\n Clue2-the value divisiable by 3 ')
            guess = input('Enter forth guess\n')
            if (int(guess) == x):
                print('\nCorrect guess\n\t\b4 Points')
            elif (x % 5 == 0):
                print('\n\t you answer is wrong\n Clue1-the value divisiable by 5 ')
                guess = input('Enter final guess\n')
                if (int(guess) == x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was ' + str(x))
        else:
            print('\n\t you answer is wrong\n Clue2-the value not divisiable by 3 ')
            guess = input('Enter forth guess\n')
            if (int(guess) == x):
                print('\nCorrect guess\n\t\b4 Points')
            elif (x % 5 == 0):
                print('\n\t you answer is wrong\n Clue1-the value divisiable by 5 ')
                guess = input('Enter final guess\n')
                if (int(guess) == x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
                    print('the nummber was ' + str(x))
            else:
                print('\n\t you answer is wrong\n Clue1-the value not divisiable by 5 ')
                guess=input('Enter final guess\n')
                if (int(guess)==x):
                    print('\nCorrect guess\n\t\b2 Points')
                else:
                    print('\n you lose better luck next time!')
