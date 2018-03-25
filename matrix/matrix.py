## Python program to convert integer N and converts N X N matrix
## matrix(2) = [[1,2],[4,3]]
## matrix(3) =   [[1,2,3],
##                [8,9,4],
##                [7,6,5]]


def matrix(n):
    n = int(n)
    result = []
    for i in range(0,n+1,1):
        result.append([])
    
    counter = 1
    startColumn = 0
    endColumn = n - 1
    startRow = 0
    endRow = n - 1
    
    while (startColumn <= endColumn) & (startRow <= endRow):
        ## top row 
        for i in range(startColumn,endColumn,1):
            result[startRow][i] = counter
            counter = counter + 1
        startRow = startRow + 1
      
        ## Right column
        for i in range(startRow, endRow,1):
            result[i][endColumn] = counter
            counter = counter + 1
        endColumn = endColumn - 1
        
        ## Bottom Row
        for i in range(endColumn, startColumn, -1):
            result[endRow][i] = counter
            counter = counter + 1
        endRow = endRow - 1
       
        # start column
        for  i in range(endRow, startRow, -1):
             result[i][startColumn] = counter
             counter = counter + 1
        startColumn = startColumn + 1

    return result


if __name__ == "__main__":
    n = input('Enter N : ')
    print(matrix(n))

