# -*- coding: UTF-8 -*-
import re
import sys


def regra_marca(data):
    array={'Ford','Fiat'}
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

def regra_cor(data):
    array = {'prata', 'branca', 'branco' 'preto', 'azul'}
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

def regra_combustivel(data):
    array = {'flex', 'alcool'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = i
    if contador==0:
        type='Gasolina'
        return type
    else:
        return type

def regra_direcao(data):
    array = {'hidráulica','completo','competo'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = 'Hidráulica'
    if contador==0:
        type='Mecânica'
        return type
    else:
        return type

def regra_arcondicionado(data):
    array = {'ar','arcondicionado','completo','competo'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = 'Sim'
    if contador==0:
        type='Não'
        return type
    else:
        return type

def regra_cambio(data):
    array = {'cambio','completo','competo'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = 'Automático'
    if contador==0:
        type='Manual'
        return type
    else:
        return type

def regra_valor(data):
    preco = re.compile('([R$]+.[,.0-9]+.[,.0-9]{2,6})')
    valor = str(preco.findall(data))
    custo = valor.replace("'", "").replace('[', '').replace(']', '').replace('u', '')
    if custo=='':
        custo='Null'
    return custo


def form(data):
    marca='Null'
    modelo='Null'
    preco=regra_valor(data)
    motor='Null'
    ano='Null'
    km='Null'
    direcao=regra_direcao(data)
    combustivel=regra_combustivel(data)
    cambio = regra_cambio(data)
    valor = regra_valor(data)
    ar= regra_arcondicionado(data)
    cor=regra_cor(data)

    # return  valor
    return 'Marca: '+marca+'\nModelo: '+modelo+'\nPreço: '+preco+'\nMotor: '+motor+'\nAno: '+ano+'\nKm: '+km+'\nCambio: '+cambio+'\nDireçao: '+direcao+'\nCor: '+cor+'\nAr: '+ar+'\n---------------------------------------------'


def formulario(data):
    cor = {'prata', 'branca','branco' 'preto', 'azul'}
    comb = {'flex', 'alcool'}
    dir = {'hidráulica'}
    cambio = {}
    ar={'arcondicionado',' ar '}
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
