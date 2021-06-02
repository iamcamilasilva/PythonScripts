# 3- Nesse exercício vamos simular um caixa de mercado!
# Dado o dicionário inicial {'banana': 3.1, 'maca': 1.5, 'goiaba': 4.3}
# Faça um Loop Infinito que pergunte para o usuário qual produto ele gostaria de consultar o preço e que retorne o valor
# contido no dicionário.
# 3.1- Faça uma condição de saída para o Looping.
# 3.2- Faça uma sessão para cadastrar novos produtos.
# 3.3- Armazene os produtos consultados em um arquivo json na mesma pasta.



#imports
import json



def check_price(mydict):
    '''Com base no dicionário inicial, consulta os produtos existentes retornando os seus valores. Salva no arquivo
    log.json os produtos consultados na execução atual.'''


    checked = {}
    product = 0
    while product != 'cadastrar':
        product = str(input("Qual produto gostaria consultar:"))

        if product in mydict.keys():
            checked.update({product: mydict[product]})
            print(mydict[product])
            with open('log.json', 'w') as log:
                json.dump(checked, log)
        else:
            print("O produto não está cadastrado no sistema.")
            add_new(mydict)


def add_new(mydict):
    '''Com base no dicionário inicial, cadastra um novo produto retornado o dicionário atualizado na saída da função.'''


    newproduct = str(input("Qual produto gostaria de cadastrar:"))
    value = float(input("Qual valor do produto:"))

    if newproduct not in mydict.keys():
        mydict.update({newproduct: value})
        print(mydict)


def main():
    check_price(mydict)


if __name__ == "__main__":
    mydict = {'banana': 3.1, 'maca': 1.5, 'goiaba': 4.3}
    main()
