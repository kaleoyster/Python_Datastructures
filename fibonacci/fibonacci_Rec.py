def fibo(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


def main():
    n = input("Enter n: ")
    print(fibo(int(n)))
if __name__ == "__main__":
    main()
