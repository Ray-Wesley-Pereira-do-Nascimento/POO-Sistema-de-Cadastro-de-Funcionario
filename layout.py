#Padrão do Menu e do padrão da interface da console
def linha(tam=100):
    return '=' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(100))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}')
        cont += 1
    print(linha())
    resp = lerResp('Digite a opção desejada: ')
    return resp


def edicao(lista):
    cabecalho('Escolha o Dado que dejesa editar')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}')
        cont += 1
    print(linha())
    resp = lerResp('Digite a opção desejada: ')
    return resp


def lerResp(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite uma opção válida.\033[m')
            continue
        else:
            return n