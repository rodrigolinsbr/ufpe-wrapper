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

def formulario(data):
    cor = {'prata', 'branca', 'preto', 'azul'}
    comb = {'flex', 'alcool'}
    dir = {'hidráulica'}
    cambio = {}
    ar={'arcondicionado'}
    camb={'cambio'}


    color = base(cor, data)
    direcao=base(dir, data)
    cambio=base(camb, data)
    custo = valor(data)
    form = 'cor: '+color+'\ndirecao:  '+direcao+'\ncambio: '+cambio+'\ncusto: '+str(custo)
    return  form
