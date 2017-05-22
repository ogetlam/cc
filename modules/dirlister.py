import os 

def run(**args):
	print "[*] Dirlister module."
	files = os.listdir(".")
	return str(files)