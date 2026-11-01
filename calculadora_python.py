import math

print('Bem-Vindo ao Mycalculator\n')


def mostrar_menu():
    print('[Menu] -> Selecione uma das operações abaixo:')
    print('[1] Adição')
    print('[2] Subtração')
    print('[3] Multiplicação')
    print('[4] Divisão')
    print('[5] Potência')
    print('[6] Raiz quadrada')
    print('[7] Porcentagem')
    print('[8] Fatorial')
    print('[9] Ajuda')
    print('[0] Sair\n')


def ler_numeros(mensagem):
    """Lê números separados por espaço e devolve uma lista de floats."""
    numeros = input(mensagem)
    return [float(n) for n in numeros.split()]  # split() sem argumento separa pelos espaços


def formatar(valor):
    """Mostra 5 em vez de 5.0 quando o número é inteiro."""
    return int(valor) if valor == int(valor) else valor


while True:  # o loop só para quando o usuário escolhe 0
    mostrar_menu()
    try:
        opcao = int(input('Operação: '))
    except ValueError:
        print('Opção inválida. Digite um número de 0 a 9.\n')
        continue

    try:
        if opcao == 1:  # adição
            print('\n[ADIÇÃO]')
            lista_valores = ler_numeros('Digite os números que deseja somar: ')
            soma = 0  # elemento neutro da soma
            for numero in lista_valores:
                soma += numero
            print(f'Resultado: {formatar(soma)}\n')

        elif opcao == 2:  # subtração
            print('\n[SUBTRAÇÃO]')
            lista_valores = ler_numeros('Digite os números que deseja subtrair: ')
            subtracao = lista_valores[0]  # começa pelo primeiro valor
            for i in range(1, len(lista_valores)):  # subtrai a partir do segundo
                subtracao -= lista_valores[i]
            print(f'Resultado: {formatar(subtracao)}\n')

        elif opcao == 3:  # multiplicação
            print('\n[MULTIPLICAÇÃO]')
            lista_valores = ler_numeros('Digite os números que deseja multiplicar: ')
            multiplicacao = 1  # elemento neutro da multiplicação
            for numero in lista_valores:
                multiplicacao *= numero
            print(f'Resultado: {formatar(multiplicacao)}\n')

        elif opcao == 4:  # divisão
            print('\n[DIVISÃO]')
            lista_valores = ler_numeros('Digite o dividendo e o divisor: ')
            if lista_valores[1] == 0:
                print('Impossível realizar divisão por zero. Tente novamente.\n')
            else:
                divisao = lista_valores[0] // lista_valores[1]
                resto = lista_valores[0] % lista_valores[1]
                print(f'Resultado: {formatar(divisao)} e resto: {formatar(resto)}\n')

        elif opcao == 5:  # potência
            print('\n[POTÊNCIA]')
            lista_valores = ler_numeros('Digite a base e o expoente: ')
            print(f'Resultado: {formatar(lista_valores[0] ** lista_valores[1])}\n')

        elif opcao == 6:  # raiz quadrada
            print('\n[RAIZ QUADRADA]')
            numero = float(input('Digite o número: '))
            if numero < 0:
                print('Não existe raiz quadrada real de número negativo.\n')
            else:
                print(f'Resultado: {formatar(math.sqrt(numero))}\n')

        elif opcao == 7:  # porcentagem
            print('\n[PORCENTAGEM]')
            lista_valores = ler_numeros('Digite a porcentagem e o valor (ex: 20 150): ')
            resultado = lista_valores[0] / 100 * lista_valores[1]
            print(f'Resultado: {lista_valores[0]:g}% de {lista_valores[1]:g} = {formatar(resultado)}\n')

        elif opcao == 8:  # fatorial
            print('\n[FATORIAL]')
            numero = int(input('Digite um número inteiro não negativo: '))
            if numero < 0:
                print('Não existe fatorial de número negativo.\n')
            else:
                fatorial = 1
                for i in range(2, numero + 1):
                    fatorial *= i
                print(f'Resultado: {numero}! = {fatorial}\n')

        elif opcao == 9:  # ajuda
            print('\n[AJUDA]')
            print('1 - Para operações que recebem mais de um valor, digite os valores separados por espaços.')
            print('2 - Para encerrar o Mycalculator, digite 0 (zero) quando for pedida a operação.')
            print('3 - Depois de escolher a operação, digite os valores pedidos e aguarde o resultado. '
                  'Em seguida, você poderá escolher uma nova operação.\n')

        elif opcao == 0:  # sair
            print('\nAté logo (:')
            break

        else:
            print('Opção inválida. Digite um número de 0 a 9.\n')

    except (ValueError, IndexError):
        print('Entrada inválida. Confira se digitou números, separados por espaço.\n')
