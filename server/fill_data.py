import random
import string
import time

STRING_LENGTH = 100

file_object = open(r"data.txt", "a")

for i in range(1500):
    res = "".join(random.choices(string.ascii_letters + string.digits, k=STRING_LENGTH))
    res = "{} \n".format(res)
    file_object.write(res)
    # time.sleep(0.1)


file_object.close()
