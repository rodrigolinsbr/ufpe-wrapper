# -*- coding: UTF-8 -*-

import xlrd
import sys
import re
import functions
from functions import base
from functions import valor
from functions import formulario

reload(sys)
#sys.setdefaultencoding('utf-8')

anuncio = xlrd.open_workbook("corpus.xlsx")
pagina = anuncio.sheet_by_index(0)

row_index = [(4,5)]

anuncio_head_array = []
anuncio_body_array = []


for i,j in row_index:
    for k in range(1,11):
        #head
        #print pagina.cell_value(rowx=int(i),colx=k)
        head = pagina.cell_value(rowx=int(i),colx=k)
        anuncio_head_array.append(head)
        #body
        # print pagina.cell_value(rowx=int(j),colx=k)
        body = pagina.cell_value(rowx=int(j),colx=k)
        anuncio_body_array.append(body)

t1='flex, prata, vidro+trava+som'
t2='caravan 79 imp. R$ 9.900,00'
t3='vhv-e branco+direção hidráulica R$ 16.900,00'
t4='4p, preto, flex.'
t5 = 'mecanica da a20 6 cil: alcool com comando 250s e escap. 6x2 cambio 5 marchas R$ 25.000,00'
t6='v6, mecanica completa, azul R$ 24.500,00'
t7='flex, branca, mecam R$ 35.990,00'
t8='spirit preto, competo R$ 19.500,00'
t9='flex, prata, vidro+trava+som'



print("-----------------------")
print formulario(t6)
print("-----------------------")

# remail=re.compile('([_.0-9a-z-]+@[0-9a-z-]+.[a-z]{2,6})')


