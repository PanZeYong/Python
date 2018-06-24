from time import time

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

squares = [value ** 2 for value in range(11, 20)]
print(squares)

for value in range(1, 21):
    print(value)

numbers = list(range(1, 1000001))
# for value in numbers:
#     print(value)
print(min(numbers))
print(max(numbers))

start = time()
print(sum(numbers))
end = time()
print(end - start)

numbers = list(range(1, 21, 2))
for value in numbers:
    print(value)

values = list(range(3, 31, 3))
for value in values:
    print(value)

values = [ value ** 3 for value in range(1, 11)]
print(values)