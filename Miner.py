import string
import secrets

print("""

███╗░░██╗██╗████████╗██████╗░░█████╗░  ░█████╗░░█████╗░██████╗░███████╗  ░██████╗░███████╗███╗░░██╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔════╝░██╔════╝████╗░██║
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░╚═╝██║░░██║██║░░██║█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░██╗██║░░██║██║░░██║██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚█████╔╝╚█████╔╝██████╔╝███████╗  ╚██████╔╝███████╗██║░╚███║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚════╝░░╚════╝░╚═════╝░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝
""")

def generate():
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	return ''.join(secrets.choice(chars) for x in range(18))

amount = input("Amount: ")
amount = int(amount)
count = 0

while amount > count:
	code = generate()
	print(code)
	save = open("nitro.txt", "a")
	save.write(f"{code}\n")
	save.close()
	count += 1