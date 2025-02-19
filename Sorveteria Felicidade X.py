def exibir_cardapio():
    print(' Bem vindo à Sorveteria Felicidade X')
    print('---------------------------------------------Cardápio--------------------------------------------')
    print('| CÓDIGO | DESCRIÇÃO            |   Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
    print('|   TR   | Sabores Tradicionais |  R$ 6,00            | R$ 10,00           | R$ 18,00          |')
    print('|   ES   | Sabores Especiais    |  R$ 7,00            | R$ 12,00           | R$ 21,00          |')
    print('|   PR   | Sabores Premium      |  R$ 8,00            | R$ 14,00           | R$ 24,00          |')
    print('|-----------------------------------------------------------------------------------------------|')

def calcular_valor(codigo, tamanho):
    precos = {
        'TR': {'P': 6.00, 'M': 10.00, 'G': 18.00},
        'ES': {'P': 7.00, 'M': 12.00, 'G': 21.00},
        'PR': {'P': 8.00, 'M': 14.00, 'G': 24.00}
    }
    return precos[codigo][tamanho]

def obter_descricao(codigo):
    descricoes = {
        'TR': 'Tradicional',
        'ES': 'Especial',
        'PR': 'Premium'
    }
    return descricoes[codigo]

def main():
    acumulador = 0

    while True:
        # Exibir o cardápio no início de cada pedido
        exibir_cardapio()

        # Validação do tamanho
        while True:
            tamanho = input('Entre com o TAMANHO do pote desejado (P/M/G): ').upper()
            if tamanho not in ['P', 'M', 'G']:
                print('!!!!!!! TAMANHO INVÁLIDO !!!!!!!')
            else:
                break  # Sai do loop quando o tamanho é válido

        # Validação do código
        while True:
            codigo = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ').upper()
            if codigo not in ['TR', 'ES', 'PR']:
                print('!!!!!!! CÓDIGO INVÁLIDO !!!!!!!')
            else:
                break  # Sai do loop quando o código é válido

        descricao = obter_descricao(codigo)
        valor = calcular_valor(codigo, tamanho)

        print(f'Você pediu um sorvete sabor {descricao.upper()} {tamanho} de R$ {valor:.2f}')
        acumulador += valor

        # Perguntar se deseja continuar
        pedir_mais = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
        if pedir_mais == 'N':
            print(f'O total a ser pago é: R$ {acumulador:.2f}')
            break

if __name__ == "__main__":
    main()
