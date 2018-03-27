def fibo(n):
    n1 = 0
    n2 = 1
    for i in range(2,n+1,1):
        temp = n1 + n2
        n1 = n2
        n2 = temp

    return n2

def main():
    n = input("Enter number: ")
    print(fibo(int(n)))

if __name__ == "__main__":
    main()

