from operator import add
#import sys

def printMatrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])

#Dim-Input from user
while True:
    try:
        row = int(input("Number of rows: "))
        break
    except ValueError:
        print("ERROR: Not a valid number")

while True:
    try:
        col = int(input("Number of columns: "))
        break
    except ValueError:
        print("ERROR: Not a valid number")

#Check for invalid dimensions (These shouldn't actually be invalid, with proper functionality)
#if row > col:
#    sys.exit("ERROR: Invalid dimensions")

#Element-Input from user
matrix = []
for i in range(0, row):
    while True:
        try:
            tempRowList = [int(x) for x in (input("Values of row {}, seperated with spaces: ".format(i + 1)).split())[:col]]
            break
        except ValueError:
            print("Not valid input")
    matrix.append(tempRowList)

#Print original matrix
printMatrix(matrix)

oMatrix = list(matrix)

#Checking for Zeroes; if there is a zero where there should be piv-element, it performs a row-swap

j = 0
while j != row:
    if matrix[j][j] == 0:
        matrix[j - 1], matrix[j] = matrix[j], matrix[j - 1]
    else:
        j += 1

#"Gaussing" downwards
t = 0
j = 1
l = 0

for x in range(0, row - 1):
    while t != row - 1:
        k = -matrix[j][l] / matrix[l][l]
        prevRowTemp = [i * k for i in matrix[l]]
        matrix[j] = list(map(add, matrix[j], prevRowTemp))

        t += 1
        j += 1
    t -= 1
    j -= 1
    l += 1

#"Gaussing" upwards
t = row - 1
j = row - 2
l = row - 1
for x in range(row - 1, 0, - 1):
    while t != 0:
        k = -matrix[j][l] / matrix[l][l]
        prevRowTemp = [i * k for i in matrix[l]]
        matrix[j] = list(map(add, matrix[j], prevRowTemp))

        j -= 1
        t -= 1
    t += 1
    j += 1
    l -= 1

#Fine tuning. Making sure that the pivot elements are equal to one
for x in range(0, row):
    if matrix[x][x] != 1:    
        matrix[x] = [i / matrix[x][x] for i in matrix[x]]   

print("The matrix in row echelon form:")
printMatrix(matrix)
