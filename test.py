import math
a = int()
b = int()
c = int()
def main():
    get_input()
    check()
    calculate()
def get_input():
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
    c = int(input("Enter 3rd number:"))
    return a,b,c
def check():
    if a == 0:
        print("a must not be 0")
        get_input()
    else:
        print("your quadratic equation is:", a ,"x^2 +", b ,"x +", c ,"= 0")
def calculate():
    dis = (b**2) - (4*a*c)
    if dis == 0:
        x12 = -b / 2*a 
        print("Because your discriminant = 0. Your equation has both same of solution x1 = x2 =", x12)
    elif dis > 0:
        x1 = (-b + sqrt(dis))/ 2*a
        x2 = (-b - sqrt(dis))/ 2*a
        print("Your equation has two distinct solutions")
        print("x1=", x1)
        print("x2=", x2)
    else:
        calculate()


main()
