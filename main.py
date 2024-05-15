import random

class Player: 
    def __init__(self) -> None:
        pass
    def GenerateBoard(self):
        array = []
        for i in range(10):
            addlist = []
            for n in range(10):
                addlist.append(".")
            array.append(addlist)
        return array
    def SetupBoard(self, playerArray):
        carrierset = False
        battleshipset = False
        cruiserset = False
        submarineset = False
        destroyerset = False
        while True:
            if carrierset == True and battleshipset == True and cruiserset == True and submarineset == True and destroyerset == True:
                break
        
            
            if carrierset == False:
                while True:
                    pcarrier = input("Please enter the row and column you would like to place your 'Carrier' (row-col): ")
                    row, column = pcarrier.split("-")
                    row, column = int(row), int(column)
                    if row > 10 or column > 10:
                        continue
                    else:
                        row -= 1
                        column -= 1
                        break
                    
                while True:
                    startPosition = input("Will your ship be horizontal or vertical? ")
                    if startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["horizontal", "h"]:
                        rowToChange = playerArray[row]
                        for i in range(5):
                            rowToChange[column + i] = "C"



                        playerArray[row] = rowToChange
                        displayObject.DisplayBoard(playerArray)
                        carrierset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(5):
                            playerArray[row][column] = "C"
                            row += 1
                        displayObject.DisplayBoard(playerArray)
                        carrierset = True
                        break


                    else:
                        print("Please enter a valid response.")
                        continue
            elif battleshipset == False:
                while True:
                    pbattle = input("Please enter the row and column you would like to place your 'Battleship' (row-col): ")
                    row, column = pbattle.split("-")
                    row, column = int(row), int(column)
                    if row > 10 or column > 10:
                        continue
                    else:
                        row -= 1
                        column -= 1
                        break
                    
                while True:
                    startPosition = input("Will your ship be horizontal or vertical? ")
                    if startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["horizontal", "h"]:
                        rowToChange = playerArray[row]
                        for i in range(4):
                            rowToChange[column + i] = "B"



                        playerArray[row] = rowToChange
                        displayObject.DisplayBoard(playerArray)
                        battleshipset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(4):
                            playerArray[row][column] = "B"
                            row += 1
                        displayObject.DisplayBoard(playerArray)
                        battleshipset = True
                        break
                    
                    else:
                        print("Please enter a valid response.")
                        continue
            elif cruiserset == False:
                while True:
                    pcruise = input("Please enter the row and column you would like to place your 'Cruiser' (row-col): ")
                    row, column = pcruise.split("-")
                    row, column = int(row), int(column)
                    if row > 10 or column > 10:
                        continue
                    else:
                        row -= 1
                        column -= 1
                        break
                    
                while True:
                    startPosition = input("Will your ship be horizontal or vertical? ")
                    if startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["horizontal", "h"]:
                        rowToChange = playerArray[row]
                        for i in range(3):
                            rowToChange[column + i] = "c"



                        playerArray[row] = rowToChange
                        displayObject.DisplayBoard(playerArray)
                        cruiserset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(3):
                            playerArray[row][column] = "c"
                            row += 1
                        displayObject.DisplayBoard(playerArray)
                        cruiserset = True
                        break
                    
                    else:
                        print("Please enter a valid response.")
                        continue
            
            elif submarineset == False:
                while True:
                    psub = input("Please enter the row and column you would like to place your 'Submarine' (row-col): ")
                    row, column = psub.split("-")
                    row, column = int(row), int(column)
                    if row > 10 or column > 10:
                        continue
                    else:
                        row -= 1
                        column -= 1
                        break
                    
                while True:
                    startPosition = input("Will your ship be horizontal or vertical? ")
                    if startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["horizontal", "h"]:
                        rowToChange = playerArray[row]
                        for i in range(3):
                            rowToChange[column + i] = "S"



                        playerArray[row] = rowToChange
                        displayObject.DisplayBoard(playerArray)
                        submarineset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(3):
                            playerArray[row][column] = "S"
                            row += 1
                        displayObject.DisplayBoard(playerArray)
                        submarineset = True
                        break
                    
                    else:
                        print("Please enter a valid response.")
                        continue
            elif destroyerset == False:
                while True:
                    pdes = input("Please enter the row and column you would like to place your 'Destroyer' (row-col): ")
                    row, column = pdes.split("-")
                    row, column = int(row), int(column)
                    if row > 10 or column > 10:
                        continue
                    else:
                        row -= 1
                        column -= 1
                        break
                    
                while True:
                    startPosition = input("Will your ship be horizontal or vertical? ")
                    if startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["horizontal", "h"]:
                        rowToChange = playerArray[row]
                        for i in range(2):
                            rowToChange[column + i] = "D"



                        playerArray[row] = rowToChange
                        displayObject.DisplayBoard(playerArray)
                        destroyerset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(2):
                            playerArray[row][column] = "D"
                            row += 1
                        displayObject.DisplayBoard(playerArray)
                        destroyerset = True
                        break
                    
                    else:
                        print("Please enter a valid response.")
                        continue


            continue    
        return playerArray    

            
       
            

class Display:
    def DisplayBoard(self, array):
        # Print column labels (letters A-J)
        
        # Print rows with row number and content
        for i in range(len(array)):
            print(f"{i+1:2}|", end=" ")  # Row number
            for col in array[i]:
                print(col, end=" ")
            print()  # Newline

        # Print row labels (numbers 1-10)
        print("  ", end=" ")  # Space for alignment
        for i in range(1, 11):
            print(i, end=" ")
        print()  # Newline
        print()  # Extra newline for spacing

        

class Computer:
    def __init__(self) -> None:
        pass
    def GenerateBoard(self):
        array = []
        for i in range(10):
            addlist = []
            for n in range(10):
                addlist.append(".")
            array.append(addlist)
        return array
    def SetupBoard(self, computerArray):
        ships  = []
        size = 10
        ship_sizes = [5, 4, 3, 3, 2]
        ship_symbols = ['C', 'B', 'c', 'S', 'D']  # Define symbols for different ships

        for ship_size, ship_symbol in zip(ship_sizes, ship_symbols):
            while True:
                orientation = random.choice(['horizontal', 'vertical'])  # Random orientation

                if orientation == 'horizontal':
                    x = random.randint(0, size - 1)
                    y = random.randint(0, size - ship_size)
                    positions = [(x, y+i) for i in range(ship_size)]
                else:
                    x = random.randint(0, size - ship_size)
                    y = random.randint(0, size - 1)
                    positions = [(x+i, y) for i in range(ship_size)]

                # Check if ship overlaps with existing ships
                overlap = any(pos in ships for pos in positions)

                # If no overlap, add ship to board and ships list
                if not overlap:
                    ships.extend(positions)
                    for pos in positions:
                        computerArray[pos[0]][pos[1]] = ship_symbol  # Assign ship symbol
                    break

        return computerArray


run = True

playerObject = Player()
computerObject = Computer()
displayObject = Display()
player_board = []
computer_board = []

player_board = playerObject.GenerateBoard()
computer_board = computerObject.GenerateBoard()
guess_board = playerObject.GenerateBoard()


shipSizes = [5, 4, 3, 3, 2]
                

ships = ['C', 'B', 'c', 'S', 'D']           

            
        
    

playerTurn = True
computerTurn = False
cGuesses = []
cGuessConfirmed = False



displayObject.DisplayBoard(player_board)
player_board = playerObject.SetupBoard(player_board)
print("Final Board:\n")
displayObject.DisplayBoard(player_board)
print("Computer Board:\n")
computer_board = computerObject.SetupBoard(computer_board)
displayObject.DisplayBoard(computer_board)


cCarrierSunk = False
cBattleshipSunk = False
cCruiserSunk = False
cSubmarineSunk = False
cDestroyerSunk = False


pCarrierSunk = False
pBattleshipSunk = False
pCruiserSunk = False
pSubmarineSunk = False
pDestroyerSunk = False

playerWon = False
computerWon = False

Cnum = 5
Bnum = 4
cnum = 3
Snum = 3
Dnum = 2

_Cnum = 5
_Bnum = 4
_cnum = 3
_Snum = 3
_Dnum = 2



while True:
    if playerTurn:
        playerGuess = input("What will your guess be? (row-col): ")
        row, column = playerGuess.split("-")
        row, column = int(row), int(column)
        row -= 1
        column -= 1
        if computer_board[row][column] in ships:
            guess_board[row][column] = "X"
            print("Player HIT!")
            pGuess = computer_board[row][column]
            if pGuess == "C":
                Cnum -= 1
                if Cnum == 0:
                    print("You Sunk the 'Carrier'!")
            elif pGuess == "B":
                Bnum -= 1
                if Bnum == 0:
                    print("You Sunk the 'Battleship'!")
            elif pGuess == "c":
                cnum -= 1
                if cnum == 0:
                    print("You Sunk the 'Cruiser'!")
            elif pGuess == "S":
                Snum -= 1
                if Snum == 0:
                    print("You Sunk the 'Submarine'!")
            elif pGuess == "D":
                Dnum -= 1
                if Dnum == 0:
                    print("You Sunk the 'Destroyer'!")
            if Cnum == 0 and cnum == 0 and Bnum == 0 and Snum == 0 and Dnum == 0:
                playerWon = True
                print("Congratulations!!!! You Won!!!!!")
            computer_board[row][column] = "X"
            if cDestroyerSunk and cCarrierSunk and cCruiserSunk and cSubmarineSunk and cBattleshipSunk:
                playerWon = True
                playerTurn = False
                computerTurn = False
            playerTurn = False
            computerTurn = True
            displayObject.DisplayBoard(guess_board)
            continue
            
            
                
                

        else:
            guess_board[row][column] = "m"
            print("You missed!!")
            playerTurn = False
            computerTurn = True
            displayObject.DisplayBoard(guess_board)

       
    elif computerTurn:
        while True:
            computer_guessRow = random.randint(0, 9)
            computer_guessCol = random.randint(0, 9)
            if [computer_guessRow, computer_guessCol] not in cGuesses:
                cGuesses.append([computer_guessRow, computer_guessCol])

                if player_board[computer_guessRow][computer_guessCol] in ['C', 'B', 'c', 'S', 'D']:
                    print("Computer HIT!")
                    cGuess = player_board[computer_guessRow][computer_guessCol]
                    if cGuess == "C":
                        _Cnum -= 1
                        if _Cnum == 0:
                            print("The Computer Sunk Your Carrier!")
                    elif cGuess == "c":
                        _cnum -= 1
                        if _cnum == 0:
                            print("The Computer Sunk Your Cruiser!")
                    elif cGuess == "B":
                        _Bnum -= 1
                        if _Bnum == 0:
                            print("The Computer Sunk Your Battleship!")
                    elif cGuess == "S":
                        _Snum -= 1
                        if _Snum == 0:
                            print("The Computer Sunk Your Submarine!")
                    elif cGuess == "D":
                        _Dnum -= 1
                        if _Dnum == 0:
                            print("The Computer Sunk Your Destroyer!")
                    if _Cnum == 0 and _cnum == 0 and _Snum == 0 and _Dnum == 0 and _Bnum == 0:
                        print("The Computer Wins The Game!!!")
                        computerWon = True
                        computerTurn = False
                        playerTurn = False
                    player_board[computer_guessRow][computer_guessCol] = 'X'
                    computerTurn = False
                    playerTurn = True
                    displayObject.DisplayBoard(player_board)
                else:
                    print("Computer Misses!")
                    computerTurn = False
                    playerTurn = True
                break
            elif playerTurn:
                break
            else:
                continue #Get a new Computer guess


    if computerWon or playerWon:
        break
    
    