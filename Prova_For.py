#Aluno:Guilherme Marzano
#Desenvolver um programa que leia o nome, idade e sexo de 5 pessoas. No final do programa exibir:
#A média de idade de todo o grupo
#Nome da pessoa mais velha
#Quantas pessoas têm menos de 20 anos
#Quantas pessoas tem mais de 40 anos
#Qual o sexo da pessoa mais nova
#---------------------------------------------------------------------------------------------------
print('Programa ler informação de pessoas')

lst_pessoas = [] 

#Criando um dicionário vazio para ajudar a digitar as chaves.
dic_pessoa = {'nome': '','idade':0,'genero':''}

flg_nome = False
flg_idade = False
flg_genero = False
flg_enunciado = True

i = 1

# Coleta e validação dos dados
while len(lst_pessoas) <=4:
    if flg_enunciado:
        dic_pessoa = {'nome': '','idade':0,'genero':''}
        print(f'Digite as informações da {i}º pessoa')
        flg_enunciado = False
    if not flg_nome:
        nome = input('Nome: ')
        if len(nome)<=1:
            print('Nome deve conter mais de uma letra')
            flg_nome = False
        else:
            flg_nome = True
    else:
        if not flg_idade:
            idade_str = input('Idade: ')
            if idade_str.isdigit():
                idade = int(idade_str)
                flg_idade = True
            else:
                print('Digite apenas números inteiros para a idade')
                flg_idade = False
        else:
            if not flg_genero:
                genero = input('Genero(m)Masculino, (f)Feminino:').lower()
                if genero in ['m','f']:
                    flg_genero = True
                else:
                    print('Digite apenas as letras m ou f')
                    flg_genero = False
    
    #Criando o dicionário e populando a lista
    if flg_genero and flg_idade and flg_nome:
        #Criando um dicionário vazio para ajudar a digitar as chaves.
        dic_pessoa['nome'] = nome
        dic_pessoa['idade'] = idade
        dic_pessoa['genero'] = genero
        flg_enunciado = True
        lst_pessoas.append(dic_pessoa)
        i += 1
        dic_pessoa = {'nome': '','idade':0,'genero':''}
        flg_nome = False
        flg_idade = False
        flg_genero = False
        flg_enunciado = True
 

#Calculo média:
#Contabilizando quantas pessoas com menos de 20 anos e quantas com mais de 20
soma = 0
cnt_menor20 = 0
cnt_maior40 = 0
for pessoa in lst_pessoas:
    soma = soma + pessoa['idade']
    if pessoa['idade'] <20:
        cnt_menor20 +=1
    elif pessoa['idade'] >40:
        cnt_maior40 +=1
   
media = soma/5

lst_pessoas = sorted(lst_pessoas, key= lambda x: x['idade'])

print('Mostrando as pessoas cadastradas em ordem de idade')
for pessoas in lst_pessoas:
    print(pessoas)

#Resposta:
print(f'A media de idade é {media} ')

print(f'Nome da pessoa mais velha é: {lst_pessoas[4]["nome"]}')

print(f' Quantidade de pessoas mais novas que 20 anos: {cnt_menor20} ')
print(f' Quantidade de pessoas mais velhas que 40 anos: {cnt_maior40} ')

print(f'O Genero da pessoa mais nova é {lst_pessoas[0]["genero"]}')

print("Fim do programa")

    
