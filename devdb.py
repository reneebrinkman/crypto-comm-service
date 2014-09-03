import database

def create_schema():
	database.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, codename TEXT, auth_hash TEXT, salt TEXT, registered INTEGER DEFAULT 0);")

def insert_testdata():
	database.execute("INSERT INTO users (email, codename) VALUES ('ben@benjaminbrinkman.com', 'solarflare');")

def initdb():
	create_schema()
	insert_testdata()
	database.commit()
	
if __name__ == "__main__":
	initdb()