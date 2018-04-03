## Python - Binary search

def bsearch(arr,l,r,s):
    if r >= l:
        mid =int (l + (r-l)/2)
        if arr[mid] == s:
            return mid
        elif arr[mid] > s:
            return bsearch(arr,l,mid-1,s)
        else:
            return bsearch(arr,mid+1,r,s)
    else:
        return -1

if __name__="__main__":
    arr = [2,2,3,4,5,6,10,40]
    s = 10
    result = bsearch(arr,0,len(arr)-1,s)
    if result != 1:
        print(result)
    else:
        print("No result")
