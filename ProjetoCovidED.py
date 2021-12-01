import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

covid=pd.read_csv(r'/content/drive/MyDrive/Projeto ED (COVID)/dados_covid_virgula.csv')
covid.head()
paises=pd.read_csv(r'/content/drive/MyDrive/Projeto ED (COVID)/paisescovid.csv')
paises.head()

#Gráfico de comparação da população semi-imunizada e completamente imunizada por estado.
def todasvac():
    fig=px.bar(covid, x='Estados', y='Primeira Dose', color='Vacina Completa', title='GRÁFICO DE COMPARAÇÃO DA POPULAÇÃO SEMI-IMUNIZADA E COMPLETAMENTE IMUNIZADA POR ESTADO.')
    fig.show()

#Gráfico de vacinação completa de cada estado brasileiro.
def vaccompleta():
    fig=px.bar(covid, x='Estados', y='Vacina Completa', color='Vacina Completa', title='GRÁFICO DE VACINAÇÃO COMPLETA APLICADA DE CADA ESTADO BRASILEIRO.')
    fig.show()

#Gráfico de comparação da vacinação completa para o total de população de cada estado.
def vacpop():
    fig=px.bar(covid, x='Estados', y='Populacao', color='Vacina Completa', title='GRÁFICO DE COMPARAÇÃO DA VACINA COMPLETA PARA O TOTAL DE POPULAÇÃO DE CADA ESTADO')
    fig.show()

#Gráfico de primeira dose de cada estado.
def primvac():
    fig=px.bar(covid, x='Estados', y='Primeira Dose', color='Estados', title='GRÁFICO DE PRIMEIRA DOSE APLICADA POR ESTADO BRASILEIRO.')
    fig.show()

#Gráfico de casos registrados por estado.
def casos():
    fig=px.bar(covid, x='Estados', y='Casos', color='Estados', title='GRÁFICO DE CASOS REGISTRADOS POR CADA ESTADO BRASILEIRO.')
    fig.show()

#Gráfico de óbitos registrado por estado.
def obitos():
    fig=px.bar(covid, x='Estados', y='Obitos', color='Estados', title='GRÁFICO DE ÓBITOS REGISTRADOS POR CADA ESTADO BRASILEIRO.')
    fig.show()

#Gráfico de comparação entre casos e óbitos e população.
def casoseobitos():
  fig=px.bar(covid, x='Estados', y='Casos', color='Obitos', title='GRÁFICO DE COMPARAÇÃO ENTRE CASOS E ÓBITOS DE CADA ESTADO BRASILEIRO.')
  fig.show()

#Gráfico da percentagem de vacinas completas de cada estado para com o Brasil.
def percvac():
    totalsegvacina=sum(covid['Vacina Completa'])
    totalbrasil=(covid['Vacina Completa']/totalsegvacina)*100
    valores=totalbrasil
    names=covid['Estados']
    fig=px.pie(values=valores, names=names, title='GRÁFICO DE PERCENTAGEM DA VACINAÇÃO COMPLETA DE CADA ESTADO RELACIONADO AO BRASIL INTEIRO.')
    fig.show()

#Gráfico de percentagem de primeira dose de cada estado para com o Brasil.
def percpridose():
    valores=covid['Primeira Dose']
    names=covid['Estados']
    fig=px.pie(values=valores, names=names, title='GRÁFICO DE PERCENTAGEM DE PRIMEIRA DOSE APLICADA DE CADA ESTADO RELACIONADO AO BRASIL INTEIRO.')
    fig.show()

#Comparativo entre primeira e segunda dose (paises).
def paisvac():
    ax=paises[['Primeira Dose', 'Vacina Completa']].plot(figsize=(25,5), kind='bar', title='GRÁFICO COMPARATIVO DA PRIMEIRA E SEGUNDA DOSE APLICADAS NOS PAISES MAIS POPULOSOS DO MUNDO')
    ax.set_xticklabels(paises['Paises'])
    plt.show()

#Comparativo entre casos e obitos (paises).
def paiscasos():
    ax=paises[['Casos', 'Obitos']].plot(figsize=(25,5), kind='bar', title='GRÁFICO COMPARATIVO DOS CASOS E OBITOS REGISTRADOS NOS PAISES MAIS POPULOSOS DO MUNDO')
    ax.set_xticklabels(paises['Paises'])
    plt.show()

#Gráfico de percentagem das vacinas completas entre os paises.
def paisperc1():
    valores=paises['Vacina Completa']
    names=paises['Paises']
    fig=px.pie(values=valores, names=names, title='GRÁFICO DE PERCENTAGEM DE VACINA COMPLETA APLICADA NOS PAISES MAIS POPULOSOS DO MUNDO.')
    fig.show()

#Gráfico de percentagem das primeiras doses entre os paises.
def paisperc2():
    valores=paises['Primeira Dose']
    names=paises['Paises']
    fig=px.pie(values=valores, names=names, title='GRÁFICO DE PERCENTAGEM DE PRIMEIRA DOSE APLICADA NOS PAISES MAIS POPULOSOS DO MUNDO.')
    fig.show()

#Gráfico de percentagem dos casos registrados entre os paises.
def paisperc3():
    valores=paises['Casos']
    names=paises['Paises']
    fig=px.pie(values=valores, names=names, title='GRÁFICO DE PERCENTAGEM DOS CASOS REGISTRADOS NOS PAISES MAIS POPULOSOS DO MUNDO.')
    fig.show()

#Gráfico de percentagem dos obitos registrados entre os paises.
def paisperc4():
    valores=paises['Obitos']
    names=paises['Paises']
    fig=px.pie(values=valores, names=names, title='GRÁFICO DE PERCENTAGEM DOS OBITOS REGISTRADOS NOS PAISES MAIS POPULOSOS DO MUNDO.')
    fig.show()

def menu_inicial():
    print('\n### MENU INICIAL ###')
    print('Opção [0] -> Finalizar o programa.')
    print('Opção [1] -> Dados sobre as vacinas.')
    print('Opção [2] -> Dados sobre os casos e óbitos.')
    print('Opção [3] -> Dados sobre os países mais populosos do mundo.')
    print('Opção [4] -> Busque seu estado.\n')

def menu_vacina():
    print('\n### MENU DE VACINAS ### ')
    print('Opção [0] -> Retornar ao menu inicial.')
    print('Opção [1] -> Gráfico de comparação da população semi-imunizada e completamente imunizada por estado brasileiro.')
    print('Opção [2] -> Gráfico de vacinação completa em relação a cada estado brasileiro.')
    print('Opção [3] -> Gráfico de comparação da vacinação completa para o total de população de cada estado brasileiro.')
    print('Opção [4] -> Gráfico das primeiras doses aplicadas por estado brasileiro.')
    print('Opção [5] -> Gráfico da percentagem de vacinas completas de cada estado para com o Brasil.')
    print('Opção [6] -> Gráfico de percentagem de primeira dose de cada estado para com o Brasil.\n')

def menu_casoseobitos():
    print('\n### MENU DE CASOS E ÓBITOS ###')
    print('Opção [0] -> Retornar ao menu inicial.')
    print('Opção [1] -> Gráfico de casos registrados por estado.')
    print('Opção [2] -> Gráfico de óbitos por estado.')
    print('Opção [3] -> Gráfico de comparação entre casos e óbitos.\n')

def menu_busca():
    print('\n### MENU DE BUSCA ###')
    print(f'Estado: {busca}\n')
    print('Opção [0] -> Retornar ao menu inicial ou pesquisar outro estado.')
    print('Opção [1] -> Total de vacinas aplicadas.')
    print('Opção [2] -> Total de casos registrados.')
    print('Opção [3] -> Total de óbitos registrados.\n')

def menu_paises():
    print('\n### MENU PAÍSES ###')
    print('Opção [0] -> Retornar ao menu inicial.')
    print('Opção [1] -> Comparativo entre primeira e segunda dose dos países mais populosos do mundo.')
    print('Opção [2] -> Comparativo entre casos e óbitos dos países mais populosos do mundo.')
    print('Opção [3] -> Gráfico de percentagem da vacinação completa entre os países mais populosos do mundo.')
    print('Opção [4] -> Gráfico de percentagem da primeira dose completa entre os países mais populos do mundo.')
    print('Opção [5] -> Gráfico de percentagem de casos registrados entre os países mais populos do mundo.')
    print('Opção [6] -> Gráfico de percentagem de óbitos registrados entre os países mais populos do mundo.\n')

menu_inicial()
print()
opcao=int(input('Digite a sua opção desejada: '))
while opcao!=0:
#====================================================================================== VACINAS ======================================================================================#
    if opcao==1:
        menu_vacina()
        while opcao!=0:
            opcao=int(input('Digite sua opção desejada: '))
            if opcao==1:
                todasvac()
            elif opcao==2:
                vaccompleta()
            elif opcao==3:
                vacpop()
            elif opcao==4:
                primvac()
            elif opcao==5:
                percvac()
            elif opcao==6:
                percpridose()
            else:
                print('Opção inválida.')
            menu_vacina()
#====================================================================================== CASOS E ÓBITOS======================================================================================#
    elif opcao==2:
        menu_casoseobitos()
        while opcao!=0:
            opcao=int(input('Digite sua opção desejada.'))
            if opcao==1:
                casos()
            elif opcao==2:
                obitos()
            elif opcao==3:
                casoseobitos()
            else:
                print('Opção inválida.')
            menu_casoseobitos() 
#====================================================================================== PAÍSES ======================================================================================#
    elif opcao==3:
        menu_paises()
        while opcao!=0:
            opcao=int(input('Digite sua opção desejada: '))
            if opcao==1:
                paisvac()
            elif opcao==2:
                paiscasos()
            elif opcao==3:
                paisperc1()
            elif opcao==4:
                paisperc2()
            elif opcao==5:
                paisperc3()
            elif opcao==6:
                paisperc4()
            else:
                 print('Opção inválida.')
            menu_paises()
#====================================================================================== BUSCA ============================================================================================#
    elif opcao==4:
      busca=input('Digite o estado que você deseja consultar: ')
      while busca.upper() !='V':
        idx=0
        for i in range(len(covid)):
          if busca==covid['Estados'][i]:
            idx = 1
            estado=covid['Estados'][i]
            primeiradose=covid['Primeira Dose'][i]
            vacinacompleta=covid['Vacina Completa'][i]
            casos=covid['Casos'][i]
            obitos=covid['Obitos'][i]
            
            menu_busca()
            opcao=int(input('Digite sua opção desejada: '))
            while opcao!=0:
              if opcao==1:
                print(f'\nInformações: \nEstado: {busca}\nTotal de vacinas aplicadas {vacinacompleta}\n')
              elif opcao==2:
                print(f'\nInformações: \nEstado: {busca}\nTotal de casos: {casos}')
              elif opcao==3:
                print(f'\nInformações: \nEstado: {busca}\nTotal de óbitos: {obitos}')
              menu_busca()
              opcao=int(input('Digite sua opção desejada: '))
        if idx==0:
            print("Estado não encontrado. \n")
        busca=str(input('Digite o estado que você deseja consultar novamente ou digite [V] para retornar ao menu inicial.'))
    menu_inicial()        
    opcao=int(input('Digite sua opção desejada: '))
