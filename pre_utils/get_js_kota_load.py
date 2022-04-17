import pymysql
import petl as etl
import pandas as pd
import requests


def main():

    # Step Extraction
    url = 'https://api.banghasan.com/sholat/kota/semua'
    header = {'Content-Type': 'application/json'}
    try:
        response = requests.get(url, headers=header)
    except Exception as e:
        raise e
    results = response.json()
    df = pd.DataFrame(results)

    table_name = "js_kota"
    conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            database='chatbot_uii',
            port=3306,
            connect_timeout=5
            )

    conn.cursor().execute('SET SQL_MODE=ANSI_QUOTES')

    # Step Transformasi
    df.columns = ['id','nama']

    # Step Load DF to Table MySQL
    table = etl.fromdataframe(df)
    etl.todb(table, conn, table_name, create=True, drop=True)

    conn.close()


if __name__ == "__main__":
    main()