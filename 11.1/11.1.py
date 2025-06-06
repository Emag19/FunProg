#11.1

def QuadradoElementos(numeros):
    return[x**2 for x in numeros]

def SomatorioLista(numeros):
    return sum(numeros)

def ConverteEmNumeros(ListaCaracteres):
    return [float(x) for x in ListaCaracteres if x.strip()]

def main():
    print("Qual o nome do ficheiro? (escreva o tipo de ficheiro no final")
    nome = input()
    with open(nome, "r") as txt:
        linhas = txt.readlines()
        numeros = ConverteEmNumeros(linhas)
        quadrados = QuadradoElementos(numeros)
        soma = SomatorioLista(quadrados)
    
    print("A soma dos quadrados dos números é:", soma)

main()
    
    