# -*- coding: UTF-8 -*-
import unicodedata
import re



def regraMarca(data):
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


def regraModelo(data):
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


def regraCor(data):
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


def regraCombustivel(data):
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


def regraDirecao(data):
    array = {'hidraulica', 'completo', 'competo','mecanica','mecam'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None and i=='hidraulica':
            contador = 1
            type = 'Hidráulica'
        if cont is not None and i=='competo':
            contador = 1
            type = 'Hidráulica'
        if cont is not None and i=='mecam':
            contador = 1
            type = 'Mecânica'
        if cont is not None and i=='mecanica':
            contador = 1
            type = 'Mecânica'
    if contador == 0:
        type = ''
        return type
    else:
        return type


def regraArcondicionado(data):
    array = {' ar ', 'arcondicionado', 'completo', 'competo'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type = 'Sim'
    if contador == 0:
        type = ''
        return type
    else:
        return type


def regraCambio(data):
    array = {'cambio', 'automatico'}
    contador = 0
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            type =i
    if contador == 0:
        type = ''
        return type
    else:
        return 'Manual'


def regraValor(data):
    preco = re.compile('([R$].[,.0-9]+.[,.0-9]{2,6})')
    valor = str(preco.findall(data))
    custo = valor.replace("'", "").replace('[', '').replace(']', '').replace('u', '')
    if custo == '':
        custo = ''
    return custo


def regraMotor(data):
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


def regraAno(data):
    expressao = re.compile('[^R$]+[" "](\d{1}\d{1})')
    ano = str(expressao.findall(data))
    ano = ano.replace("'", "").replace('[', '').replace(']', '').replace('u', '')
    if ano == '':
        ano = ''
    return ano


def regraModelo(data):
    array = {'Chevrollet', 'Fiat', 'BMW','Ford'}
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


def regraOpcionais(data):
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

def regraKm(data):
    expressao = re.compile('(\d{1}\d{1})[" "][km]')
    km = str(expressao.findall(data))
    km = km.replace("'", "").replace('[', '').replace(']', '').replace('u', '')
    if km == '':
        km = ''
    return km

def form(data):
    marca = regraMarca(data)
    modelo = regraModelo(data)
    preco = regraValor(data)
    motor = regraMotor(data)
    ano = regraAno(data)
    km = regraKm(data)
    direcao = regraDirecao(data)
    combustivel = regraCombustivel(data)
    cambio = regraCambio(data)
    valor = regraValor(data)
    ar = regraArcondicionado(data)
    cor = regraCor(data)
    opcionais = regraOpcionais(data)

    # return  valor
    return 'Marca: ' + marca + '\nModelo: '+modelo+'\nPreço: ' + preco + '\nMotor: ' + motor + '\nAno: ' + ano + '\nKm: ' + km + '\nCombustível: ' + combustivel + '\nCambio: ' + cambio + '\nDireçao: ' + direcao + '\nCor: ' + cor + '\nAr-cond: ' + ar + '\nOpcionais: ' + opcionais + '\n--------------'



def removerAcentos(palavra):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9$., \\\]', '', palavraSemAcento)