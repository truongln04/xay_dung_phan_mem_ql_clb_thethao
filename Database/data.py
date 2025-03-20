import mysql.connector
from sqlalchemy import create_engine
def get_db_connection():
    """Kết nối đến cơ sở dữ liệu MySQL"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3308,  # Đảm bảo đúng port MySQL
            user="root",
            password="123456@Ab",
            database="QL_CLB_THE_THAO_CHUAN",
            auth_plugin='mysql_native_password'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Lỗi kết nối CSDL: {err}")
        return None


