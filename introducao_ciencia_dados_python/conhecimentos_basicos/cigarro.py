# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias. 

cigarros_por_dia = int(input("Quantos cigarros você fuma por dia?"))
anos = int(input("Quantos anos você já fumou?"))

cigarros_total = (cigarros_por_dia*365)*anos
minutos_perdidos = cigarros_total*10
dias_perdidos = minutos_perdidos//1440

print("Um total de {} cigarros fumados equivale a aproximadamente {} dias de vida perdidos".format(cigarros_total, dias_perdidos))