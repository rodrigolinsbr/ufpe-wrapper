# -*- coding: UTF-8 -*-

import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

anuncio = xlrd.open_workbook("data.xlsx")
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
print(anuncio_head_array)
print("-----------------------")
print(anuncio_body_array)



