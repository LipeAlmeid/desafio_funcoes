from decimal import Decimal

'''
Criar um programa que calcula a quantidade de tinta necessária para 
pintar uma parede. O usuário deverá fornecer as seguintes 
informações: Rendimento, altura e largura. 
O programa deve mostrar na tela a mensagem 'Você necessita de x
latas de tinta'
'''

rendimento = Decimal(input('Qaul é o rendimento da lata? '))
altura = Decimal(input('Qual é a altura da parede? '))
largura = Decimal(input('Qual é a largura da parede? '))

def calcula_quantidade (rendimento, altura, largura):
    area = altura * largura
    quantidade_necessaria = area / rendimento
    return quantidade_necessaria
    

resultado = calcula_quantidade(rendimento, altura, largura)
print(f'Voce necessita de : {resultado:.2f} latas de tinta')


