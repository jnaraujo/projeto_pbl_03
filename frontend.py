from operator import index
import arquivo


currentPath = arquivo.getMainPath() # path da main do projeto
indexPath = currentPath+"\\indices\\" # local onde os indices serão armazenados

HELP = ""

def addDir(folderPath):
    folderPath = " ".join(folderPath)

    if not arquivo.doesPathExists(folderPath):
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

    print("Diretório adicionado com sucesso!")

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

def handleArgs(args):
    if len(args) <= 1:
        return print(HELP)

    if args[0] == '--addDir':
        addDir(args[1:])
    elif args[0] == '--rmvDir':
        removeDir(args[1:])
    elif args[0] == '--rmvFile':
        removeFile(args[1:])

def init(args):
    with open(currentPath+"/help.txt", "r") as helpFile:
        global HELP
        HELP = helpFile.read()
    handleArgs(args)