## program to chunk a list into specified number

def chunk(arr, n):
    k =[arr[i:i+n]for i in range(0,len(arr),n)]
    return k

if __name__=="__main__":
   arr = [1,2,3,4,5,6]
   size = 2
   print(chunk(arr, size))
