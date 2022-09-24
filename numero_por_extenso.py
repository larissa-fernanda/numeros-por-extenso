def extenso (numero):
    numeros = ['Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    for indice in range (20):
        if numero == indice:
            return numeros[indice]

def ordem_grandeza (numero, ordem, texto_ordem): 
    if numero % ordem < 10 or numero > 100 and numero % ordem <= 1000:
        if numero == ordem:
            return texto_ordem
    
        texto = texto_ordem + ' e '
        if numero < 100:
            return texto + extenso(numero%ordem)
        if numero > 100 and numero < 1000:
            return texto + extenso_dezenas(numero % ordem)
        if numero >= 1000 and numero < 1000000:
            return extenso_centenas(numero//ordem) + ' ' + texto + extenso_centenas(numero%ordem)
    
def extenso_dezenas (numero):
    if numero<20:
        return extenso(numero)
    minha_lista = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta','noventa']
    for dezena in range(20, 90 + 1, 10): # [20 30 40 50 60 70 80 90]
        if numero<dezena+10:
            indice = int(dezena / 10)
            return ordem_grandeza(numero, dezena, minha_lista[indice - 2])

def extenso_centenas (numero):
    if numero<100:
        return extenso_dezenas(numero)
    if numero==100:
        return 'cem'
    minha_lista = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos','oitocentos','novecentos']
    for centena in range(100, 900 + 1, 100):
        if numero<centena+100:
            indice = int(centena / 100)
            return ordem_grandeza(numero, centena, minha_lista[indice - 1])   

def extenso_milhares (numero):
    if numero<1000:
        return extenso_centenas(numero)
        
    if numero % 1000 == 0:
        return extenso_centenas(numero // 1000) + ' mil'
    
    return extenso_centenas(numero//1000) + ' mil e ' + extenso_centenas(numero % 1000)
    
def extenso_milhoes (numero):
    if numero<1000000:
        return extenso_milhares(numero)
        
    if numero == 1000000:
        return 'um milhão'
    if numero<2000000:
        return 'um milhão e ' + extenso_milhares (numero % 1000000)
    if numero % 1000000 == 0:
        return extenso_centenas(numero//1000000) + ' milhões'
    
    return extenso_centenas(numero//1000000) + ' milhões e ' + extenso_milhares (numero % 1000000)

def extenso_bilhoes (numero):
    if numero<1000000000:
        return extenso_milhoes(numero)
        
    if numero == 1000000000:
        return 'um bilhão'
    if numero<2000000000:
        return 'um bilhão e ' + extenso_milhoes (numero % 1000000000)
    if numero % 1000000000 == 0:
        return extenso_centenas(numero//1000000000) + ' bilhões'
    
    return extenso_centenas(numero//1000000000) + ' bilhões e ' + extenso_milhoes (numero % 1000000000)
    
def extenso_trilhoes (numero):
    if numero<1000000000000:
        return extenso_bilhoes(numero)
        
    if numero == 1000000000000:
        return 'um trilhão'
    if numero<2000000000000:
        return 'um trilhão e ' + extenso_bilhoes (numero % 1000000000000)
    if numero % 1000000000000 == 0:
        return extenso_centenas(numero//1000000000000) + ' trilhões'
    
    return extenso_centenas(numero//1000000000000) + ' trilhões e ' + extenso_bilhoes (numero % 1000000000000)


while True:
    try:
        pergunta = int(input('digite um numero até a casa dos trilhões [ou uma string para interromper]:'))
        print (extenso_trilhoes(pergunta))
    except:
        break