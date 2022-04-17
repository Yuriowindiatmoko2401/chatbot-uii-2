import pymysql
import petl as etl
import tabula, os


def main():
    workdir = os.getcwd()

    # Step Extraction
    df = tabula.read_pdf(workdir+"/sample-jadwal.pdf", pages='all')

    table_name = "jadwal_kuliah"

    conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            database='chatbot_uii',
            port=3306,
            connect_timeout=5
            )

    conn.cursor().execute('SET SQL_MODE=ANSI_QUOTES')

    # Step Transformasi
    df.columns = ['semester','konsentrasi','matakuliah','pengajar','hari','jam','status','catatan']
    ks = {'DS':'DATA SCIENCE', 'FD':'FORENSIKA DIGITAL', 'IM':'INFORMATIKA MEDIS', 'SIE':'SISTEM INFORMASI ENTERPRISE', 'Umum':'SEMUA'}
    df['ks']=df["konsentrasi"].map(ks)

    # Step Load DF to Table MySQL
    table = etl.fromdataframe(df)
    etl.todb(table, conn, table_name, create=True, drop=True)

    conn.close()



if __name__ == "__main__":
    main()