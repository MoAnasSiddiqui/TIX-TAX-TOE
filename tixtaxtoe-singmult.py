import random
import time
pos=["0","1","2","3","4","5","6","7","8","9"]
randomdo=[0,5,1,3,7,9,2,4,6,8]
name=[0,1]
sign=["X","O"]
another="N"
win0,win1,draw=0,0,0
first=True
while True:
    if another!="Y":
        if first==False:
            time.sleep(0.5)
            print(f"\n\n\nScorecard:\n \nWins({savedn0}): {win0}\nWins({savedn1}): {win1}\nDraws: {draw} \n\n\n")
            time.sleep(1)
            print("Starting in 3 seconds...\n\n")
            time.sleep(3)
        win0,win1,draw=0,0,0
        print("Tic-Tac-Toe v4.1.1 | Made by Mohammad Anas Siddiqui\n\n\n   TIX-TAX-TOE™\n\n")
        print("      |     |   \n  ",pos[1]," | ",pos[2]," | ",pos[3],"   \n _____|_____|_____\n      |     |    \n  ",pos[4]," | ",pos[5]," | ",pos[6],"   \n _____|_____|_____\n      |     |    \n  ",pos[7]," | ",pos[8]," | ",pos[9],"    \n      |     |     \n\n")
        print("Welcome to TicTacToe v4.1.1.\n\n\nDo you want to play as single player or multiplayer?\n\nPress 1 to play Player vs Player.\nPress 2 to play Player vs PC.\nPress any other key to exit the game.\n\n\nEnter your choice: ",end="")
        mode=input()
        if mode!="1" and mode!="2":
            break
        else:
            print("\n-----------------------------------------------------\n")
            name[0]=input("Player1. Enter your name: ")
            print(name[0],"Do you want to choose 'X' or 'O':",end=" ")
            choice=input()
            choice=choice.upper()
            while choice!="X" and choice!="O":
                choice=input("Enter again: ")
                choice=choice.upper()
            if choice=="O":
                sign[1],sign[0]=sign[0],sign[1]
            print("Your sign is: ",sign[0])
            print()
            time.sleep(0.5)
            if mode=="1":
                name[1]=input("Player2. Enter your name: ")
                print("Your sign is: ",sign[1],"\n")
            else:
                name[1]="PC"
                print("Player 2 is PC. PC sign is: ",sign[1])
    if first==True:
        savedn0,savedn1=name[0],name[1]
        first=False
    #Toss
    time.sleep(0.5)
    call=random.randint(0,1)
    if mode=="2" and name[1]=="PC": call=0
    if mode=="2" and name[0]=="PC": call=1
    toss=str(random.randint(1,2))
    #print((call+1),toss)
    print("\n")
    print(name[call],end="")
    choice=input(", will call the toss. Enter 1 for Head or 2 for Tail? ")
    while choice!="1" and choice!="2":
        choice=input("Enter again: ")
    if choice==toss:
        print( name[call],"has won the toss.")
        name[call],name[(call+1)%2]=name[0],name[1]
        sign[call],sign[(call+1)%2]=sign[0],sign[1]
    else:
        print(name[(call+1)%2],"has won the toss.\n")
        name[(call+1)%2],name[call]=name[0],name[1]
        sign[(call+1)%2],sign[call]=sign[0],sign[1]
    time.sleep(0.5)
    print("\n")
    pos=["0","1","2","3","4","5","6","7","8","9"]
    win=False
    #Move
    for move in range(0,9):
        step=move%2
        if mode=="1" or name[step]!="PC":
            print(name[step], end="")
            print(", Where do you want to enter",sign[step],": ",end="")
            user=input()
            while True:
                if user not in pos or user=="0":
                    user=input("Enter again: ")
                else:
                    break
            user=int(user)
            print(f"{name[step]} ({sign[step]}) chooses place {user}.\n")
            pos[user]=sign[step]
        else:
            do="0"
            inuse=sign[step]
            while do=="0":
                for j in range (1,10):
                    copy=list(pos)
                    if pos[j]==str(j):
                        copy[j]=inuse
                    if (copy[1]==copy[2]==copy[3]) or (copy[4]==copy[5]==copy[6]) or (copy[7]==copy[8]==copy[9]) or (copy[1]==copy[5]==copy[9]) or (copy[3]==copy[5]==copy[7]) or (copy[1]==copy[4]==copy[7]) or (copy[2]==copy[5]==copy[8]) or (copy[3]==copy[6]==copy[9]):
                        do=j
                        break
                if inuse==sign[step]:
                    inuse=sign[(step+1)%2]
                else:
                    break
            if do=="0":
                inuse=sign[step]
                ftrap=0
                while do=="0":
                    for i in range (1,10):
                        fwin=0
                        copy=list(pos)
                        if copy[i]==str(i):
                            copy[i]=inuse
                        else:
                            continue       
                        for j in range (1,10):
                            if copy[j]==str(j):
                                copy[j]=inuse
                            else:
                                continue
                            if (copy[1]==copy[2]==copy[3]) or (copy[4]==copy[5]==copy[6]) or (copy[7]==copy[8]==copy[9]) or (copy[1]==copy[5]==copy[9]) or (copy[3]==copy[5]==copy[7]) or (copy[1]==copy[4]==copy[7]) or (copy[2]==copy[5]==copy[8]) or (copy[3]==copy[6]==copy[9]):
                                fwin+=1
                            copy[j]=str(j)
                        if fwin==2:
                            fwin=0
                            ftrap+=1
                            save=i
                    if ftrap==2:
                        if inuse==sign[(step+1)%2]:
                            for k in range(2,9,2):
                                if pos[k]==str(k):
                                    do=k
                                    break
                        else:
                            do=save
                    if ftrap==1:
                        do=save
                        break
                    if inuse==sign[step]:
                        inuse=sign[(step+1)%2]
                    else:
                        break
            if do=="0":
               for i in range(1,10):
                   if pos[randomdo[i]]==str(randomdo[i]):
                       do=randomdo[i]
                       break
            print(f"Computer ({sign[step]}) chooses place {do}.\n")
            pos[do]=sign[step]                
        print("      |     |   \n  ",pos[1]," | ",pos[2]," | ",pos[3],"   \n _____|_____|_____\n      |     |    \n  ",pos[4]," | ",pos[5]," | ",pos[6],"   \n _____|_____|_____\n      |     |    \n  ",pos[7]," | ",pos[8]," | ",pos[9],"    \n      |     |     \n\n")
        time.sleep(0.5)
        if ((pos[1]==pos[2]==pos[3]==sign[step]) or (pos[4]==pos[5]==pos[6]==sign[step]) or (pos[7]==pos[8]==pos[9]==sign[step]) or (pos[1]==pos[4]==pos[7]==sign[step]) or (pos[2]==pos[5]==pos[8]==sign[step]) or (pos[3]==pos[6]==pos[9]==sign[step]) or (pos[1]==pos[5]==pos[9]==sign[step]) or (pos[3]==pos[5]==pos[7]==sign[step])):
                print(name[step],"have won") 
                if name[step]==savedn0:
                    win0=win0+1
                else:
                    win1=win1+1
                win=True
                break
    if win==False: 
        print("Its a draw.")
        draw=draw+1
    another=input(("\n\nDo you want to play again? Press Y for yes or press any other key to display the main menu: "))
    another=another.upper()
print("\n\nThanks for playing.\nThis game is designed by Mohammed Anas Siddiqui.")
        
    

   
