from math import sqrt, log2
from termcolor import colored

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b

def raiz_quadrada(a):
    return sqrt(a)

def logaritmo_base2(a):
    return log2(a)

def exibir_menu():
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada (do valor atual)")
    print("6 - Logaritmo na Base 2 (do valor atual)")
    print("0 - Sair")

def formatar_resultado(resultado):
    if resultado.is_integer():
        resultado_convertido = int(resultado)
        return resultado_convertido
    
    return resultado

def colorir_resultado(resultado_formatado):
    cor_resultado = ""

    if resultado_formatado >= 0:
        cor_resultado = "green"
    else:
        cor_resultado = "red"

    resultado_colorido = colored(resultado_formatado, cor_resultado)
    return resultado_colorido

def main():
    opcoes_validas = {'1', '2', '3', '4', '5', '6', '0'}

    try:
        resultado_atual = float(input("Digite o valor inicial: "))
    except ValueError:
        print("Valor inválido.")
        return

    while True:
        resultado_formatado = formatar_resultado(resultado_atual)
        resultado_colorido = colorir_resultado(resultado_formatado)
        print(f"Valor atual: {resultado_colorido}")
        exibir_menu()

        opcao_escolhida = input("Escolha uma opção: ")

        if opcao_escolhida == '0':
            break 

        if opcao_escolhida not in opcoes_validas:
            print("\nOpção inválida. Tente novamente.")
            print("Opções válidas são: 1, 2, 3, 4, 5, 6 ou 0 para sair.\n")
            continue

        if opcao_escolhida in {"1", "2", "3", "4"}:
            try:
                valor_operacao = float(input("Digite o próximo valor do operando: "))
            except ValueError:
                print("\nValor inválido. Tente novamente.\n")
                continue
        

        if opcao_escolhida == '1':
            resultado_atual = soma(resultado_atual, valor_operacao)
        elif opcao_escolhida == '2':
            resultado_atual = subtracao(resultado_atual, valor_operacao)
        elif opcao_escolhida == '3':
            resultado_atual = multiplicacao(resultado_atual, valor_operacao)
        elif opcao_escolhida == '4':
            try:
                resultado_atual = divisao(resultado_atual, valor_operacao)
            except ZeroDivisionError:
                print("\nErro: Divisão por zero não é permitida. Tente novamente.\n")
        elif opcao_escolhida == '5':
            try:
                resultado_atual = raiz_quadrada(resultado_atual)
            except ValueError:
                print("\nErro: Não é possível calcular a raiz quadrada de um número negativo. Tente novamente.\n")
        elif opcao_escolhida == '6':
            try:
                resultado_atual = logaritmo_base2(resultado_atual)
            except ValueError:
                print("\nErro: Não é possível calcular o logaritmo na base 2 de um número não positivo. Tente novamente.\n")
        else:
            print("Opção inválida. Tente novamente.")

    print("Encerrando a calculadora. Até mais!")

main()



