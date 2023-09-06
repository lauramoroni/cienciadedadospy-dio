#Maiúscula, minúscula e título
curso = "pYthOn"

print(curso)
print(curso.upper())
print(curso.lower())
print(curso.title())

# Eliminando espaço em branco 
curso = "    Python "
print(curso)

print(curso.strip() + ".")
print(curso.lstrip() + ".")
print(curso.rstrip() + ".")

# Junções e centralização 
curso = "Python"

print(curso)
print(curso.center(10, "#"))
print(".".join(curso))

# Fatiamento 
texto = "Curso de Python"
print(texto)
print(texto[0])
print(texto[10])
print(texto[:9])
print(texto[9:])

print(texto.split()[0])
print(texto.split()[1])
print(texto.split()[2])
