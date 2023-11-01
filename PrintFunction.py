if __name__ == '__main__':
    n = int(input())

    if n <=0:
        print("The input number is too small.")
    else:
        print(*range(1, n + 1), sep='')