# Escreva um programa que converta uma temperatura digitada em °C em °F. 

graus_celsius = float(input("Informe o valor em graus Celsius: "))

graus_fahrenheit = ((9*graus_celsius)//5)+32

print("{} graus Celsius equivale a {} graus Fahrenheit".format(graus_celsius, graus_fahrenheit))