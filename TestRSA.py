from Crypto import Random
from Crypto.PublicKey import RSA
import base64
from random import randint
import os


def random(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def generate_keys():
	# RSA modulus length must be a multiple of 256 and >= 1024
	modulus_length = 256*8 # use larger value in production
	privatekey = RSA.generate(modulus_length, Random.new().read)
	publickey = privatekey.publickey()
	return privatekey, publickey

def encrypt_message(a_message , publickey):
	encrypted_msg = publickey.encrypt(a_message, 32)[0]
	encoded_encrypted_msg = base64.b64encode(encrypted_msg) # base64 encoded strings are database friendly
	return encoded_encrypted_msg

def decrypt_message(encoded_encrypted_msg, privatekey):
	decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
	decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
	return decoded_decrypted_msg
def Public_key():
	file = open('Public.pem', 'wb')
	file.write(publickey.exportKey())

def Private_key():
	file = open('Private.pem', 'wb')
	file.write(privatekey.exportKey())

def Encrypted_key():
	file = open('Encrypted_data.txt', 'w+')
	file.write(encrypted_msg)

def pin():
	file = open('Pin.txt', 'w+')
	pin = random(6)
	print "Your Pin is : %s " %(pin)
	file.write(str(pin))

def Read_Private_key():
	key = RSA.importKey(open("Private.pem", "rb"))
	print key
	return key
def Read_Public_key():
	key = RSA.importKey(open("Public.pem", "rb"))
	print key
	return key
def Read_Encrypted_msg():
	file = open('Encrypted_data.txt','r')
	text = file.read()
	print text
	return text
def getPin():
	file = open('Pin.txt','r')
	text = file.read()
	pin = int(text)
	return pin	
########## BEGIN ##########
while True:
	os.system('clear')
	print "====================Research and Development=============================================="
	print " "
	print " "
	print "Press (1) To generate keys and Encrypt String using Public Key and Gerenate a PIN "
	print " "
	print " "	
	print "Press (2) To Decrypt Using Private Key "
	print " "
	print " "
	print "Press (3) To Exit "
	print " "
	print " "	
	print "=========================================================================================="
	num = input("Enter a Number : ")
	if num == 1:
		print "*********Option 1 Selected**************"
		print " "
		a_message = raw_input("Enter a String to Encrypt : ")
		print "*********Generating Keys**************"	
		privatekey , publickey = generate_keys()
		print " ----Generating Private key---- "
		Private_key()
		print " "
		print " "	
		print " ----Generating Public key---- "
		Public_key()
		print "*********Encrypting String************"
		print " Original content: %s " % (a_message)	
		encrypted_msg = encrypt_message(a_message , publickey)
		Encrypted_key()
		print " "
		print " "		
		print "Message Encrypted Successfully "	
		print " "
		print " "
		print "*********Generating Pin***************"
		pin()
		print " "
		print " "
		print " "
		print " "
		print " "
		print " "
		print "**********Sending Email****************"
		os.system('python3 send_Pin.py')
		os.system('python3 send_Private_key.py')
		raw_input("Press Enter to continue...")
	elif num == 2:
		print "*********Option 2 Selected**************"
		print " "
		pin = input( "Please Enter The Pin To decrypt the Message : ")
		file_pin = getPin()
		if pin == file_pin:
			print " "
			print "Reading Private.key"
			privatekey = Read_Private_key()
			print " "
			#Publickey = Read_Public_key()
			print "Reading Encrypted Message"
			encrypted_msg =  Read_Encrypted_msg()
			print " "
			print "Decrypting Encrypted Message"
			decrypted_msg = decrypt_message(encrypted_msg, privatekey)
			print " "		
			print "Decrypted Message: %s " % (decrypted_msg)
			print " "
			print " "
			print " "
			print " "
			print " "
			print " "
			print " "
			print " "
			raw_input("Press Enter to continue...")
		else:
			print "Wrong Pin..........."
			raw_input("Press Enter to continue...")
	elif num == 3:
		break
	else:
		continue
else:
	print "Thank You"
