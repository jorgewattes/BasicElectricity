import numpy as np
import math

def Q1():
    V=110*np.random.randint(1,3)
    P=np.random.randint(2,6)*1200
    enun=f'Um chuveiro elétrico feito para instalações de {V:.0f}V, e com uma potência de {P:.0f} foi instalado em um circuito com disjuntor de 20A. Buscando saber se o circuito era adequado ao equipamento, calculou-se a corrente do mesmo, qual o valor obtido? o circuito é adequado?\nResposta:__________'
    gab=f'{P/V:.3f}A, {"Sim" if P/V<20 else "não"}'
    return[enun,gab]

def Q2():
    I=1*np.random.randint(1,5)
    Cores=['Preto','Marrom','Vermelho','Laranja','Amarelo','Verde','Azul','Violeta','Cinza','Branco']
    c1=np.random.randint(1,10)
    c2=np.random.randint(1,10)
    c3=np.random.randint(1,5)
    R=int(f'{c1}{c2}') *(10**c3)
    Cor1=Cores[c1]
    Cor2=Cores[c2]
    Cor3=Cores[c3]

    enun=f'Um resistor com as seguintes cores, terá uma resistência de quantos ohms?\n{Cor1} | {Cor2} | {Cor3} | Dourado\nResposta:__________'
    gab=f'{R} Ohms'
    return[enun,gab]

def Q3():
    V=6*np.random.randint(1,4)
    R=np.random.randint(12,67)*10
    P=(V**2)/R
    enun=f'Alimentando com uma fonte de {V:.0f} V, um resistor de {R:.0f} Ohms, ele irá aquecer, transformando energia elétrica em térmica com que potência?\nResposta:__________'
    gab=f'{P/V:.3f} W'
    return[enun,gab]

def Q4():
    V=5*np.random.randint(1,5)
    n=np.random.randint(2,5)
    R=np.random.randint(12,67)*10
    Req=R/n
    P=(V**2)/Req
    enun=f'Alimentando com uma fonte de {V:.0f} V, {n:.0f} resistores de {R:.0f} Ohms são conectados em paralelo. Qual a potência total consumida pelos resistores?\nResposta:__________'
    gab=f'{P/V:.3f} W'
    return[enun,gab]

def Q5():
    V=110*np.random.randint(1,3)
    P=np.random.randint(2,6)*1200
    R1=(V**2)/P
    R2=(V**2)/(P/2)
    enun=f'Um chuveiro elétrico de {P:.0f} W feito para instalações de {V:.0f} V, possui um seletor de inverno e verão. Na opção verão, o consumo cai pela metade. Qual o valor da resistência na opção inverno? e na opção verão? Resposta:__________'
    gab=f'Inverno: {R1:.2f} Ohms, Verão: {R2:.2f} Ohms'
    return[enun,gab]

def Q6():
    n=np.random.randint(8,20)
    tar=np.random.randint(74,86)/100
    h=np.random.randint(7,10)
    P=np.random.randint(10,14)*100
    E=P*n*h/1000
    val=E*tar
    enun=f'Um ar-condicionado de 7.500 Btus, tem em média {P:.0f} W. Um casal que ligue o ar-condicionado apenas em noites quentes, observou que em um mês de 31 dias, ligou o ar-condicionado apenas {n:.0f} vezes. Considerando a tarifa de {tar:.2f} R$/kW.h, o uso noturno de {h:.0f} horas. Qual será o valor, em reais, da conta de energia referente ao uso do ar-condicionado?\nResposta:__________'
    gab=f'R$ {val:.2f} '
    return[enun,gab]

def Q7():
    V=np.random.randint(1,3)*12
    Imax=np.random.randint(2,5)*10
    R=V/Imax
    enun=f'Uma bateria automotiva de {V:.0f}V e 60A.h, possui uma Amperagem de {Imax:.0f}A. Se a mesma fosse utilizada em um “ajuste técnico” para ligar uma sanduicheira elétrica, qual o valor mínimo de resistência elétrica da sanduicheira para que a bateria não fosse prejudicada (>{Imax:.0f}A)?'
    gab=f'R$ {R:.3f} '
    return[enun,gab]

def Q8(): 
    V=np.random.randint(1,3)*12
    R=10*np.random.randint(10,22)
    I=np.random.randint(1,8)*0.25
    N=np.ceil(I/(V/R))
    enun=f'Resistores de {R:.0f} Ohms são conectados em paralelo a uma fonte de {V:.0f}V. Quantos resistores deste valor devem ser associados em paralelo para que a corrente drenada da fonte seja maior que {I:.0f}A?'
    gab=f'{N:.0f} '
    return[enun,gab]

def Q9(): 
    P=1200*np.random.randint(2,7)
    V=110*np.random.randint(1,3)
    Ri=V*V/P
    Rv=V*V/(P/2)
    enun=f'Um chuveiro elétrico de {P:.0f} W feito para instalações de {V:.0f} V, possui um seletor de inverno e verão. Na opção verão, o consumo cai pela metade. Qual o valor da resistência na opção inverno? e na opção verão?'
    gab=f'Inverno:{Ri:.0f} - Verão: {Rv:.0f}'
    return[enun,gab]

