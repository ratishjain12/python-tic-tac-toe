import sys
l = ["_","_","_",
     "_","_","_",
     "_","_","_",]

running = True
chance = 1
boolean = False
if running:
    def board():
            print(l[0]+' | ',l[1]+' | ',l[2],sep='')
            print(l[3]+' | ',l[4]+' | ',l[5],sep='')
            print(l[6]+' | ',l[7]+' | ',l[8],sep='')

    board()



    
while running:
    
    def firstplayer(value):
        l[value-1] = 'X'

    def secondplayer(value):
        l[value-1] = 'O'

    def rows():
        if l[0] == l[1] and l[0]==l[2]:
            if l[0] == 'X':
                print('Player 1 wins')
                running = False
                sys.exit()
            elif l[0] == 'O':
                print('Player 2 wins')
                running = False
                sys.exit()
                
            

                
        elif l[3] == l[4] and l[3]==l[5]:
            if [3] == 'X':
                print('Player 1 wins')
                running = False
                sys.exit()
                
            elif l[3] == 'O':
                print('Player 2 wins')
                running = False
                sys.exit()
                
        elif l[6] == l[7] and l[6]==l[8]:
            if [6] == 'X':
                print('Player 1 wins')
                running = False
                sys.exit()
                
            elif l[6] == 'O':
                print('Player 2 wins')
                running = False
                sys.exit()
                
                

    def columns():
        if l[0] == l[3] and l[0]==l[6]:
            if l[0] == 'X':
                print('Player 1 wins')
                running = False
                sys.exit()
                
            elif l[0] == 'O':
                print('Player 2 wins')
                running = False
                sys.exit()
                
        elif l[1] == l[4] and l[1]==l[7]:
            if l[1] == 'X':
                print('Player 1 wins')
                running = False
                sys.exit()
                
            elif l[1] == 'O':
                print('Player 2 wins')
                running = False
                sys.exit()
                
            
        elif l[2] == l[5] and l[2]==l[8]:
            if l[2] == 'X':
                print('Player 1 wins')
                running = False
                sys.exit()
                
            elif l[2] == 'O':
                print('Player 2 wins')
                running = False
                sys.exit()
                

    def diagonals():
        if l[0] == l[4] and l[0]==l[8]:
            if l[0] == 'X':
                print('Player 1 wins')
                running = False
                sys.exit()
                
            elif l[0] == 'O':
                print('Player 2 wins')
                running = False
                sys.exit()
                
                
        elif l[2] == l[4] and l[2]==l[6]:
            if l[2] == 'X':
                print('Player 1 wins')
                running = False
                sys.exit()
                
                
            elif l[2] == 'O':
                print('Player 2 wins')
                running = False
                sys.exit()
                
                
        

    def checking():
        rows()
        columns()
        diagonals()
        
                
                

    i = 0
    while boolean != True:
        if chance == 1:
            player1 = int(input('Player 1 enter position from 1 to 9(x)'))
            chance = 0
            i+=1
            firstplayer(player1)
            board()
            checking()
            
            

        if i == 9:
            chance = 2
            boolean = True
            
            
        
        else:
            player2 = int(input('Player 2 enter position from 1 to 9(0)'))
            chance = 1
            i+=1
            secondplayer(player2)
            board()
            checking()
            
            
    


    
    
