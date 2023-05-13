import sqlite3   
a = 'db.sqlite3' 
with sqlite3.connect(a) as sql:
    print(sql)
    delete = """ delete from shop_category where title='test2';"""
    sql.execute(delete)
    sql.commit()
  