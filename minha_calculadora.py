def soma(a, b):
    return a + b

def subtracao(a,b):
    return a - b

def main():
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    print(f"A soma de {x} e {y} é {soma(x, y)}")
    print(f"A subtração de {x} e {y} é {subtracao(x, y)}")

main()