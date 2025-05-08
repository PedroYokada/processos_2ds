estado = input('Coloque "d" para desligar ou "l" para ligar o seu disposito: ')

if estado == "d":
    print('Você desligou o seu dispositivo')
elif estado == "l":
    print('Você ligou o seu dispositivo')
else:
    print("Informação inválida!")
    
