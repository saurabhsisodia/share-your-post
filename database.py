import mysql.connector
class make_connection(object):
	def __init__(self):
		DB_NAME="project"

		'create table'
		table=("CREATE TABLE entries(id  int(255) PRIMARY KEY auto_increment,title VARCHAR(255) not null,content LONGTEXT not null)")

		'establishing connections with mysql db'
		self.cnx=mysql.connector.connect(host="localhost",user="root",passwd="UBUNTU.123",database=DB_NAME)
		self.cursor=self.cnx.cursor()
		try:
			self.cursor.execute(table)
		except:
			pass
	def add_entry(self,data):
		add_user=("INSERT INTO entries (title,content)VALUES(%s,%s)")
		add_data=(data['title'],data['content'])
		self.cursor.execute(add_user,add_data)
		self.cnx.commit()

	def show_entries(self):
		command=("SELECT title,content from entries ORDER BY id DESC")
		self.cursor.execute(command)
		return self.cursor

