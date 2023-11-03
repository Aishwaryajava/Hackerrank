#The provided code stub reads and integer,n , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# solution 1 
if __name__ == '__main__':
    n = int(input())

def square(n):
  return n * n

# Create a range of numbers from 0 to 5
numbers = range(0,n)

# Square each number in the range and print the result
for number in numbers:
  print(square(number))

#solution 2  List Comprehension method
if __name__ == '__main__':
    n = int(input())
    squares = [n**2 for n in range(n) if n >= 0]
    print(*squares, sep='\n')

#solution 3 
for i in range(0,n):
    print(i*i)
      



