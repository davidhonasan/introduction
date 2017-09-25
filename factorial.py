def factorial(x):
    n = 1
    while x > 0:
        n = n * x
        x = x - 1
    print(n)

def main():
    x = int(input("Please input digits"))
    factorial(x)

main()
