# -*- coding: UTF-8 -*-
import unicodedata
import re



def regraModelo(data):
    array = {'CORSA CLASSIC', 'FIESTA HATCH', 'CARAVAN', 'CELTA LIFE',
             'CELTA SPIRIT', 'VERANEIO', 'BLAZER', 'AGILE', 'MUSTANG', 'FIESTA SEDAN', 'FOCUS',
             'KA', 'ESCORT SW', 'RANGER XL', 'ESCORT', 'BRAVO ESSENCE', 'STRADA ', 'VECTRA ELEGANCE 2008',
             'CHEVETTE L', 'VECTRA ELITE', 'NEW FIESTA','PALIO WEEKEND','STILO','FIORINO','COBALT LTX',
             'OMEGA GLS','S-10','P-306','CLIO AUTHENTIC','NISSAN SENTRA','VOYAGE','RANGER','RANGER XL',
             'CLASSE A','JOURNEY','FUSCA'}
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
    array = {'flex', 'alcool','gasolina','diesel','gvn'}
    # add disel e GVN
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
    # tentar melhorar comp*
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
    # add os outros
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
    preco = re.compile('([R$].[" "].[,.0-9]+.[,.0-9]{2,6})')
    valor = str(preco.findall(data))
    custo = valor.replace("'", "").replace('[', '').replace(']', '').replace('u', '')
    if custo == '':
        custo = ''
    return custo


def regraMotor(data):
    expressao = re.compile('(\s+\d{1}[.]+\d{1}\s)')
    motor = str(expressao.findall(data))
    motor = motor.replace("'", "").replace('[', '').replace(']', '').replace('u', '')
    return motor


def regraAno(data):
    expressao = re.compile('[^R$]+[" "](\d{1}\d{1})')
    # add 4 digitos
    ano = str(expressao.findall(data))
    ano = ano.replace("'", "").replace('[', '').replace(']', '').replace('u', '')
    return ano


def regraMarca(data):
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
    # adicionar variedades
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


    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9$., \\\]', '', palavraSemAcento)