
import json
import random
def read_from_file():
    with open("wheel.json", 'r') as f:
        r1 = f.read()
        print(type(r1))
        w = json.loads(r1)


        print(w)


read_from_file()

#print (p, c)
#category, phrase = getRandomCategoryAndPhrase()