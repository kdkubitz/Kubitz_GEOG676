def print_vertically(a, b, c, n):
        count = 3
        print(a)
        print(b)
        while count <= n:
                print(c)
                a = b
                b = c
                c = (a + b)
                count += 1
a = 1
b = 1
c = (a + b)
n = int(input("Choose an nth number in the sequence."))
print_vertically(a, b, c, 100)

def print_horizontally(a, b, c, n):
        count = 3
        fib_seq = []
        fib_seq.append(a)
        fib_seq.append(b)

        while count <= n:
                fib_seq.append(c)
                a = b
                b = c
                c = (a + b)
                count += 1
        
        print(fib_seq)

print_horizontally(a, b, c, 7)