# -*- coding: UTF-8 -*-
import re
import sys


def base(array, data):
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = i
    if contador==0:
        type='Null'
        return type
    else:
        return type

def valor(data):
    preco = re.compile('([R$]+.[,.0-9]+.[,.0-9]{2,6})')
    return preco.findall(data)

# ta feio para caralho ajuste isso meu filho. Ass seu eu do passado!
def formulario(data):
    cor = {'prata', 'branca','branco' 'preto', 'azul'}
    comb = {'flex', 'alcool'}
    dir = {'hidráulica'}
    cambio = {}
    ar={'arcondicionado',' ar ',}
    camb={'cambio'}

    com = base(comb, data)
    color = base(cor, data)
    direcao=base(dir, data)
    cambio = base(camb, data)
    ar = base(ar, data)

    if direcao=='Null':
        direcao='Mecanica'
    if cambio=='Null':
        cambio='Normal'
    if ar=='Null':
        ar='Não'
    else:
        ar='Sim'
    if com=='Null':
        com='Gasolina'
    custo = str(valor(data))
    custo = custo.replace("'","").replace('[','').replace(']','')
    form = 'cor: '+color+'\ndirecao:  '+direcao+'\nArcond: '+ar+'\nCombustível: '+com+'\ncambio: '+cambio+'\nValor: '+custo
    return  form
