import string
import random
print("Welcome to genetor of password. The n3dh4ck3r!")
print("We are propose four length the password. W have the password the length 12,14,18,20.")
size = int(input("Please enter the password size you would like:"))

pol = string.ascii_letters + string.digits + string.punctuation
passw = random.choices(string.ascii_letters, k=10)
passw += random.choices(string.digits, k=5)
passw += random.choices(string.punctuation, k=5)
random.shuffle(passw)
while size not in [12,14,18,20]:
    print("The size of your password is incorrect:")
    size = int(input("Please enter the correct size of password: "))
passw = ''.join(random.choices(pol, k=size))
print(f"Here is your password:{passw}")
