import forca
import adivinhacao


print("********************************")
print('Jogos Index')
print("********************************")

print("Escolha o jogo que deseja: (1)Forca (2)Adivinhação ")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Jogar o Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogar o Adivinhação")
    adivinhacao.jogar()
else:
    print("Por favor escolha um jogo válido")




