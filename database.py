import MySQLdb


class database():


  def __init__(self):
    # Open database connection
    self.db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

    # prepare a cursor object using cursor() method
    self.cursor = self.db.cursor()




  def insert(self, name, personId):
     # Prepare SQL query to INSERT a record into the database.
    sql ="INSERT INTO faceslist(Name, personId) VALUES ('%s', '%s')" % (name, personId)
    db = self.db
    try:
      # Execute the SQL command
      self.cursor.execute(sql)
      # Commit your changes in the database
      db.commit()
    except:
      # Rollback in case there is any error
      db.rollback()

    # disconnect from server
    db.close()