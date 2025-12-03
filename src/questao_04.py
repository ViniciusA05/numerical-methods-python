import numpy as np

def mapa_logistico(x,r):
    """
    funcao de iteracao do mapa logistico
    """

    x = r*x*(1-x)
    return x

def gera_dados_bifurcacao(r_min, r_max, r_steps=1000, transient=500, capture=100):
    """
    gera dados para o diagrama de bifurcacao

    parametros:
    r_min, r_max = Intervalo do eixo R
    r_steps = Quantos pontos R vamos testar
    transient = Quantas iteracoes descartar
    capture = Quantas iteracoes guardar para o grafico
    """

    # logica do professor
    total_points = int(r_steps * capture)
    buffer_r = np.zeros(total_points)
    buffer_diagrama = np.zeros(total_points)

    k=0  #contador para preencher o vetor linear

    #loop
    for i in range(r_steps):
        r = r_min + i * (r_max - r_min) / r_steps

        x = 0.1 #condicao inicial fixa

        #loop transient
        for j in range(transient):
            x = mapa_logistico(x,r)

        #loop capture
        for j in range(capture):
             x = mapa_logistico(x,r)
             buffer_r[k] = r
             buffer_diagrama[k] = x
             k+=1
    
    return buffer_r , buffer_diagrama

