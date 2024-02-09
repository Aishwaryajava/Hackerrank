def is_leap(year):
    leap = False
    
    #if year is divisible by 4 
    if year % 4 ==0: 
        leap = True
    #if year is divisible by 100
        if year % 100 ==0:
            leap = True
    #if year is divisible by 400
            if year % 400 ==0:
                leap = True
    else: 
        leap = False
   
    return leap

year = int(input())
print(is_leap(year))