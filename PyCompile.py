from subprocess import call
import os
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
try:
	def compile():
		cmd1 = "cython --embed " + f
		cmd2 = "gcc $CFLAGS -I/usr/include/python3.8 -o " + outputName + " " + fc + " -lpython3.8 -lpthread -lm -lutil -ldl"
		call(cmd1, shell = True)
		call(cmd2, shell = True)
		import stat
		st = os.stat(outputName)
		oct_perm = oct(st.st_mode)
		oct_perm = str(oct_perm)
		print("***********")
		print(oct_perm[-3: ])
		print("***********")
		print("Permissions are listed. The output file has not been automatically marked for execution.")
		print("Successfully compiled.")
	f = str(input("Input the file name including the .pyx extension: "))
	fc = f.replace(".pyx", ".c")
	while ".pyx" not in f:
		f = str(input(".pyx not detected. Try again: "))
	obj = os.scandir(os.getcwd())
	print("Scanning for the .pyx...")
	entries = []
	for entry in obj:
		entries.append(entry.name)
	for i in range(0, len(entries)):
		if entries[i] == f:
			global outputName
			outputName = str(input("Please enter the desired output name: "))
			print("File found. Compiling...")
			found = 1
			compile()
			break
		else:
			continue
	try:
		if found == 1:
			pass
		else:
			pass
	except NameError:
		print("Sorry. File was not found.")
	exit(0)
except KeyboardInterrupt:
	print(f"{bcolors.HEADER}Thanks for using PyCompile.{bcolors.ENDC}")
	print(f"{bcolors.OKCYAN}Credit: The Enigma Project\n\n Twitter: @enigmapr0ject\n GitHub: @projectintel-anon\n Email: theenigmaproject@cyberservices.com\n\n\n {bcolors.BOLD}Stay safe, guardian.{bcolors.ENDC}")
except Exception as e:
	print("Exception has occurred. Please contact the developer and quote this:\n")
	print(f"{bcolors.FAIL}Error: {bcolors.ENDC}")
	print(repr(e))

