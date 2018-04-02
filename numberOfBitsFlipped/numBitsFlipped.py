

def setBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count



def calBitsFlipped(a, b):
    return setBits(a^b)



if __name__ == "__main__":
    a = 10
    b = 20
    print(calBitsFlipped(a, b))

