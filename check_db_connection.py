import pymysql
# from models import Product
# from typing import Optional
# from sqlmodel import Field, Session, SQLModel, create_engine

# timeout = 10  # Set your desired timeout value
# HOST = "mysql-12c605c0-bhawna-aeb3.a.aivencloud.com"
# PORT = 10298
# USER = "avnadmin"
# PASSWORD = "AVNS_CZrlqhxcMzaiKVVTWwp"
# DB_NAME = "defaultdb"

connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-12c605c0-bhawna-aeb3.a.aivencloud.com",
  password="AVNS_CZrlqhxcMzaiKVVTWwp",
  read_timeout=timeout,
  port=10298,
  user="avnadmin",
  write_timeout=timeout,
)
# database_uri = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# engine = create_engine(database_uri)
# SQLModel.metadata.create_all(engine)
# product1  = Product(title = "Gift Card",body_html  = "test",price=10.0,stock=10,)
# with Session(engine) as session:
#     session.add(product1)
#     session.commit()

try:
  cursor = connection.cursor()
  cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
  cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
  cursor.execute("SELECT * FROM mytest")
  print(cursor.fetchall())
finally:
  connection.close()