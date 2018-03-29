## python program for optimized bubble sorting

def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        ## create a variable to keep a track of swapping
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break

    return arr

def main():
    arr = [21,32,54,21,65,23,4,68,12,4]
    arr = bubblesort(arr)
    print(arr)

if __name__ == "__main__":
    main()
