def is_leap(year):
    leap = False
    if year % 4 == 0:  # Check if the year is divisible by 4
        if year % 100 == 0:  # Check if the year is divisible by 100
            if year % 400 == 0:  # Check if the year is divisible by 400
                return True  # Leap year if divisible by 400
            else:
                return False  # Not a leap year if divisible by 100 but not by 400
        else:
            return True  # Leap year if divisible by 4 but not by 100
    else:
        return False  # Not a leap year if not divisible by 4

    return leap

year = int(input())
print(is_leap(year))
