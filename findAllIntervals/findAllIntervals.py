## Python Program to all the intervals with any sudden increase.
## If there is a sudden increase then we split that time interval into two

def findAllIntervals(lst):
    fList = []
    temp = []
    i = 0
    j = 1
    for k in lst:
        if j == len(lst):
            temp.append(lst[i])
            fList.append(temp)
            return (fList,len(fList))
        if lst[i] == lst[j]:
            pass
        temp.append(lst[i])
        if lst[i] < lst[j]:
            diff = lst[j] - lst[i]
            if diff > 1:
               #break
               fList.append(temp)
               temp = []
            pass
        i = i + 1
        j = j + 1
    

if __name__=='__main__':
    lst = [9,8,7,6,6,6,7,6,8,4,6,5,5,4]
    intList, intervals = findAllIntervals(lst)
    print(intList[0])
    print(intList[1])
    print(intList[2])
