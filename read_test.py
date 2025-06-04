from file_handler import FileHandler
import random
import time

file = FileHandler()



while True:
    print(file.get_last_line())
    time.sleep(0.5)