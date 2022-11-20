#DINESH N on 19.11.2022
#Random Password Generator
import random
def Password_Generator(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)
password=str()
for i in range(8):
  uppercaseLetter1=chr(random.randint(33,125))
  password += uppercaseLetter1
password = Password_Generator(password)
print(password)



