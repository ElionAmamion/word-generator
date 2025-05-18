import random as r

def word():
    start = r.choice(["b", "d", "c"])

    vocala = r.choice(["a", "o", "i"])

    mid = r.choice(["m", "n"])

    vocalb = r.choice(["e", "u"])

    ra = r.randint(1, 2)

    if ra == 1:
        word = start + vocala + mid
    else:
        word = start + vocala + mid + vocalb

    return word

try:
    with open("words.txt", "x") as w:
        for i in range(25):
            w.write(word()+ "\n")
except FileExistsError:
    with open("words.txt", "a") as w:
        for i in range(25):
            if i < 25-1:
                w.write(word()+ "\n")
            else:
                w.write(word())