#NOUGHTS & CROSSES
#initialising the game board
ttt={1:' ',2:' ',3:' ',     
     4:' ',5:' ',6:' ',
     7:' ',8:' ',9:' '}
print("WELCOME TO NOUGHTS & CROSSES!\nFollow this guide to play:")
print("1|2|3\n-*-*-\n4|5|6\n-*-*-\n7|8|9") #printing the guide
print()
thekeys=[]     
for i in ttt:
    thekeys.append(i) #list with the values of the board
def printtoe(x):       #function to print the board each time 
    print(ttt[1]+'|'+ttt[2]+'|'+ttt[3])
    print("-*-*-")
    print(ttt[4]+'|'+ttt[5]+'|'+ttt[6])
    print("-*-*-")
    print(ttt[7]+'|'+ttt[8]+'|'+ttt[9])
def thegame():
    chance='X'
    c=0
    while c<9: 
        printtoe(ttt)
        print("It's your chance " + chance + '!')
        movein = input("Enter the move according to the guide - ")
        #checking for valid input

        if len(movein)>1 or len(movein)==0 or 9<=ord(movein)<=47 or 58<=ord(movein)<=126:  
            print("Invalid input. Enter valid input according to guide.")  
            continue
        else:
            move=int(movein)
            if 1<= move and move<=9:
                if ttt[move]==' ': #filling up the space on the board if available
                    ttt[move]=chance 
                    c+=1
                else:
                    print("Occupied position!\nInput unoccupied position!")
                    continue
            else:  
                print("Invalid input. Enter valid input according to guide.")
                continue

        #checking if there is a winner
        if c >= 5:
            if ttt[1] == ttt[2] == ttt[3] != ' ': #checking across the top
                printtoe(ttt)
                print("\nGame Over.\n")                
                print("Congratulations! " + chance + " is the winner!")                
                break
            elif ttt[4] == ttt[5] == ttt[6] != ' ': #checking across the middle
                printtoe(ttt)
                print("\nGame Over.\n")                
                print("Congratulations! " + chance + " is the winner!")                
                break
            elif ttt[7] == ttt[8] == ttt[9] != ' ': #checking across the bottom
                printtoe(ttt)
                print("\nGame Over.\n")                
                print("Congratulations! " + chance + " is the winner!")
                break
            elif ttt[1] == ttt[4] == ttt[7] != ' ': #checking down the left side
                printtoe(ttt)
                print("\nGame Over.\n")                
                print("Congratulations! " + chance + " is the winner!")
                break
            elif ttt[2] == ttt[5] == ttt[8] != ' ': #checking down the middle
                printtoe(ttt)
                print("\nGame Over.\n")                
                print("Congratulations! " + chance + " is the winner!")
                break
            elif ttt[3] == ttt[6] == ttt[9] != ' ': #checking down the right side
                printtoe(ttt)
                print("\nGame Over.\n")                
                print("Congratulations! " + chance + " is the winner!")
                break 
            elif ttt[7] == ttt[5] == ttt[3] != ' ': #checking diagonal 1
                printtoe(ttt)
                print("\nGame Over.\n")                
                print("Congratulations! " + chance + " is the winner!")
                break
            elif ttt[1] == ttt[5] == ttt[9] != ' ': #checking diagonal 2
                printtoe(ttt)
                print("\nGame Over.\n")                
                print("Congratulations !" + chance + " is the winner!")
                break
        if c == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            break

        #changing player after every move.
        if chance =='X':
            chance = 'O'
        else:
            chance = 'X'
    print()    

    #giving the option to play again
    p=0
    while p==0:
        choice = input("Do you want to play again? \nYes - Enter y/Y \nNo - Enter n/N ")
        if choice == "y" or choice == "Y":
            p=1
            for i in thekeys:
                ttt[i] = " "        #makes the whole board blank if u want to play again
            thegame()
        elif choice == "n" or choice == "N":
            p=1
            print("Thank you for playing NOUGHTS & CROSSES! See you later!")
        else:
            print("Invalid input.")
thegame() #calling the game
