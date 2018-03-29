## Python Program to bubble sort

def bubbleSort(Arr):
    for i in range(len(Arr)):
        for j in range(0,len(Arr)-1,1):
            if Arr[j]>Arr[j+1]:
                Arr[j], Arr[j+1] = Arr[j+1], Arr[j]
    return Arr



if __name__=="__main__":
    array = [32,321,43,654,76,2,3]
    sortedArr = bubbleSort(array)

    print("sorted array is:" )
    for i in sortedArr:
        print(i)

