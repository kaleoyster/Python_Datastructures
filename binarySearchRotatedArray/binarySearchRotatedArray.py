## Python an Element in a sorted and Rotated Array



def binarySearch(arr, low, high, key):
    if high < low:
        return -1
    mid = int((low + high) / 2)
     
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr,(mid+1),high,key)
    return binarySearch(arr,low,(mid-1),key)

def main():
    arr = [8,9,10,11,1,3,5,6]
    n = len(arr)
    key = 3
    print('Index of the element is:',pivotedBinary(arr, n, key))


if __name_=="__main__":
   main()
