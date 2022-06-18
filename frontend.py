import arquivo


currentPath = arquivo.getMainPath() # path da main do projeto
indexPath = currentPath+"\\indices\\" # local onde os indices serão armazenados

HELP = ""

def addDir(folderPath, output=True):
    folderPath = " ".join(folderPath)

    if not arquivo.doesPathExists(folderPath):
        if output==True:
            print("O diretório informado não existe.")
            print("Verifique se o caminho passado está correto e tente novamente.")
            print("Um exemplo de caminho válido: C:\\Users\\Antonio\\Documents\\pasta")
        return

    arquivos = arquivo.getFolderFilesPath(folderPath)

    palavrasDoArquivo = {}

    for path in arquivos:
        texto = arquivo.readFile(path)
        lista = arquivo.textToList(texto)

        countWords = arquivo.countWords(lista)

        for word, count in countWords.items():
            if word in palavrasDoArquivo:
                palavrasDoArquivo[word].append((path, count))
            else:
                palavrasDoArquivo[word] = [(path, count)]
    arquivo.saveIndexToFile(palavrasDoArquivo, folderPath, indexPath)

    if output==True:
        print("Diretório adicionado com sucesso!")

def updateDirs():
    indexes = arquivo.getFolderFilesPath(indexPath)
    print("----------- Lista de Diretórios para Atualizar -----------")
    for path in indexes:
        folderPath = arquivo.indexNameToPath(path, indexPath)

        print("Atualizando diretório: "+folderPath)
        addDir([folderPath], output=False)
        



def removeDir(args):
    folderPath = " ".join(args)

    # if not arquivo.doesPathExists(folderPath):
    #     print("O diretório informado não existe.")
    #     print("Verifique se o caminho passado está correto e tente novamente.")
    #     print("Um exemplo de caminho válido: C:\\Users\\Antonio\\Documents\\pasta")
    #     return

    status = arquivo.removeIndexPath(folderPath, indexPath)

    if not status:
        print("O diretório informado não está no indice.")
        print("Verifique se o caminho passado está correto e tente novamente.")
        print("Um exemplo de caminho válido: C:\\Users\\Antonio\\Documents\\pasta")
        return

    print("O diretório foi removido com sucesso do indice!")

def removeFile(args):
    filePath = " ".join(args)
    folderPath = "\\".join(filePath.split("\\")[:-1])

    folderPathName = folderPath.replace("\\", "__").replace(":", "__")+".txt"

    indexes = arquivo.getFolderFilesPath(indexPath)

    folderIndex = indexPath+folderPathName

    if folderIndex in indexes:
        dicionario = arquivo.indexFileToDict(folderIndex)
        
        for word, arr in dicionario.copy().items():
            for path, count in arr:
                if path == filePath: # se o arquivo for encontrado
                    arr.remove((path, count))
            
            if len(arr) == 0: # se o dicionário estiver vazio
                del dicionario[word]
            else:
                dicionario[word] = arr

        arquivo.saveIndexToFile(dicionario, folderPath, indexPath)
        print("Arquivo removido com sucesso do indice!")
        return
    print("O arquivo informado não está no indice.")
    print("Verifique se o caminho passado está correto e tente novamente.")
    print("Você pode verificar todos os diretórios no indice com a opção --listDirs")
def listDirs():
    print("----------- Lista de Diterórios -----------")
    indexes = arquivo.getFolderFilesPath(indexPath)
    for index in indexes:
        path = arquivo.indexNameToPath(index, indexPath)

        print(path)

def listFiles():
    print("----------- Lista de Arquivos Indexados -----------")
    indexes = arquivo.getFolderFilesPath(indexPath)

    files = []
    for path in indexes:
        dicionario = arquivo.indexFileToDict(path)

        for word, lista in dicionario.items():
            for value in lista:
                if value[0] not in files:
                    files.append(value[0])

    if len(files) == 0:
        print("Não há arquivos indexados.")
        print("Você pode adicionar arquivos com a opção --addDir")
        return
    
    for file in files:
        print(file)
def search(args):
    palavra = " ".join(args)

    reversedIndex = {}
    indexes = arquivo.getFolderFilesPath(indexPath)

    for path in indexes:
        dicionario = arquivo.indexFileToDict(path)
        for word, lista in dicionario.items():
            if word in reversedIndex:
                reversedIndex[word].append(*lista)
            else:
                reversedIndex[word] = lista


    res = arquivo.search(palavra, reversedIndex)

    if len(res) == 0:
        print("Não há arquivos com a palavra informada.")
        return
    else:
        print(f"----------- Lista de Arquivos com a palavra {palavra} -----------")
        for path, count in res:
            print(f"{path} ({count}x)")

def handleArgs(args):

    # comandos que nao precisam de argumentos adicionais
    if args[0] == '--listDirs':
        return listDirs()
    elif args[0] == '--listFiles':
        return listFiles()
    elif args[0] == '--help':
        return print(HELP) 
    elif args[0] == '--updateDirs':
        return updateDirs()

    if len(args) <= 1: # se não houver argumentos adicinais
        return print(HELP)

    if args[0] == '--addDir':
        return addDir(args[1:])
    elif args[0] == '--rmvDir':
        return removeDir(args[1:])
    elif args[0] == '--rmvFile':
        return removeFile(args[1:])
    elif args[0] == '--search':
        return search(args[1:])
    

def init(args):
    with open(currentPath+"/help.txt", "r", encoding="utf-8") as helpFile:
        global HELP
        HELP = helpFile.read()
    handleArgs(args)