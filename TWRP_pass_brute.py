#!/bin/python
import itertools
import os

password_symbols = 'qwertyuiopasdfghklzcvbnm' # Symbols that could be in your password
password_symbols_repeats = False # Replace to True if your password can contain a symbol multiple times.
password_length = 4 # Length of your password.

if password_symbols_repeats:
    res = list(map(lambda x: ''.join(x), itertools.combinations_with_replacement(password_symbols,password_length)))
else:
    res = list(map(lambda x: ''.join(x), itertools.combinations(password_symbols,password_length)))

combinations_total = len(res)

n = 0
for passw in res:
    n+=1
    print ("{}/{}: {}".format(n,combinations_total,passw))
    cmd_out = os.popen("adb shell twrp decrypt {}".format(passw)).read()
    if "Attempting to decrypt data partition via command line" not in cmd_out:
        print(cmd_out)
        print('\nSomething went wrong. Check connection to your device')
        break
    if 'Data successfully decrypted' in cmd_out:
        print ("\nYour password is: {}\nBye!".format(passw))
        break
else
    print("\nNo result.")
