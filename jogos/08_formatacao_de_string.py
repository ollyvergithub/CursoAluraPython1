print("********************************")
print('Formatação de string - String Interpolation')
print("********************************")

numero_secreto = 42

total_de_tentativas = 3

rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {}  de : {} ".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if(chute_maior):
            print("Você errou! Seu chute foi maior que o número secreto!")
        elif(chute_menor):
            print("Você errou! Seu chute foi menor que o número secreto!")

    rodada = rodada + 1


print("Fim do Jogo!")
