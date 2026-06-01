def fibonacci(n):
    if n <=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

term =5

print(f"fibonacci series up to {term} terms")
for i in range(term):
    print(fibonacci(i), end=" ")
    
