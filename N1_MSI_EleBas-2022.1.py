import numpy as np
import math
import EleBas_N0 as EB

alunos=[
'ALYNE CAVALCANTE ROCHA',
'ANDERSON BEZERRA DA COSTA',
'ANTONIA VANESKA ROBERTO VIEIRA',
'ANTONIO RAILTON SILVA ALMEIDA',
'ARTHUR DA SILVA BARROZO',
'CARLA RAYSA BARBOZA UCHÔA',
'CLAUDIO MOISÉS VIEIRA GOMES',
'EMANOEL BERNARDINO DA SILVA',
'FRANCISCA ALBEVANIA MENEZES DO CARMO',
'FRANCISCO CARLOS FERREIRA DOS SANTOS JUNIOR',
'FRANCISCO MATHEUS DA SILVA',
'FRANCISCO WALLISON RIBEIRO VIEIRA',
'ISMAEL RODRIGUES DE SALES',
'KLISMANN FLOR DA ROCHA',
'MARIA JULIANA FERREIRA DE MOURA DA SILVA',
'MARIANE DE FREITAS ALVES',
'NICOLLY ELIDA VIEIRA LIMA',
'RAFAELA CRISTINA GONDIM SILVA',
'RYAN MAGALHÃES DE ALMEIDA',
'Vih Menezes'
]

resp={}
enunciado=''
gabaritoaluno=''
gabarito={}

# Questoes
for x in range(len(alunos)):
    #print(alunos[x])
    enunciado=enunciado+'Prova N1 (7-pontos)\nAluno: '+ alunos[x]+' \n'

    [enun,gab]=EB.Q2()
    gabaritoaluno=gabaritoaluno+'Q1) '+gab+' / '
    enunciado=enunciado+'1) (1 ponto) '+f'{enun}\n\n\n'

    [enun,gab]=EB.Q8()
    gabaritoaluno=gabaritoaluno+'Q2) '+gab+' / '
    enunciado=enunciado+'2) (1 ponto) '+f'{enun}\n\n\n\n'

    [enun,gab]=EB.Q7()
    gabaritoaluno=gabaritoaluno+'Q3) '+gab+' / '
    enunciado=enunciado+'3) (1 ponto) '+f'{enun}\n\n\n\n'

    [enun,gab]=EB.Q4()
    gabaritoaluno=gabaritoaluno+'Q4) '+gab+' / '
    enunciado=enunciado+'4) (1 ponto) '+f'{enun}\n\n\n\n'

    [enun,gab]=EB.Q5()
    gabaritoaluno=gabaritoaluno+'Q5) '+gab+' / '
    enunciado=enunciado+'5) (1 ponto) '+f'{enun}\n\n\n\n'

    [enun,gab]=EB.Q6()
    gabaritoaluno=gabaritoaluno+'Q6) '+gab+' / '
    enunciado=enunciado+'6) (1 ponto) '+f'{enun}\n\n\n'

    [enun,gab]=EB.Q3()
    gabaritoaluno=gabaritoaluno+'Q7) '+gab
    enunciado=enunciado+'7) (1 ponto) '+f'{enun}\n'

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