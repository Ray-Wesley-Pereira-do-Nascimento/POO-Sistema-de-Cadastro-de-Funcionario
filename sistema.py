from layout import *
from time import sleep
import mysql.connector

conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='S6!3&de7p@fd',
            database='projeto',
        )

cursor = conexao.cursor()

criar_tabela_mySQL = """CREATE TABLE IF NOT EXISTS cadastros (
                            id_funcionario int(11) NOT NULL AUTO_INCREMENT,
                            nome_funcionario VARCHAR(60) NOT NULL,
                            idade_funcionario int(5),
                            telefone_funcionario VARCHAR(20),
                            email_funcionario VARCHAR(70) NOT NULL,
                            PRIMARY KEY (id_funcionario))"""

cursor.execute(criar_tabela_mySQL)


class Cadastrar:
    def __init__(self, nome_funcionario, idade_funcionario, telefone_funcionario, email_funcionario):


        #Guardando os cadastro no Banco de dados
        comando = f'INSERT INTO cadastros (nome_funcionario, idade_funcionario, telefone_funcionario, email_funcionario)'\
                  f'VALUES ("{nome_funcionario}", "{idade_funcionario}", "{telefone_funcionario}", "{email_funcionario}")'
        cursor.execute(comando)
        conexao.commit()



class Mostrar_Cadastros:
    def __init__(self):
        comando = f'SELECT * FROM cadastros'
        cursor.execute(comando)
        linhas = cursor.fetchall()
        cabecalho('Funcionários Cadastrados')
        # Vai buscando linha por linha e mostra na tela os cadastros do banco
        for i in linhas:
            print(f'|Id: {i[0]} | Nome: {i[1]} | Idade: {i[2]} | Telefone: {i[3]} | Email: {i[4]}')



class Editar:
    def __init__(self, id, opcao):
        if opcao == 1:
            nome = input('Digite o nome do funcionário: ')

            comando = f'UPDATE cadastros SET nome_funcionario = "{nome}" WHERE id_funcionario = "{id}"'
            cursor.execute(comando)
            conexao.commit()
        elif op == 2:
            idade = int(input('Digite a idade do funcionário: '))

            comando = f'UPDATE cadastros SET idade_funcionario = "{idade}" WHERE id_funcionario = "{id}"'
            cursor.execute(comando)
            conexao.commit()
        elif op == 3:
            telefone = input('Digite o telefone do funcionário: ')

            comando = f'UPDATE cadastros SET telefone_funcionario = "{telefone}" WHERE id_funcionario = "{id}"'
            cursor.execute(comando)
            conexao.commit()
        elif op == 4:
            email = input('Digite o email do funcionário: ')

            comando = f'UPDATE cadastros SET email_funcionario = "{email}" WHERE id_funcionario = "{id}"'
            cursor.execute(comando)
            conexao.commit()
        elif op == 5:
            nome = input('Digite o nome do funcionário: ')
            idade = int(input('Digite a idade do funcionário: '))
            telefone = input('Digite o telefone do funcionário: ')
            email = input('Digite o email do funcionário: ')

            comando = f'UPDATE cadastros SET nome_funcionario = "{nome}", ' \
                      f'idade_funcionario = "{idade}", ' \
                      f'telefone_funcionario = "{telefone}", ' \
                      f'email_funcionario = "{email}" WHERE id_funcionario = "{id}"'
            cursor.execute(comando)
            conexao.commit()
        else:
            print('Opção inválida, você será re-direcionado ao Menu Principal!!!')



class Deletar:
    def __init__(self, id_funcionario):
        try:
            comando = f'DELETE FROM cadastros WHERE id_funcionario = "{id_funcionario}"'
            cursor.execute(comando)
            conexao.commit()
        except TypeError:
            print('Erro, cadastro não deletado!!!')



#Menu
while True:
        opcao = menu(['Cadastrar', 'Mostrar Cadastros', 'Editar Cadastro', 'Deletar Cadastro', 'Sair'])
        if opcao == 1:
            cabecalho('Cadastrar Funcionário')
            nome_funcionario = input('Digite o nome do funcinário: ')
            idade_funcionario = int(input('Digite a idade do funcionário: '))
            telefone_funcionario = input('Digite o telefone do funcionário: ')
            email_funcionario = input('Digite o email do funcionário: ')
            Cadastrar(nome_funcionario, idade_funcionario, telefone_funcionario, email_funcionario)

        elif opcao == 2:
            cabecalho('Mostrar Cadastros')
            Mostrar_Cadastros()

        elif opcao == 3:
            cabecalho('EDITAR')
            id_func = int(input('Digite o ID do funcionário que deseja editar: '))
            op = edicao(['Nome', 'Idade', 'Telefone', 'Email', 'Editar todos os Campos'])
            Editar(id_func, op)

        elif opcao == 4:
            cabecalho('Deletar Cadastro')
            delete_id = int(input('Informe o ID do funcionário que deseja deletar: '))
            Deletar(delete_id)

        elif opcao == 5:
            print('Saíndo do sistema.......')
            break
        else:
            print('Opção inválida. Por favor digite uma opção válida')
        sleep(2)


conexao.close()
cursor.close()