nome = 'Éberton'
altura = 1.80
peso = 90
imc = peso / altura ** 2

#f-strings -- Inserir variáveis com strings
resultado = f'{nome} tem {altura:.2f} de altura e seu IMC é: {imc}'
print(resultado)

# .format() Formatando as variávies no padrão desejado
a = 'A'
b = 'B'
c = 1.1

# Entre {} é esperado algum argumento que são passados pela variável formato
string = 'a={} b={} c{:.2f}'

formato = string.format(a,b,c)

print(formato)