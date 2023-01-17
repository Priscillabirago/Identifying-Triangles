# a,b, c accepts values of the length of the sides of a trisngle
a = int(input("Enter value of the length of a side of a triangle:"))
b = int(input("Enter value of the length of a side of a triangle:"))
c = int(input("Enter value of the length of a side of a triangle:"))

# a,b, c are stored in s list
list2 = [a, b, c]
# list is arranged from descending to ascending order
list2.sort()
# the lengths are assigned to different variables based on their magnitude
max_num = list2[-1]
first = list2[0]
second = list2[1]

# checking for the condition of an equilateral triangle: all the sides are equal
if a == b == c:
    print("This is an equilateral triangle")
# checking for the condition of isosceles triangle: two of the given sides are equal
elif a == b != c or a != b == c or a == c != b:
    print("This is an isosceles triangle")
# checking if the square of the two smallest sides is equal to that of the square of the longest side
elif max_num ** 2 == first ** 2 + second **2:
    print("This is a right-angled triangle")
# checking if the magnitude of the longest side is greater than or equal to the sum of the magnitude of the other two sides
elif max_num >= first + second:
    print("This is not a triangle")
# checking if the three sides are not equal
elif a != b != c:
    print("This is a scalene triangle")

