"""
Task 1
Write a Python program to detect the number of local variables declared in a function.
"""
def fun() :
    x = 1
    y = 2



if __name__ == "__main__":
    print(fun.__code__.co_nlocals)



"""
Task 2
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""


def say_hi(day_part):
    def name_formating(name):
        return f" Good {day_part},  {name.title()} !!!!"

    return name_formating


if __name__ == "__main__":
    print(say_hi("morning")("ivanka"))


"""
Task 3
Write a function called `choose_func` which takes a list of nums and 2 callback functions. If all nums inside the list 
are positive, execute the first function on that list and return the result of it. Otherwise, return the result of 
the second one
def choose_func(nums: list, func1, func2):
    pass
# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
"""


def choose_func(nums: list, func1, func2):
    if [x for x in nums if x < 0]:
        return func2(nums)
    else:
        return func1(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    print(choose_func(nums1, square_nums, remove_negatives))
    print(choose_func(nums2, square_nums, remove_negatives))
