"""
A thin wrapper around sqlite3 for the intents and purposes of this software.  Compatibility with larger database systems will be considered in the future.
"""
import sqlite3

conn = sqlite3.connect("dev.db")
c = conn.cursor()

def execute(sql, *args):
	c.execute(sql, *args)

def commit():
	conn.commit()

def fetchall():
	return c.fetchall()

def create_schema():
	execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, codename TEXT, registered INTEGER DEFAULT 0);")

def insert_testdata():
	execute("INSERT INTO users (email, codename) VALUES ('ben@benjaminbrinkman.com', 'solarflare');")

def initdb():
	create_schema()
	insert_testdata()
	commit()