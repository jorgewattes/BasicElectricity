import numpy as np
import math
import EleBas_N0 as EB

alunos=[
'Adriano Pires Ferreira',
'Ana Alice Araujo Nogueira',
'Camile Jordana Franco Garcia',
'Camilly Vitória Gomes De Sousa',
'Clenia Santos Silva Ferreira',
'Daniel Ferreira Simões',
'Derlan Da Silva Oliveira',
'Felipe Soares Gomes',
'Francisca Maria Queiroz Da Silva',
'Francisco Ivan Gomes De Oliveira',
'Gustavo Chagas Barbosa',
'Hygo De Souza E Silva',
'João Victor Rocha Costa',
'José Wellington Nunes Pereira',
'Kailany Santos Vieira',
'Leandro Oliveira De Lima',
'Lohanne Da Silva Vieira',
'Lucas Vinicius De Oliveira Lima',
'Marcelo De Oliveira Melo Costa',
'Maria Da Glória De Cristo Félix',
'Paulo Roberto Nepomuceno De Sousa',
'Pedro Evander Lopes Da Silva',
'Pedro Ryan Ferreira Lima',
'Rafael Luz Gomes',
'Raquel Das Chagas',
'Rogerson Sousa Do Nascimento',
'Sabrina Rodrigues De Amorim',
'Tamires Vitória Silva De França',
'Wagner Gomes De Oliveira'
]

resp={}
enunciado=''
gabaritoaluno=''
gabarito={}


# Questoes
for x in range(len(alunos)):
    #print(alunos[x])
    enunciado=enunciado+'Prova N0! (0-pontos)\nAluno: '+ alunos[x]+' \n'

    [enun,gab]=EB.Q1()
    gabaritoaluno=gabaritoaluno+'Q1)'+gab+' / '
    enunciado=enunciado+f'{enun}\n\n\n\n\n'

    [enun,gab]=EB.Q2()
    gabaritoaluno=gabaritoaluno+'Q2)'+gab+' / '
    enunciado=enunciado+f'{enun}\n\n\n\n\n'

    [enun,gab]=EB.Q3()
    gabaritoaluno=gabaritoaluno+'Q3)'+gab+' / '
    enunciado=enunciado+f'{enun}\n\n\n\n\n'

    [enun,gab]=EB.Q4()
    gabaritoaluno=gabaritoaluno+'Q4)'+gab+' / '
    enunciado=enunciado+f'{enun}\n\n\n\n\n'

    [enun,gab]=EB.Q5()
    gabaritoaluno=gabaritoaluno+'Q5)'+gab+' / '
    enunciado=enunciado+f'{enun}\n\n\n\n'

    [enun,gab]=EB.Q6()
    gabaritoaluno=gabaritoaluno+'Q6)'+gab
    enunciado=enunciado+f'{enun}\n'

    gabarito[alunos[x]]=gabaritoaluno
    gabaritoaluno=''
#Gabarito
enunciado=enunciado+f'Gabarito Prova N2\n'
for x in range(len(alunos)):
    enunciado=enunciado+f'{alunos[x]}\n{gabarito[alunos[x]]}\n'

#enunciado=enunciado.replace('.',',')
print(enunciado)
#file = open('RegraDeTes.txt','w+')
#file.write(enunciado)
#file.close()
