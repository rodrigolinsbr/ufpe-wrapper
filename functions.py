# -*- coding: UTF-8 -*-
import unicodedata
import re



def regraModelo(data):
    array = {'CORSA CLASSIC', 'FIESTA HATCH', 'CARAVAN', 'CELTA LIFE',
             'CELTA SPIRIT', 'VERANEIO', 'BLAZER', 'AGILE', 'MUSTANG', 'FIESTA SEDAN', 'FOCUS',
             'KA', 'ESCORT SW', 'RANGER XL', 'ESCORT', 'BRAVO ESSENCE', 'STRADA ', 'VECTRA ELEGANCE 2008',
             'CHEVETTE L', 'VECTRA ELITE', 'NEW FIESTA','PALIO WEEKEND','STILO','FIORINO','COBALT LTX',
             'OMEGA GLS','S-10','P-306','CLIO AUTHENTIC','NISSAN SENTRA','VOYAGE','RANGER','RANGER XL',
             'CLASSE A','JOURNEY','RANGER XL','ESCORT','FIESTA','KA','FORD KA','NEW FIESTA HATCH',
             'ECOSPORT','ECOSPORT','COURIER','FIESTA CLASS','KA SE','FOCUS HATCH','KA SEL','ECOSPORT SE',
             'KA GL','DEL REY','ESCORT SW','COBALT LTX','OMEGA GLS','COURIER','FIESTA CLASS','S10',
             'ONIX LT','ASTRA ADVANEGE','CELTA SPIRIT','VECTRA ELEGANCE','CHEVETTE L','VECTRA ELITE','UNO',
             'S-10 KTZ','CLASSIC LS','ONIX','ONIX ACTIVE','MERIVA MAXX','PALIO FIRE ECONOMY','PUNTO','SIENA',
             'FIORINO','PALIO FIRE','SPACEFOX','STRADA ADVENT','FIESTA SEDAN','GRAND SIENA','PALIO ESSENC',
             'BRAVO ESSENCE','STRADA','PUNTO','PALIO FIRE','PALIO ELX','PALIO WEEKEEND','FOX HIGHLINE',
             'FUSCA','UNO MILLE FIRE','STRADA WORK','UNO VIVACE','UNO FIRE','UNO CS','ONIX ACTIV','GOL',
             'COBALT LTZ','COBALT LTX','VECTRA ELEGANCE','CELTA SPIRIT','ONIX ACTIVE','MERIVA','MERIVA MAXX',
             ''}
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
    array = {'prata', 'branca', 'branco', 'preto', 'preta', 'azul',
             'amarelo','vermelho','azul','vinho',''}
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
    array = {'hidraulica', 'completo','dh', 'competo','mecanica','mecam'}
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
    if(ano==''):
        expressao = re.compile('[^R$]+[" "](\d{1}\d{1}\d{1}\d{1})')
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
    array = {'radio', 'CD', 'MP3 Player', 'alarme', 'airbag','imp.','som','vidro','trava','escap.',
             'ipva pago','motor feito','couro','roda liga','mp3',
             'revisado','2 dono','trava eletrica','sensor','4pts','4pt',
             '2pts','4 portas','2 portas'}
    # adicionar variedades
    contador = 0
    opc = ""
    for i in array:
        cont = re.search(i, str(data))
        if cont is not None:
            contador = 1
            opc = i+" "+opc
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
    return re.sub('[^a-zA-Z0-9$., \\\]', ' ', palavraSemAcento)