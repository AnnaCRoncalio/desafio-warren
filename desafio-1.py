numero_atual = 10
numeros_reversiveis = []

while numero_atual < 1000:
    ultimo_digito_numero = int(repr(numero_atual)[-1])
    numero_existente_lista = numeros_reversiveis.count(numero_atual)
        
    if ultimo_digito_numero != 0:
        numero_invertido = int((str(numero_atual)[::-1]))

        if numero_atual not in numeros_reversiveis and numero_invertido not in numeros_reversiveis:
            soma_numeros = numero_atual + numero_invertido
    
            if soma_numeros % 2 != 0:
                numeros_reversiveis.append(numero_atual)
                print(numero_atual, ' + ', numero_invertido, ' = ', soma_numeros)
    
    numero_atual += 1

print('Total de números reversíveis: ', len(numeros_reversiveis))
