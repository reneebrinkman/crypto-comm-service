import hashlib
import database
import bcrypt

def unregistered_dataset():
	database.execute("SELECT email, codename FROM users WHERE registered = 0;")
	return database.fetchall()

def build_test_hash(userdata):
	return hashlib.sha512("%s %s" % (str(userdata[0]), str(userdata[1]))).hexdigest()

def build_auth_hash(password):
	salt = bcrypt.gensalt()
	auth_hash = hashlib.sha512("%s%s" % (salt, password))
	return auth_hash, salt
	
class CryptoFactory(object):
	def register_user(self, registrar_key, password):
		keyfound_token = False
		for user in unregistered_dataset():
			if build_test_hash(user) == registrar_key:
				database.execute("UPDATE users SET registered = 1 WHERE codename = ?;", (str(user[1]),))
				auth_hash, salt = build_auth_hash(password)
				database.execute("UPDATE users SET auth_hash = ? WHERE codename = ?;", (auth_hash, str(user[1])))
				database.execute("UPDATE users SET salt = ? WHERE codename = ?;", (salt, str(user[1])))
				keyfound_token = True
		return keyfound_token
	