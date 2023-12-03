
numbers = []
print(numbers)
strings = []
print(strings)
names = ["John", "Eric", "Jessica"]

second_name = None
print("The second name on the names list is %s" % second_name)

# Arithmetic Operators
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squeared = 7 ** 2
cubed = 2 ** 3
print(squeared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

hels = "hello" * 10
print(hels)


even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1, 2, 3] * 3)

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list містить %d об'єктів" % len(x_list))
print("y_list містить %d об'єктів" % len(y_list))
print("big_list містить %d об'єктів" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Майже готово...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")