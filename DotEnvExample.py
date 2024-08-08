# This is a library that works like a lib with env variabnles and passwords
#   This crappy shit does not encrypt! it's the same as creating a dict in a .py file and importing the .py file

from dotenv import load_dotenv
import os

load_dotenv()
var1 = var2 = ""
var1 = os.getenv('SECRET_KEY')
print(var1)
var2 = os.getenv('DATABASE_URL')
print(var2)