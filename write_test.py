from file_handler import FileHandler
import random
import time

file = FileHandler()


i = 0

while True:
    i += 1
    file.append_to_file(f"Sandun is {i} years old")
    time.sleep(0.5)