print("********************************")
print('Encerrando a interação e o loop. Break e Continue')
print("********************************")

numero_secreto = 42

total_de_tentativas = 3

rodada = 1

for numero_de_vezes in range(1,total_de_tentativas + 1):
    print("Tentativa ", rodada, " de : ", total_de_tentativas)
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    else:
        if (chute_maior):
            print("Você errou! Seu chute foi maior que o número secreto!")
        elif (chute_menor):
            print("Você errou! Seu chute foi menor que o número secreto!")

    rodada = rodada + 1

print("Fim do Jogo!")
