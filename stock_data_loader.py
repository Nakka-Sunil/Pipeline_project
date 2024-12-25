import oracledb
from pipeline_requests import data_record

if data_record:
    try:
        connstr = 'user/password@host:1522/xepdb1'
        connection = oracledb.connect(connstr)
        cur = connection.cursor()

        statement = """
        INSERT INTO stock_data
        (trade_date, open_price, high_price, low_price, close_price, volume)
        VALUES (:1, :2, :3, :4, :5, :6)
        """
        
        cur.executemany(statement, data_record)

        connection.commit()
        
        print("Data inserted successfully.")
    except oracledb.Error as e:
        print("Error occurred while connecting to Oracle:", e)
    finally:
        cur.close()
        connection.close()
else:
    print("No data to insert.")
