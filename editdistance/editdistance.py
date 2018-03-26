## python program for edit distance
def editDistance(str1,str2,m,n):
    # check for empty string
    if m == 0:
        return n

    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return editDistance(str1,str2,m-1, n-1)

    return 1 + min(editDistance(str1, str2, m, n-1),   #insert
                   editDistance(str1, str2, m-1, n),   #remove 
                   editDistance(str1, str2, m-1, n-1)  #replace
                  )
    
                     
def main():
    string1 = 'sunday'
    string2 = 'saturday'
    print(editDistance(string1,string2,len(string1),len(string2)))



if __name__=='__main__':
    main()
