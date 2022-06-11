import os

def getFoulderFilesPath(path):
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def getMainPath():
    return os.path.abspath(os.getcwd())

def readFile(path):
    with open(path, "r") as f:
        return f.read()

def writeFile(path, text):
    with open(path, "w") as f:
        f.write(text)


def sanitize(text):
    words = text.replace("\n", " ")
    return words

def textToList(text):
    text = sanitize(text).strip()

    lista = text.split(" ")

    return [word for word in lista if word != ""]

def countWords(lista):
    d = {}
    for word in lista:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1     
    return d


def countDictToIndexFile(d, path):
    with open(path, "w") as f:
        for key in d:
            f.write(key + " " + str(d[key]) + "\n")

def indexFileToDict(path):
    d = {}
    with open(path, "r") as f:
        for line in f:
            word, count = line.split(" ")
            d[word] = int(count)
    return d