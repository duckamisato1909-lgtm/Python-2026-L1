import math

# 1
def ex1():
    radius_str = input("Enter circle radius? ")
    radius = float(radius_str)
    area = 3.14 * (radius ** 2)
    print(f"Circle area = {area}")

# 2
def ex2():
    celsius = float(input("Enter the temperature in Celsius? "))
    fahrenheit = celsius * 1.8 + 32
    c_display = int(celsius) if celsius.is_integer() else celsius
    print(f"{c_display} (C) = {fahrenheit:.1f} (F)")

# 3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ex3():
    num = int(input("Enter a number? "))
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is a NOT prime number")

# 4
def is_perfect(n):
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def ex4():
    num = int(input("Enter a number? "))
    if is_perfect(num):
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is a NOT perfect number")

# 5
def ex5():
    colors = ["Blue", "Yellow", "Black", "Red", "White"]
    fav_color = input("What is your favorite color? ")
    if fav_color in colors:
        print(f"Your colod is at index {colors.index(fav_color)} in my list")
    else:
        print("Sorry, I could not find your color")

# 6
def ex6():
    range1 = list(range(0, 7))
    range2 = list(range(1, 11, 3))
    range3 = list(range(5, 0, -1))
    range4 = list(range(6, -3, -2))
    print("range1:", ", ".join(map(str, range1)))
    print("range2:", ", ".join(map(str, range2)))
    print("range3:", ", ".join(map(str, range3)))
    print("range4:", ", ".join(map(str, range4)))

# 7
def remove_dollar_sign(s):
    return s.replace("$", "")

# 8
def extract_even(l):
    return [x for x in l if x % 2 == 0]

# 9
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 10
def get_divisors(n):
    if n == 0:
        return []
    n = abs(n)
    return [i for i in range(1, n + 1) if n % i == 0]

# 11
def compute_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def ex11():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    dist = compute_distance(x1, y1, x2, y2)
    print(f"Distance between points = {dist}")

# 12
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print(" ".join(["*"] * n))
        else:
            print("*" + " " * (2 * n - 3) + "*") 


if __name__ == "__main__":
    print("# 1")
    ex1()
    
    print("\n# 2")
    ex2()
    
    print("\n# 3")
    ex3()
    
    print("\n# 4")
    ex4()
    
    print("\n# 5")
    ex5()
    
    print("\n# 6")
    ex6()
    
    print("\n# 7")
    print(remove_dollar_sign("$100 is equal to 100$"))
    
    print("\n# 8")
    sample_list = [1, 4, 5, -1, 10]
    print(extract_even(sample_list))
    
    print("\n# 9")
    print(factorial(5))
    
    print("\n# 10")
    print(get_divisors(12))
    
    print("\n# 11")
    ex11()
    
    print("\n# 12")
    print_pattern(4, 5)