# -*- coding: UTF-8 -*-
import re
import sys


def regra_marca(data):
    array = {'CORSA CLASSIC', 'CARAVAN', 'CELTA LIFE', 'CELTA SPIRIT', 'VERANEIO', 'BLAZER', 'AGILE'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = i
    if contador == 0:
        type = ''
        return type
    else:
        return type


def regra_modelo(data):
    array = {'CORSA CLASSIC', 'CARAVAN', 'CELTA LIFE', 'CELTA SPIRIT', 'VERANEIO', 'BLAZER', 'AGILE'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = i
    if contador == 0:
        type = ''
        return type
    else:
        return type


def regra_cor(data):
    array = {'prata', 'branca', 'branco', 'preto', 'preta', 'azul'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = i
    if contador == 0:
        type = ''
        return type
    else:
        return type


def regra_combustivel(data):
    array = {'flex', 'alcool','gasolina'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = i
    if contador == 0:
        type = ''
        return type
    else:
        return type


def regra_direcao(data):
    array = {'hidráulica', 'completo', 'competo'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = 'Hidráulica'
    if contador == 0:
        type = 'Mecânica'
        return type
    else:
        return type


def regra_arcondicionado(data):
    array = {' ar ', 'arcondicionado', 'completo', 'competo'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = 'Sim'
    if contador == 0:
        type = 'Não'
        return type
    else:
        return type


def regra_cambio(data):
    array = {'cambio', 'automático', 'automatico'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type =i
    if contador == 0:
        type = 'Manual'
        return type
    else:
        return type


def regra_valor(data):
    preco = re.compile('([R$].[,.0-9]+.[,.0-9]{2,6})')
    valor = str(preco.findall(data))
    custo = valor.replace("'", "").replace('[', '').replace(']', '').replace('u', '')
    if custo == '':
        custo = ''
    return custo


def regra_motor(data):
    # preco = re.compile('(\s+\d{1}[.]+\d{1}\s)')
    array = {'1.0', '4.3', '1.4', '4.3'}
    # array = {'prata', 'branca', 'branco' 'preto', 'azul'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = i
    if contador == 0:
        type = ''
        return type
    else:
        return type


def regra_ano(data):
    expressao = re.compile('[^R$]+[" "](\d{1}\d{1})')
    ano = str(expressao.findall(data))
    ano = ano.replace("'", "").replace('[', '').replace(']', '').replace('u', '')
    if ano == '':
        ano = ''
    return ano


def regra_modelo(data):
    marca = regra_marca(data)
    array = {'CORSA CLASSIC', 'CARAVAN', 'CELTA LIFE', 'CELTA SPIRIT', 'VERANEIO', 'BLAZER', 'AGILE'}
    if marca=='CORSA CLASSIC' or marca=='CARAVAN' or marca=='CELTA LIFE' or marca=='CELTA SPIRIT':
        modelo='Chevrollet'
    elif marca=='AGILE' or marca=='UNO':
        modelo='Fiat'
    elif marca=='BLAZER' or marca=='VERANEIO':
        modelo='Ford'
    else:
        modelo=''

    return modelo


def regra_opcionais(data):
    array = {'radio', 'CD', 'MP3 Player', 'alarme', 'airbag'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            opc = ''
    if contador == 0:
        opc = ''
        return opc
    else:
        return opc


def form(data):
    marca = regra_marca(data)
    modelo = regra_modelo(data)
    preco = regra_valor(data)
    motor = regra_motor(data)
    ano = regra_ano(data)
    km = ''
    direcao = regra_direcao(data)
    combustivel = regra_combustivel(data)
    cambio = regra_cambio(data)
    valor = regra_valor(data)
    ar = regra_arcondicionado(data)
    cor = regra_cor(data)
    opcionais = regra_opcionais(data)

    # return  valor
    return 'Marca: ' + marca + '\nModelo: '+modelo+'\nPreço: ' + preco + '\nMotor: ' + motor + '\nAno: ' + ano + '\nKm: ' + km + '\nCombustível: ' + combustivel + '\nCambio: ' + cambio + '\nDireçao: ' + direcao + '\nCor: ' + cor + '\nAr-cond: ' + ar + '\nOpcionais: ' + opcionais + '\n--------------'


def formulario(data):
    cor = {'prata', 'branca', 'branco' 'preto', 'azul'}
    comb = {'flex', 'alcool'}
    dir = {'hidráulica'}
    cambio = {}
    ar = {'arcondicionado', ' ar '}
    camb = {'cambio'}

    com = base(comb, data)
    color = base(cor, data)
    direcao = base(dir, data)
    cambio = base(camb, data)
    ar = base(ar, data)

    if direcao == 'Null':
        direcao = 'Mecanica'
    if cambio == 'Null':
        cambio = 'Normal'
    if ar == 'Null':
        ar = 'Não'
    else:
        ar = 'Sim'
    if com == 'Null':
        com = 'Gasolina'
    custo = str(valor(data))
    custo = custo.replace("'", "").replace('[', '').replace(']', '')
    form = 'cor: ' + color + '\ndirecao:  ' + direcao + '\nArcond: ' + ar + '\nCombustível: ' + com + '\ncambio: ' + cambio + '\nValor: ' + custo
    return form
