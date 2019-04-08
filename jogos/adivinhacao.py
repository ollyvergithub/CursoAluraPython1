import random

def jogar():
    print("********************************")
    print('Definindo pontuação para o usuário')
    print("********************************")

    print("Qual o nível de dificuldade?")
    print("(1)Facil (2)Moderado (3)Difícil")
    nivel = int(input("Defina um nível: "))

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #print(numero_secreto)

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
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (chute_maior):
                print("Você errou! Seu chute foi maior que o número secreto!")
            elif (chute_menor):
                print("Você errou! Seu chute foi menor que o número secreto!")

            pontos_perdidos = abs(numero_secreto - chute) #abs = absolute sem sinal negativo
            pontos = pontos - pontos_perdidos


        rodada = rodada + 1

    print("Fim do Jogo!")

if(__name__ == '__main__'):
    jogar()



