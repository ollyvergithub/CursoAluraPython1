print("********************************")
print('O laço for')
print("********************************")

numero_secreto = 42

total_de_tentativas = 3

rodada = 1

for numero_de_vezes in range(1,total_de_tentativas + 1):
    print("Tentativa ", rodada, " de : ", total_de_tentativas)
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if (chute_maior):
            print("Você errou! Seu chute foi maior que o número secreto!")
        elif (chute_menor):
            print("Você errou! Seu chute foi menor que o número secreto!")

    rodada = rodada + 1

print("Fim do Jogo!")

print("Outra Forma de for \n")
for numero_de_vezes in [1,2,3,4,5,6]:
    print("Variável Número de Vezes {} ".format(numero_de_vezes ))

