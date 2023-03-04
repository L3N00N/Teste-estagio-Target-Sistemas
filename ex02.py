# solicita um número ao usuário
numero = int(input("Digite um número: "))

# verifica se o número está na sequência de Fibonacci
a, b = 0, 1
while b < numero:
    a, b = b, a + b
if b == numero:
    print(numero, "está na sequência de Fibonacci!")
else:
    print(numero, "não está na sequência de Fibonacci.")