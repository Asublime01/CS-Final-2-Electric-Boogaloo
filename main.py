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
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
                        carrierset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(5):
                            playerArray[row][column] = "C"
                            row += 1
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
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
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
                        battleshipset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(4):
                            playerArray[row][column] = "B"
                            row += 1
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
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
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
                        cruiserset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(3):
                            playerArray[row][column] = "c"
                            row += 1
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
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
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
                        submarineset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(3):
                            playerArray[row][column] = "S"
                            row += 1
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
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
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
                        destroyerset = True
                        break

                    elif startPosition.lower() in ["horizontal", "vertical", "h", "v"] and startPosition in ["vertical", "v"]: 
                        for i in range(2):
                            playerArray[row][column] = "D"
                            row += 1
                        for row in playerArray:
                            for col in row:
                                print(col, end=" ")
                            print()
                        print()
                        destroyerset = True
                        break
                    
                    else:
                        print("Please enter a valid response.")
                        continue


            continue    
        return playerArray    

            
       
            

class Display:
    def DisplayBoard(self, array):
        for row in array:
            for col in row:
                print(col, end=" ")
            print()
        print()
        

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




while True:
    if playerTurn:
        playerGuess = input("What will your guess be? (row-col): ")
        row, column = playerGuess.split("-")
        row, column = int(row), int(column)
        row -= 1
        column -= 1
        if computer_board[row][column] in ships:
            guess_board[row][column] = "X"
            computer_board[row][column] = "X"
            print("Player HIT!")
            if computer_board[row][column] == "C":
                shipCount = 0
                for row in computer_board:
                    for value in row:
                        if value == "C":
                            shipCount += 1
                if shipCount == 0:
                    cCarrierSunk = True
                    print("You Sunk the Computer's Carrier!")
            elif computer_board[row][column] == "c":
                shipCount = 0
                for row in computer_board:
                    for value in row:
                        if value == "c":
                            shipCount += 1
                if shipCount == 0:
                    cCruiserSunk = True
                    print("You Sunk the Computer's Cruiser!")
            elif computer_board[row][column] == "S":
                shipCount = 0
                for row in computer_board:
                    for value in row:
                        if value == "S":
                            shipCount += 1
                if shipCount == 0:
                    cSubmarineSunk = True
                    print("You Sunk the Computer's Submarine!")
            elif computer_board[row][column] == "B":
                shipCount = 0
                for row in computer_board:
                    for value in row:
                        if value == "B":
                            shipCount += 1
                if shipCount == 0:
                    cBattleshipSunk = True
                    print("You Sunk the Computer's Battleship!")
            elif computer_board[row][column] == "D":
                shipCount = 0
                for row in computer_board:
                    for value in row:
                        if value == "D":
                            shipCount += 1
                if shipCount == 0:
                    cDestroyerSunk = True
                    print("You Sunk the Computer's Destroyer!")
            elif cDestroyerSunk and cCarrierSunk and cCruiserSunk and cSubmarineSunk and cBattleshipSunk:
                playerWon = True
            playerTurn = False
            computerTurn = True
            displayObject.DisplayBoard(guess_board)
            
                
                

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
                    player_board[computer_guessRow][computer_guessCol] = 'X'
                    print("Computer HIT!")

                    # Update player's ship sunk status
                    if player_board[computer_guessRow][computer_guessCol] == "C":
                        shipCount = sum(row.count("C") for row in player_board)
                        if shipCount == 0:
                            pCarrierSunk = True
                            print("Computer Sunk your Carrier!")
                    elif player_board[computer_guessRow][computer_guessCol] == "c":
                        shipCount = sum(row.count("c") for row in player_board)
                        if shipCount == 0:
                            pCruiserSunk = True
                            print("Computer Sunk your Cruiser!")
                    elif player_board[computer_guessRow][computer_guessCol] == "S":
                        shipCount = sum(row.count("S") for row in player_board)
                        if shipCount == 0:
                            pSubmarineSunk = True
                            print("Computer Sunk your Submarine!")
                    elif player_board[computer_guessRow][computer_guessCol] == "B":
                        shipCount = sum(row.count("B") for row in player_board)
                        if shipCount == 0:
                            pBattleshipSunk = True
                            print("Computer Sunk your Battleship!")
                    elif player_board[computer_guessRow][computer_guessCol] == "D":
                        shipCount = sum(row.count("D") for row in player_board)
                        if shipCount == 0:
                            pDestroyerSunk = True
                            print("Computer Sunk your Destroyer!")

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
    
    
        