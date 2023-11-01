#Print Function 
#The included code stub will read an integer,n, from STDIN.

#Without using any string methods, try to print the following: 123..n

if __name__ == '__main__':
    n = int(input())

    if n <=0:
        print("The input number is too small.")
    else:
        print(*range(1, n + 1), sep='')
