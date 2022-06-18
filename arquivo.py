import os


def doesPathExists(path):
    return os.path.exists(path) and not os.path.isfile(path)

def getFolderFilesPath(path):
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def getMainPath():
    return os.path.abspath(os.getcwd())

def readFile(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def writeFile(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def sanitize(text):
    stopChars = list("?!.,;:()[]{}<>\"'`´")
    words = text.replace("\n", " ")

    for char in stopChars:
        words = words.replace(char, "")

    return words

def textToList(text):
    text = sanitize(text).strip().lower()

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
    with open(path, "w", encoding="utf-8") as f:
        for key in d:
            f.write(key + " " + str(d[key]) + "\n")

def saveIndexToFile(indexes, filename, savepath):
    filename = filename.replace("\\", "__").replace(":", "__")+".txt"

    with open(savepath+filename, "w", encoding="utf-8") as f:
        for key in indexes:
            f.write(key + " " + str(indexes[key]) + "\n")

def indexFilenameToPath(filename):
    return filename.replace("__", "\\").replace(".txt", "")

def indexFileToDict(path):
    d = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            splitedLine = line.split(" ")
            word, lista = splitedLine[0], " ".join(splitedLine[1:])
            d[word] = eval(lista)
    return d
def readIndexFiles():
    path = getMainPath()+"\indices\\"

    indexDict = {}

    for file in os.listdir(path):
        if file.endswith(".txt"):
            indexDict[file] = indexFileToDict(path+file)

    return indexDict

def search(word, index):

    if word in index:
        return sortIndex(index[word])
    else:
        return []

def sortIndex(arr):
    arr = arr.copy()

    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(arr)-1):
            current = arr[i]
            next = arr[i+1]

            if current[1] < next[1]:
                arr[i], arr[i+1] = next, current
                isSorted = False
    return arr


def removeIndexPath(folderPath, indexPath):
    filename = folderPath.replace("\\", "__").replace(":", "__")+".txt"
    path = indexPath+filename
    if not doesPathExists(path):
        return False

    os.remove(path)
    return True


def indexNameToPath(name, indexPath):
    path = name.replace(indexPath, "").replace(".txt", "") # remove o caminho do index e o .txt
    path = path.replace("__", "\\") # troca os carecteres especiais
    path = path.split("\\") # divide o caminho em um array

    path[path.index("")] = ":" # no primeiro espaço em branco troca o caractere por :

    disk = path[0] # pega o disco
    path = "\\".join(path[1:]) # junta os outros itens do caminho

    path = disk+path # junta o disco com o caminho
    return path