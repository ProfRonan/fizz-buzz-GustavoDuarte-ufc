a = int(input())
b = a % 3
c = a % 5

if b == 0:
    print('Fizz')
elif c == 0:
    print('Buzz')
elif b == 0 and c == 0:
    print('FizzBuzz')
else:
    print(a)