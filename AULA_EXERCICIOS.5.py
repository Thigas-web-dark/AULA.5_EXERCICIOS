# 1 Imprima uma mensagem de boas-vindas na tela.
print('BOAS VINDAS!')

# 2 Declare uma variável booleana verdadeiro com o valor True e imprima seu tipo
Sinal = bool(input('1 ou 0? '))
print(Sinal)

# 3 Imprima o resultado da multiplicação de dois números decimais de sua escolha    
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite mais um valor '))
multiplicacao = (num1 * num2)
print(multiplicacao)

# 4 Imprima o resultado da divisão de dois números inteiros de sua escolha.
print('Divisão')
numero1 = int(input("Digite um valor "))
numero2 = int(input("Digite mais um valor "))
divisao = numero1 / numero2 
print(divisao)

# 5 Imprima o resultado da subtração de dois números inteiros de sua escolha
print('Subtração')
number1 = int(input('Digite um valor '))
number2 = int(input('Digite mais um valor '))
subtracao = number1 - number2 
print(subtracao)

# 6 Imprima o resultado da divisão inteira de dois números inteiros de sua escolha.
print('Divisão, denovo')
numero1 = int(input("Digite um valor "))
numero2 = int(input("Digite mais um valor "))
divisao = numero1 / numero2 
print(divisao)

# 7 Imprima o resultado da multiplicação de 4 números decimais de sua escolha
print('multiplicação de 4 numeros decimais')
um = float(input('Digite um valor '))
dois = float(input('Digite um mais valor '))
tres = float(input('Digite um mais valor '))
quatro = float(input('Digite um mais valor '))
juncao = um * dois * tres * quatro
print(juncao)

# 8 Declare uma variável numero e atribua um número inteiro. Em seguida, imprima o dobro desse número
print("Digite um valor, que voce queira que seja dobrado")
valor = int(input('Digite um valor: '))
dobra = valor * 2
print(dobra)

# 9 Crie uma calculadora de soma com as ferramentas que vc já conhece(Use apenas input, print e variavel)
print('calculadora de soma')
soma1 = int(input('Digite o primeiro valor para a soma '))
soma2 = int(input('Digite o segundo valor para a soma '))
soma3 = int(input('Digite o terceiro valor para a soma '))
calculo = soma1 + soma2 + soma3 
print(calculo)

# 10 Crie um sistema de cadastro com as estruturas que vc já conhece(Use apenas input, print e variavel)
print('Bem vindo ao cadastro da sua conta')
nome = str(input('Digite o seu nome: '))
senha = str(input('Digite a sua senha: '))
print('login cadastrado')
print('olá ',nome)