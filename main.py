# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import xlrd
import csv
import sys
import re
import functions
from functions import form

reload(sys)
sys.setdefaultencoding('utf-8')

anuncio = xlrd.open_workbook("corpus.xlsx")
pagina = anuncio.sheet_by_index(0)


row_index_body = [(48,10)]
for i, j in row_index_body:
    for k in range(2, 10):

        # print pagina.cell_value(rowx=int(i), colx=k)
        head = '' + pagina.cell_value(rowx=int(i), colx=k)+ ''+pagina.cell_value(rowx=int(i+1), colx=k)
        print  k-1
        print head
        print form(head)


# arq = open('form.txt', 'w')
# arq.write(head)
# arq.close()



# remail=re.compile('([_.0-9a-z-]+@[0-9a-z-]+.[a-z]{2,6})')


