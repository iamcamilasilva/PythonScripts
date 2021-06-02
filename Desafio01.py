# 1- Crie um programa que pergunte para o usuário colocar seu nome e sua idade. Imprima uma mensagem personalizada que
# diga a ele quantos anos vai demorar para ele ter 100 anos!
# 1.1- Utilize a biblioteca datetime para fazer as contas de data.
# 1.2 -Pergunte para o usuário um número de 1 a 10 e imprima a mensagem personalizada X vezes.



#imports
import datetime



def count_years(age):
    '''Calcula a diferença de anos com base no ano em que o indivíduo terá 100 anos subtraído do ano atual.'''


    years = 0
    today = datetime.date.today()
    centenary = ((today.year - age) + 100) - today.year
    if age < 100:
        years += centenary
    else:
        print("Você já tem ou passou dos 100 anos.")
    return years


def main():
    '''Estabelece condição para parar a execução caso o número de repetições exceda 10Vzs.'''


    result = count_years(age)
    repeat = int(input("Digite um número de 1 a 10:"))
    if repeat <= 10:
        print("Você levará {} anos para completar 100 anos. \n".format(str(result)) * repeat)
    else:
        print("Digite um número dentro do intervalo de 1 a 10.")


if __name__ == "__main__":
    name = str(input("Digite o seu nome:"))
    age = int(input("Digite a sua idade:"))
    main()
