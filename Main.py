Operation = input("Do You Want to do encryption y/n\n")
if Operation == "y":
	import os
	from cryptography.fernet import Fernet
	
	files = []
	
	for file in os.listdir():
		if file == "encrypt.py" or file == "thekey.key" or 	file == "replit.nix" or file == ".replit" or file == 	"poetry.lock" or file == "pyproject.toml" or file == 	"decrypt.py" or file == "Main.py":
			continue
		if os.path.isfile(file):
			files.append(file)

	print(files)

	key = Fernet.generate_key()

	with open("thekey.key", "wb") as thekey:
		thekey.write(key)
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
			contents_encrypted = Fernet(key).encrypt(contents)
			with open(file, "wb") as thefile:
				print(contents)
				thefile.write(contents_encrypted)
else:
	import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "replit.nix" or file == ".replit" or file == "poetry.lock" or file == "pyproject.toml" or file == "decrypt.py" or file == "Main.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretpass = "PassMeFile"

user_phrase = input("what is the key?")
if user_phrase == secretpass:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("K your done - Decrypt")

