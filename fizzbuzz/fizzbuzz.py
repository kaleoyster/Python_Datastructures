## Python Fizzbuzz

def fizzbuzz(n):
    for i in range(1,n+1,1):
        if (i%3 == 0) & (i%5 == 0):
            print("FizzBuzz")
        elif (i%3 == 0):
            print("Fizz")
        elif (i%5 == 0 ):
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    n  = input("Enter number: ")
    fizzbuzz(int(n))
