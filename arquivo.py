import os


def doesIndexFolderExists(indexPath): # verifica se o diretorio de index existe
    if not doesPathExists(indexPath):
        os.makedirs(indexPath)


def doesPathExists(path): # verifica se o caminho existe
    return os.path.exists(path) and not os.path.isfile(path) # se o caminho existe e não é um arquivo

def getFolderFilesPath(path): # retorna todos os arquivos de um diretorio
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))] # retorna todos os arquivos de um diretorio

def getMainPath(): # retorna o caminho do diretorio principal
    return os.path.abspath(os.getcwd())

def readFile(path): # le um arquivo e retorna o texto
    with open(path, "r", encoding="utf-8") as f: # abre o arquivo
        return f.read() # retorna o texto

def sanitize(text): # remove caracteres especiais
    stopChars = list("?!.,;:()[]{}<>\"'`´") # caracteres que não devem ser considerados
    words = text.replace("\n", " ") # substitui os \n por espaços

    for char in stopChars: # remove os caracteres especiais
        words = words.replace(char, "") # remove os caracteres especiais

    return words

def textToList(text): # transforma um texto em uma lista de palavras
    text = sanitize(text).strip().lower() # remove caracteres especiais e transforma em minusculo

    lista = text.split(" ") # divide o texto em uma lista de palavras

    return [word for word in lista if word != ""] # retorna uma lista de palavras sem espaços em branco

def countWords(lista): # conta o numero de palavras de uma lista
    d = {} # dicionario de palavras
    for word in lista: # para cada palavra da lista
        if word in d: # se a palavra ja existe
            d[word] += 1 # incrementa o numero de vezes que ela aparece
        else: # se a palavra nao existe
            d[word] = 1  # adiciona a palavra ao dicionario  
    return d

def saveIndexToFile(indexes, filename, savepath): # salva o index em um arquivo
    filename = filename.replace("\\", "__").replace(":", "__")+".txt" # troca os caracteres especiais

    with open(savepath+filename, "w", encoding="utf-8") as f: # abre o arquivo
        for key in indexes: # para cada chave do dicionario
            f.write(key + " " + str(indexes[key]) + "\n") # escreve a chave e o valor no arquivo

def indexFilenameToPath(filename): # retorna o caminho do arquivo de index
    return filename.replace("__", "\\").replace(".txt", "") # troca os caracteres especiais

def indexFileToDict(path): # transforma um arquivo de index em um dicionario
    d = {} # dicionario de palavras
    with open(path, "r", encoding="utf-8") as f: # abre o arquivo
        for line in f: # para cada linha do arquivo
            splitedLine = line.split(" ") # divide a linha em um array
            word, lista = splitedLine[0], " ".join(splitedLine[1:]) # pega a palavra e a lista de arquivos
            d[word] = eval(lista) # transforma a lista de arquivos em um array
    return d

def search(word, index): # busca um termo no index
    if word in index: # se o termo existe
        return sortIndex(index[word]) # retorna a lista de arquivos ordenada
    else: # se o termo nao existe
        return [] # retorna uma lista vazia

def sortIndex(arr): # ordena um array de arquivos
    arr = arr.copy() # copia o array

    isSorted = False # flag para saber se o array esta ordenado

    while not isSorted: # enquanto o array nao estiver ordenado
        isSorted = True # assume que o array esta ordenado
        for i in range(len(arr)-1): # para cada item do array
            current = arr[i] # pega o item atual
            next = arr[i+1] # pega o item seguinte

            if current[1] < next[1]: # se o item atual for maior que o seguinte
                arr[i], arr[i+1] = next, current # troca os itens
                isSorted = False # o array nao esta ordenado
    return arr


def removeIndexPath(folderPath, indexPath): # remove o caminho do index do caminho do diretorio
    filename = folderPath.replace("\\", "__").replace(":", "__")+".txt" # troca os caracteres especiais
    path = indexPath+filename # cria o caminho do arquivo
    if not doesPathExists(path): # se o arquivo nao existe
        return False 

    os.remove(path) # remove o arquivo
    return True


def indexNameToPath(name, indexPath): 

    if not str(indexPath).endswith("\\"): # se o caminho nao termina com um \
        indexPath += "\\" # adiciona um \ no final do caminho

    path = name.replace(indexPath, "").replace(".txt", "") # remove o caminho do index e o .txt

    path = path.replace("__", "\\") # troca os carecteres especiais
    path = path.split("\\") # divide o caminho em um array

    path[path.index("")] = ":" # no primeiro espaço em branco troca o caractere por :

    disk = path[0] # pega o disco
    path = "\\".join(path[1:]) # junta os outros itens do caminho

    path = disk+path # junta o disco com o caminho
    return path