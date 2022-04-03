# usage, python pdf_csv.py input output
import tabula, sys, os

workdir = os.getcwd()

tabula.convert_into(workdir + '/' + str(sys.argv[1]), workdir + '/' + str(sys.argv[2]), output_format="csv", pages='all')

