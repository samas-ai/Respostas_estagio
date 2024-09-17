def pesquisaLetra(palavra):
    x = 0
    for letra in palavra:
        if letra == "a" or letra == "A":
            x += 1
    
    return x


palavra = input()
print(pesquisaLetra(palavra))



