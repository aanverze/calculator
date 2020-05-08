#Calculadora - definindo suas funções

'''
programinha para calcular
'''
def bemvindo():
    print('''
BEM-VINDO A CALCULADORA!
''')
...
# Don’t forget to call the function
bemvindo()


def calculadora():
    operacao = input('''
----------CALCULADORA----------
Por gentileza informe uma operação matemática:
+ para soma
- para subtração
* para multiplicação
/ para divisão

''')


    calc1 = int(input("Informe o primeiro número: "))
    calc2 = int(input("Informe o segundo número: "))

    if operacao == '+' :
        print('{} + {} = '.format(calc1, calc2))
        print(calc1 + calc2)

    elif operacao == '-' :
        print('{} - {} = '.format(calc1, calc2))
        print(calc1 - calc2)

    elif operacao == '*' :
        print('{} * {} = '.format(calc1, calc2))
        print(calc1 * calc2)

    elif operacao == '/' :
        print('{} / {} = '.format(calc1, calc2))
        print(calc1 / calc2)

    else:
        print("Você não informou um operador válido, por favor tente novamente!")


#Definindo função again() para questionar usuário se deseja calcular novamente
    again()

def again():

    #Pegue as informações do usuário
    calc_again = input('''
Você quer calcular novamente?
Por favor escolha S para SIM ou N para NÃO.
''')

    #Se usuário escolher sim, execute a função calculadora()
    if calc_again.upper() == 'S':
        calculadora()
    #Se o usuário escolher não, execute a função calculadora()
    elif calc_again.upper() == 'N':
        print("Até mais!")
    #Se o usuário executar outra tecla, execute novamente a função again
    else:
        again()
        
calculadora()

        
    







