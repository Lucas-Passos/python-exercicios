def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO:\"{entrada}\" e um preco invalido!\033[m')
        else:
            valida = True
            return float(entrada)
