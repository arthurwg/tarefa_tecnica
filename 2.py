def is_fibonacci(n):
   
    a, b = 0, 1
    
   
    if n == 0 or n == 1:
        return True
    
    
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    
    
    return False


numero = int(input("Informe um número: "))


if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
