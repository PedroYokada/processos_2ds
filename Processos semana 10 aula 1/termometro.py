class Termometro:
    def __init__(self, temperatura=0):
        self.__temperatura_celsius = temperatura
    
    def get_temperatura_celsius(self):
        return self.__temperatura_celsius
    
    def get_temperatura_fahrenheit(self):
        return (self.__temperatura_celsius * 9/5) + 32
    
    def set_temperatura_celsius(self, temperatura):
        self.__temperatura_celsius = temperatura
    
    def set_temperatura_fahrenheit(self, temperatura):
        self.__temperatura_celsius = (temperatura - 32) * 5/9

# Uso da classe
termometro = Termometro()
termometro.set_temperatura_fahrenheit(68)
print(termometro.get_temperatura_fahrenheit())  # Deve mostrar 68
print(termometro.get_temperatura_celsius())     # Mostra a temperatura em Celsius