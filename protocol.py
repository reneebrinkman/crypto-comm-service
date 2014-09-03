import hashlib
import database

def unregistered_dataset():
	database.execute("SELECT email, codename FROM users WHERE registered = 0;")
	return database.fetchall()

def build_test_hash(userdata):
	return hashlib.sha512("%s %s" % (str(userdata[0]), str(userdata[1]))).hexdigest()
	
class CryptoProtocol(object):
	def register_device(self, registrar_key):
		keyfound_token = False
		for user in unregistered_dataset():
			if build_test_hash(user) == registrar_key:
				database.execute("UPDATE users SET registered = 1 WHERE codename = ?;", (str(user[1]),))
				keyfound_token = True
		return keyfound_token

