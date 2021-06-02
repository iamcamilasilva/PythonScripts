# 2 - Com a lista de exemplo [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] escreva um programa que imprima todos os elementos que
# sejam maiores que 5.
# 2.1- Faça uma nova lista com os elementos maiores que 5 e imprima essa nova lista.
# 2.2- Peça para o usuário um número e retorne uma lista que contenha apenas elementos da lista de exemplo que forem
# maiores que o valor dado pelo usuário.



def order_list(mylist):
    '''Com base na lista de exemplo, seleciona e salva em uma nova lista todos os elementos maiores que 5.'''


    newlist = []
    for i in mylist:
        if i > 5:
            newlist.append(i)
            print("Maiores que 5:", newlist)


def user_list(number, mylist):
    '''Com base na lista de exemplo, seleciona e salva em uma nova lista todos os elementos maiores que um determinado
    número fornecido pelo usuário.'''


    userlist = []
    for j in mylist:
        if j >= number:
            userlist.append(j)
            print("Maiores que", number, ":", userlist)


def main():
    order_list(mylist)
    user_list(number, mylist)


if __name__ == "__main__":
    mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    number = int(input("Digite um número entre 1 e 89:"))
    main()
