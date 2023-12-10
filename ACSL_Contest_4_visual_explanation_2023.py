'''
Inputs:
Size: n, grid: nxn (square)
Targets: (example format) 01 20 53, where first number is row, second is column and space is dividor
which represents new target

Arrows representation:
(A): Left
(B): Up
(C): Right
(D): Down
(E): Diagonally left up
(F): Diagonally right up
(G): Diagonally right down
(H): Diagonally left down

Look through the grid using all types of arrows (shown above), and determine
the arrow that goes through the most targets without touching an empty space

This is a visual to show how the code works
'''

import time

print("Welcome to a visual representation of the ACSL Contest #4 Problem 2023. \
Starting with given dimensions and coordinates of 'targets', the goal of the \
program is to find the best possible placement of arrow which goes through \
the most targets. There are 8 types of arrows, namely: \n\
\n\
(A): Left\n\
(B): Up\n\
(C): Right\n\
(D): Down\n\
(E): Diagonally left up\n\
(F): Diagonally right up\n\
(G): Diagonally right down\n\
(H): Diagonally left down\n\
\n\
The 8 arrows will be compared and placed in all border squares, namely \
the outer squares. Targets are not allowed to be in border squares, and \
arrows can only be in border squares. Therefore, the maximum dimension size \
is 3. Coordinates are represented through \rowcolumn, with no space between \
the row number and the column number. This is done for easier accessibility \
in code. In the name of a tie, the minimum value of the coordinate in ASCII \
code is taken as the result. Lets get started!\n\n")

#Define A arrow path (Left)
def A_arrow(coordinate, dict, size, totalList):
    score = 0
    columnnum = coordinate[1]
    
    #Checks which border columns are usable for A-type arrow
    if (coordinate[0] != 0 and coordinate[0] != size-1 and coordinate[1] == size-1 and coordinate[1] != 0):
        for coordinates in range(size-1):
            #Keep track of current coordinate
            currentCoord = (coordinate[0],columnnum)
            columnnum -= 1
            
            if dict[currentCoord] == 1:
                score += 1
                
                #Check if next spot is a target (if not then break)
                if dict[(currentCoord[0], currentCoord[1]-1)] == 0:
                    break
                
        result = f'{score},{coordinate[0]}{coordinate[1]}A'
        if score > 0:
            totalList.append(result)
    else:
        pass

#Define B arrow path (Up)
def B_arrow(coordinate, dict, size, totalList):
    score = 0
    rownum = coordinate[0]
    
    #Checks which border columns are usable for B-type arrow
    if (coordinate[0] != 0 and coordinate[0] == size-1 and coordinate[1] != 0 and coordinate[1] != size-1):
        for coordinates in range(size-1):
            #Keep track of current coordinate
            currentCoord = (rownum,coordinate[1])
            rownum -= 1
            
            if dict[currentCoord] == 1:
                score += 1
                
                #Check if next spot is a target (if not then break)
                if dict[(currentCoord[0]-1, currentCoord[1])] == 0:
                    break
                
        result = f'{score},{coordinate[0]}{coordinate[1]}B'
        if score > 0:
            totalList.append(result)
    else:
        pass

#Define C arrow path (Right)
def C_arrow(coordinate, dict, size, totalList):
    score = 0
    columnnum = coordinate[1]
    
    #Checks which border columns are usable for C-type arrow
    if (coordinate[0] != 0 and coordinate[0] != size-1 and coordinate[1] != size-1 and coordinate[1] == 0):
        for coordinates in range(size-1):
            #Keep track of current coordinate
            currentCoord = (coordinate[0],columnnum)
            columnnum += 1
            
            if dict[currentCoord] == 1:
                score += 1
                
                #Check if next spot is a target (if not then break)
                if dict[(currentCoord[0], currentCoord[1]+1)] == 0:
                    break
                
        result = f'{score},{coordinate[0]}{coordinate[1]}C'
        if score > 0:
            totalList.append(result)
    else:
        pass

#Define D arrow path (Down)
def D_arrow(coordinate, dict, size, totalList):
    score = 0
    rownum = coordinate[0]
    
    #Checks which border columns are usable for D-type arrow
    if (coordinate[0] == 0 and coordinate[0] != size-1 and coordinate[1] != 0 and coordinate[1] != size-1):
        for coordinates in range(size-1):
            #Keep track of current coordinate
            currentCoord = (rownum,coordinate[1])
            rownum += 1
            
            if dict[currentCoord] == 1:
                score += 1
                
                #Check if next spot is a target (if not then break)
                if dict[(currentCoord[0]+1, currentCoord[1])] == 0:
                    break
        result = f'{score},{coordinate[0]}{coordinate[1]}D'
        if score > 0:
            totalList.append(result)
    else:
        pass

#Define E arrow path (Diagonally Left Up)
def E_arrow(coordinate, dict, size, list, totalList):
    score = 0
    rownum = coordinate[0]
    columnnum = coordinate[1]
    
    #Checks which border columns are usable for E-type arrow
    if (coordinate[0] != 0 and coordinate[1] != 0):
        for coordinates in range(size-1):
            #Keep track of current coordinate
            currentCoord = (rownum,columnnum)
            rownum -= 1
            columnnum -= 1
        
            if currentCoord in dict:
                if dict[currentCoord] == 1:
                    score += 1
                    
                    #(Try) if next spot is a target (if not then break)
                    try:
                        if (dict[(currentCoord[0]-1, currentCoord[1]-1)] == 0 or (currentCoord[0]-1, currentCoord[1]-1) in list):
                            break
                        
                    except KeyError:
                        break
            else:
                break
        result = f'{score},{coordinate[0]}{coordinate[1]}E'
        if score > 0:
            totalList.append(result)
    else:
        pass

#Define F arrow path (Diagonally Right Up)
def F_arrow(coordinate, dict, size, list, totalList):
    score = 0
    rownum = coordinate[0]
    columnnum = coordinate[1]
    
    #Checks which border columns are usable for F-type arrow
    if (coordinate[0] != 0 and coordinate[1] != size-1):
        for coordinates in range(size-1):
            #Keep track of current coordinate
            currentCoord = (rownum,columnnum)
            rownum -= 1
            columnnum += 1
        
            if currentCoord in dict:
                if dict[currentCoord] == 1:
                    score += 1
                    
                    #(Try) if next spot is a target (if not then break)
                    try:
                        if (dict[(currentCoord[0]-1, currentCoord[1]+1)] == 0 or (currentCoord[0]-1, currentCoord[1]+1) in list):
                            break
                    except KeyError:
                        break
            else:
                break
        result = f'{score},{coordinate[0]}{coordinate[1]}F'
        if score > 0:
            totalList.append(result)
    else:
        pass

#Define G arrow path (Diagonally Right Down)
def G_arrow(coordinate, dict, size, list, totalList):
    score = 0
    rownum = coordinate[0]
    columnnum = coordinate[1]
    
    #Checks which border columns are usable for G-type arrow
    if (coordinate[0] != size-1 and coordinate[1] != size-1):
        for coordinates in range(size-1):
            #Keep track of current coordinate
            currentCoord = (rownum,columnnum)
            rownum += 1
            columnnum += 1
        
            if currentCoord in dict:
                if dict[currentCoord] == 1:
                    score += 1
                    
                    #(Try) if next spot is a target (if not then break)
                    try:
                        if (dict[(currentCoord[0]+1, currentCoord[1]+1)] == 0 or (currentCoord[0]+1, currentCoord[1]+1) in list):
                            break   
                    except KeyError:
                        break
            else:
                break
        result = f'{score},{coordinate[0]}{coordinate[1]}G'
        if score > 0:
            totalList.append(result)
    else:
        pass

#Define H arrow path (Diagonally Left Down)
def H_arrow(coordinate, dict, size, list, totalList):
    score = 0
    rownum = coordinate[0]
    columnnum = coordinate[1]
    
    #Checks which border columns are usable for H-type arrow
    if (coordinate[0] != size-1 and coordinate[1] != 0):
        for coordinates in range(size-1):
            #Keep track of current coordinate
            currentCoord = (rownum,columnnum)
            rownum += 1
            columnnum -= 1
        
            if currentCoord in dict:
                if dict[currentCoord] == 1:
                    score += 1
                    
                    #(Try) if next spot is a target (if not then break)
                    try:
                        if (dict[(currentCoord[0]+1, currentCoord[1]-1)] == 0 or (currentCoord[0]+1, currentCoord[1]-1) in list):
                            break   
                    except KeyError:
                        break
            else:
                break
        result = f'{score},{coordinate[0]}{coordinate[1]}H'
        if score > 0:
            totalList.append(result)
    else:
        pass


def drawBoard(board,size):
    print()
    print(' ', end='')
    for x in range(size):
        print('   %s ' % x, end='')
    print()

    print('  +────+' + ('────+' * (size - 1)))

    rowcount = 0
    for y in range(size):

        print(f'{rowcount} |', end='')
        for x in range(size):
            if board[y][x] == '🎯':
                print(' %s |' % board[y][x], end='')
            else:
                print('%s|' % board[y][x], end='')
        print()

        rowcount +=1
        print('  +────+' + ('────+' * (size - 1)))

def arrowForMostTargets(size, targets):
    #Create dictionary-matrix of coordinates to depict the grid
    coordDict = {}
    arrowPlacement = []
    finalCoordList = []
    coordList = []
    scoreList = []
    totalList = []
    coordValueList = []

    left = '🡰'
    up = '🡱'
    right = '🡲'
    down = '🡳'
    DLU = '🡴'
    DRU = '🡵'
    DRD = '🡶'
    DLD = '🡷'
    
    #Construct matrix with 0s representing empty space
    for row in range(size):
        appendList = []
        for column in range(size):
            appendList.append('    ')
            coordDict[(row,column)] = 0
        coordValueList.append(appendList)

    #Replace coordinates of the targets with 1s
    for coordinate in targets.split(' '):
        coordDict[(int(coordinate[0]),int(coordinate[1]))] = 1
        coordValueList[int(coordinate[0])][int(coordinate[1])] = '🎯'

    drawBoard(coordValueList, size)
    
    for arrowCoord in coordDict:
        if arrowCoord[0] == 0:
            arrowPlacement.append(arrowCoord)
        elif (arrowCoord[1] == 0 and arrowCoord[0] != 0 and arrowCoord[0] != (size-1)):
            arrowPlacement.append(arrowCoord)
        elif arrowCoord[0] == (size-1):
            arrowPlacement.append(arrowCoord)
        elif (arrowCoord[1] == (size-1) and arrowCoord[0] != 0 and arrowCoord[0] != (size-1)):
            arrowPlacement.append(arrowCoord)

    for placement in arrowPlacement:
        A_arrow(placement,coordDict,size, totalList)
        B_arrow(placement,coordDict,size, totalList)
        C_arrow(placement,coordDict,size, totalList)
        D_arrow(placement,coordDict,size, totalList)
        E_arrow(placement,coordDict,size,arrowPlacement, totalList)
        F_arrow(placement,coordDict,size,arrowPlacement, totalList)
        G_arrow(placement,coordDict,size,arrowPlacement, totalList)
        H_arrow(placement,coordDict,size,arrowPlacement, totalList)

    for value in totalList:
        scoreValue = value.split(',')[0]
        coordValue = value.split(',')[1]
        scoreList.append(scoreValue)
        coordList.append(coordValue)

    for maxValue in range(len(scoreList)):
        if max(scoreList) == scoreList[maxValue]:
            finalCoordList.append(coordList[maxValue])
            
    tPlot = []
    answer = min(finalCoordList)
    
    printVal = f'The best arrow placement would be {answer}, where \
{answer[0]} and {answer[1]} are the coordinates of the arrow (row and column),\
 and {answer[2]} is the type of the arrow.'
    resultVal = f'{answer}'
    for i in resultVal:
        tPlot.append(i)

    if tPlot[2] == 'A':
        coordValueList[int(tPlot[0])][int(tPlot[1])] = f' {left}  '
    elif tPlot[2] == 'B':
        coordValueList[int(tPlot[0])][int(tPlot[1])] = f' {up}  '
    elif tPlot[2] == 'C':
        coordValueList[int(tPlot[0])][int(tPlot[1])] = f' {right}  '
    elif tPlot[2] == 'D':
        coordValueList[int(tPlot[0])][int(tPlot[1])] = f' {down}  '
    elif tPlot[2] == 'E':
        coordValueList[int(tPlot[0])][int(tPlot[1])] = f' {DLU}  '
    elif tPlot[2] == 'F':
        coordValueList[int(tPlot[0])][int(tPlot[1])] = f' {DRU}  '
    elif tPlot[2] == 'G':
        coordValueList[int(tPlot[0])][int(tPlot[1])] = f' {DRD}  '
    elif tPlot[2] == 'H':
        coordValueList[int(tPlot[0])][int(tPlot[1])] = f' {DLD}  '

    solve = str(input("\n\nWould you like to see the answer? "))
    followUp = ''
    while True:
        if (solve.startswith('y') or solve.startswith('s') or followUp.startswith('y') or followUp.startswith('s')):
            print('\n')
            drawBoard(coordValueList, size)
            break
        
        else:
            print('\nYou have chosen to not see the answer. Please enter how many seconds until next follow-up below.')
            numSeconds = int(input())
            time.sleep(numSeconds)
            followUp = str(input("\n\nWould you like to see the answer now? "))
            
    print(f'\n{printVal}')

while True:
    emptyGraph = []
    while True:
        dimension = int(input('\nPlease enter the side length of the graph: '))
        if 3 <= dimension <= 10:
            break
        else:
            print('Invalid dimension size')
        
    for row in range(dimension):
            appendEmptyList = []
            for column in range(dimension):
                appendEmptyList.append('    ')
            emptyGraph.append(appendEmptyList)

    drawBoard(emptyGraph,dimension)

    numTargets = int(input('\nPlease enter the number of targets: '))

    targets = ''
    count = 1
    for target in range(numTargets):
        targetCoord = str(input("\nPlease enter target coordinate in form \
row,column without parenthesis, spaces and commas: "))
            
        if count < numTargets:
            targets += f'{targetCoord[0]}{targetCoord[1]} '
        else:
            targets += f'{targetCoord[0]}{targetCoord[1]}'
            
        count += 1

    print(targets)

    print('\nHere is the graph:\n')

    arrowForMostTargets(dimension, targets)
    
    print('\nWould you like to enter a new graph?')
    Again = input()

    if (Again.startswith('y') or Again.startswith('s')):
        continue
    else:
        print('\nYou have chosen to stop the program.')
        break
