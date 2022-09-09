import os,sys,time,getpass

a="TroyNeT"
b="Executive"


def sec():
	# Untuk Clear
	os.system("clear")
	# Login Logo
	os.system("figlet Login Sec")
	print ("")
	sec2()

def sec2():
	# Penginputan
	sec=input("Username : ")
	tok=getpass.getpass("Token : ")
	if sec == a and tok == b:
		print ("Access Login Success !")
		# Jeda Waktu
		time.sleep(2)
	# Kecuali
	else:
		print ("Access Denied Gagal !")
		time.sleep(4)
		# Python Nya Sesuaikam Nama File Kalian ✓
		os.system("python log.py")


sec()
