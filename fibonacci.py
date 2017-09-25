stacks = []
def fibo(x):
    a, b = 0, 1
    while b < x:
        a = a + b
        b = b + a
        stacks.append(a)
        stacks.append(b)

def main():
    x = int(input())
    fibo(x)
    print(stacks)

main()