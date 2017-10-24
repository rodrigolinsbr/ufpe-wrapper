# -*- coding: UTF-8 -*-

import xlrd
import csv
import sys
import re
import functions
from functions import base
from functions import form

reload(sys)
sys.setdefaultencoding('utf-8')

anuncio = xlrd.open_workbook("corpus.xlsx")
pagina = anuncio.sheet_by_index(0)

row_index = [(49,10)]

for i,j in row_index:
    for k in range(2,11):
        # print pagina.cell_value(rowx=int(i),colx=k)
        head = ''+pagina.cell_value(rowx=int(i),colx=k)
        # print head
        print form(head)
        # print regra_combustivel(head)



# remail=re.compile('([_.0-9a-z-]+@[0-9a-z-]+.[a-z]{2,6})')


