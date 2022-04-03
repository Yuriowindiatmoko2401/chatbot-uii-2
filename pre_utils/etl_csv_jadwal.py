import pymysql
import petl as etl
import pandas as pd
import sys, os


def main():
	workdir = os.getcwd()
	path = sys.argv[1]
	table_name = sys.argv[2]

	conn = pymysql.connect(
	        host='127.0.0.1',
	        user='root',
	        database='chatbot_uii',
	        port=3306,
	        connect_timeout=5
	        )
	
	conn.cursor().execute('SET SQL_MODE=ANSI_QUOTES')

	df = pd.read_csv(workdir + '/' + path, error_bad_lines=False)
	df.columns = ['semester','konsentrasi','matakuliah','pengajar','hari','jam','status','catatan']
	ks = {'DS':'DATA SCIENCE', 'FD':'FORENSIKA DIGITAL', 'IM':'INFORMATIKA MEDIS', 'SIE':'SISTEM INFORMASI ENTERPRISE', 'Umum':'SEMUA'}
	df['ks']=df["konsentrasi"].map(ks)
	table = etl.fromdataframe(df)

	etl.todb(table, conn, table_name, create=True, drop=True)

	conn.close()

if __name__ == '__main__':
	main()
