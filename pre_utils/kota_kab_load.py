import pymysql
import petl as etl
import pandas as pd
import os


def main():
    workdir = os.getcwd()

    # Step Extraction
    df = pd.read_csv(workdir+"/kota-kab-indo.csv", pages='all')

    table_name = "kota_indo"

    conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            database='chatbot_uii',
            port=3306,
            connect_timeout=5
            )

    conn.cursor().execute('SET SQL_MODE=ANSI_QUOTES')

    # Step Transformasi
    df.columns = ['no','nama_kota','provinsi']

    # Step Load DF to Table MySQL
    table = etl.fromdataframe(df)
    etl.todb(table, conn, table_name, create=True, drop=True)

    conn.close()



if __name__ == "__main__":
    main()