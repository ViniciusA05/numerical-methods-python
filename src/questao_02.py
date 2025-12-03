import numpy as np  

def metodo_bisseccao(f,a,b,iteracoes=21):
    """
    executa metodo da bisseccao com 21 iteracoes
    """

    if f(a)*f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos nos extremos a e b")
    
    historico = []
    raiz = (a + b)/2.0

    #loop fixo para rodar quantidade correta de vezes
    for _ in range(iteracoes):
        raiz = (a + b)/ 2.0
        historico.append(raiz)

        # faz o teste do sinal
        if f(a) * f(raiz) < 0 :
            b = raiz
        else:
            a = raiz

    return raiz,historico
