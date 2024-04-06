import copy
atual=[]
lista=[]
agenda= { }


##Criando a estrutura dos dados para a agenda

#adicionar_novo_contato()
def adicionar_novo_contato():
    print('Inserindo novos numeros')
    while True:
        print(' Adicione um novo contato ? ')
        agenda['nome'] = input('Escolha um nome ')
        agenda['Telefone1'] = (input('Adicione o numero de celular chip1 '))
        agenda['Telefone2'] = (input('Adicione o numero de celular chip2 '))
        lista.append(agenda.copy())

        print('Contato adicionado')
        print(lista)

        continuar = input('Deseja continuar a inserir os contatos ? sim ou não ')
        if continuar == 'sim'.lower:
            continue
        else:
            print('Finalizando adição de contatos')
            print(lista)
            break

# adicionar_novo_numero()
def adicionar_novo_numero():
    inserir = input('Deseja inserir a um numero a um contato existente ou inserir do começo ? ')
    if inserir == 'começo':
        adicionar_novo_contato()
    elif inserir == 'existente':
        qualc = str(input('Qual seria o nome dessa pessoa ? '))
        for n in lista:
            if qualc in n['nome']:
                decisao=input('O contato vai ser adicionado no chip 1 ou no chip 2 ? ')
                if decisao == '1':
                    n['Telefone1'] = input('Insira o numero se for no chip1 ')
                    print('Contato adicionado com sucesso')
                    print(lista)
                elif decisao == '2':
                    n['Telefone2'] = input('Insira o numero se for no chip2 ')
                    print('Cotnato adicionado com sucesso')
                    print(lista)
               
            


# excluir_contato_completo()
def excluir_contato_completo():
    ctz = input('Tem certeza que deseja utilizar essa função de deletar contatos ? ')
    if ctz == 'sim':
        apagar = input('Qual nome do contato que deseja apagar ')
        if apagar in agenda['nome']:
            agenda.clear()
            for n in lista:
                if n['nome'] == apagar:
                    alvo = (lista.index(n))
                    lista.pop(alvo)
                    print('Listas com os contatos atuais ')
                    print(lista)
        else:
            print('Nome invalido')
                    
        
            

# encontrar_numero()
def encontrar_numero():
    numero = str(input('DIgite um numero'))
    for n in lista:
        # car=(input('Digite um numero para realizar verificação '))
        if numero in n['Telefone1']:
            print(f'O numero pertence a primeira paleta de contatos {n}')
        elif numero in n['Telefone2']:
            print(f'O numero pertence a segunda paleta de contatos {n}')
        else:
            print('Numero invaido')


# excluir_numero()
def excluir_numero():
    print('=-=' * 20)
    print(lista)
    excluir = input('Qual numero de celular voce quer excluir ? ')
    for n in lista:
        if excluir in n['Telefone1'] or n['Telefone2']:
            print(lista)
            exe = n['nome']
            print(exe)
            if n['Telefone1'] == excluir:
                n['Telefone1'] = ' '
                print(lista)

            elif n['Telefone2'] == excluir:
                n['Telefone2']=''
                print(lista)

            else:
                print('Inserção numero invalida')


"""Excluir telefone"""

print('Agenda telefonica')
print('Ola Selecione conforme melhor opção te atender')

opcoes=[
    'Escolha 1 = Adicionar novo contato',
    'Escolha 2 = Adcionar novo numero',
    'Escolha 3 = Encontrar numero ',
    'Escolha 4 = Excluir numero ',
    'Escolha 5 = Excluir contato completo',
    'Escolha 6 = Fechar agenda',
]


while True:
    for n in opcoes:
        print(f'{n}')
        print('-=-'*18)
    escolha=input(f'Qual das opções voce deseja ')


    if escolha =='1':
        adicionar_novo_contato()
    elif escolha=='2':
        adicionar_novo_numero()
    elif escolha=='3':
        encontrar_numero()
    elif  escolha=='4':
        excluir_numero()
    elif escolha =='5':
        excluir_contato_completo()
    elif escolha=='6':
        print('Fim do codigo')
        break
    else:
        print('Opção invaliada')