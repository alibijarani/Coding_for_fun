import random
import secrets
import string
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers ="0123456789"
symbols =",.-;:_!°§$%&//()==?`[{]}~]"
all =lower + upper + numbers + symbols
length = 16

# 1st  Way, Using random
password = "" .join(random.sample(all,length))
print(f" Random generated password :  {password}")


# 2nd Way , Using secrets library
all_chars = string.ascii_letters + string.digits  # All alphanumeric characters
length = 16

password = ''.join(secrets.choice(all) for _ in range(length))
print(f" Password generated with secrets module :  {password}")

