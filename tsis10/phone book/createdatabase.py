import psycopg2 as ps
import csv
from config import host, user, password, db_name




conn = ps.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE phone_book (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL
);
""")


    
conn.commit()


cur.close()
conn.close()