import json
import random
from typing import Iterable
"""
def sample(items:Iterable[str], k: int):
    s = []
    for x in items:
        if x.isascii():
            s.append(x)
"""
def letter2star(s:str, exceptions:Iterable[str]):
    return "".join(c if not c.isalpha() or c in exceptions else "*" for c in s)

info = json.load(open("Phigros.json"))
ascii_info = {}
for x in info.keys():
    if x.isascii():
        ascii_info[x] = info[x]
sam = random.sample(sorted(ascii_info.keys()),10)
exc = []
correct_list = []
def display(correct:Iterable[int], exceptions:Iterable[str]):
    for x,y in enumerate(sam):
        if not x+1 in correct:
            print(x+1,letter2star(y,exceptions),"IN Lv.",ascii_info[y]["chart"]["IN"]["level"])
        else:
            print(x+1,y,"IN Lv.",ascii_info[y]["chart"]["IN"]["level"])


while True:
    display([1,2,3,4,5,6,7,8,9,10],[])
    print()
    display(correct_list,exc)
    print()
    ch = input("Please input: ")
    if ch.isascii() and not ch.isdigit():
        exc.append(ch.upper())
        exc.append(ch.lower())
    elif ch.isdigit():
        correct_list.append(int(ch))
    else:
        print("Illegal Input! ")
    print()
