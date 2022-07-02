import arquivo

import os

currentPath = arquivo.getMainPath() # path da main do projeto
indexPath = os.path.join(currentPath, "indices\\") # local onde os indices serão armazenados

arquivo.doesIndexFolderExists(indexPath) # verifica se o diretório de indices existe

HELP = ""

'''
    Função que adiciona um diretório do indice
'''
def addDir(folderPath, output=True):
    folderPath = " ".join(folderPath) # pega o path do diretório

    if not arquivo.doesPathExists(folderPath): # se o caminho não existe
        if output==True: # se for para imprimir na tela
            print("O diretório informado não existe.")
            print("Verifique se o caminho passado está correto e tente novamente.")
            print("Um exemplo de caminho válido: C:\\Users\\Antonio\\Documents\\pasta")
        return 0

    arquivos = arquivo.getFolderFilesPath(folderPath) # pega todos os arquivos do diretório

    palavrasDoArquivo = {} # dicionário que armazena as palavras do arquivo

    for path in arquivos: # para cada arquivo do diretório
        texto = arquivo.readFile(path) # le o arquivo
        lista = arquivo.textToList(texto) # transforma o texto em uma lista
 
        countWords = arquivo.countWords(lista) # conta as palavras do arquivo

        for word, count in countWords.items(): # para cada palavra e seu número de ocorrências
            if word in palavrasDoArquivo: # se a palavra já existir no dicionário
                palavrasDoArquivo[word].append((path, count)) # adiciona o arquivo e o número de ocorrências
            else:
                palavrasDoArquivo[word] = [(path, count)] # se não, adiciona a palavra e a lista de arquivos e o número de ocorrências
    
    arquivo.saveIndexToFile(palavrasDoArquivo, folderPath, indexPath) # salva o dicionário no arquivo de indice

    if output==True: # se for para imprimir na tela
        print("Diretório adicionado com sucesso!")
    return 1

'''
    Função que atualiza o indice de todos os diretórios
'''
def updateDirs():
    indexes = arquivo.getFolderFilesPath(indexPath) # pega todos os arquivos indexados

    if len(indexes) == 0: # se não houver arquivos indexados
        print("Não há arquivos indexados.")
        print("Você pode adicionar arquivos com a opção --addDir")
        return

    for path in indexes: # para cada arquivo indexado
        folderPath = arquivo.indexNameToPath(path, indexPath) # pega o path do diretório

        status = addDir([folderPath], output=False) # atualiza o indice do diretório

        if status == 0: # o diretório não existe/mudou de nome
            print("-"*70)
            print("O diretório ({}) não existe ou mudou de nome.".format(folderPath))
            print("Você pode adicionar o diretório com a opção --addDir")
            print("Ou você pode remover o diretório com a opção --rmvDir")
            print("Um exemplo de caminho válido: C:\\Users\\Antonio\\Documents\\pasta")
            print("-"*70)
        else:
            print("Diretório atualizado: "+folderPath)

def showIndex(args):
    folderPath = " ".join(args) # pega o path do diretório
    indexFileName = folderPath.replace("\\", "__").replace(":", "__")+".txt" # nome do arquivo de indice

    folderIndexPath = os.path.join(indexPath, indexFileName)

    if not arquivo.doesFileExists(folderIndexPath): # verifica se o caminho existe
        print("O diretório informado não está no índice.")
        print("Verifique se o caminho passado está correto e tente novamente.")
        print("Você pode adicionar o diretório com a opção --addDir")
        print("Um exemplo de caminho válido: C:\\Users\\Antonio\\Documents\\pasta")
        return

    print("----------- Índice do diretório -----------")
    indexes = arquivo.indexFileToDict(folderIndexPath) # pega o dicionário do arquivo de indice

    for word, files in indexes.items():
        print(word, "> " ,end="")
        contador = 0
        for file, count in files:
            filename = file.split("\\")[-1]
            if contador == 0:
                print("{} ({}x)".format(filename, count), end="")
            else:
                print(", {} ({}x)".format(filename, count), end="")
            contador+=1
        print()

'''
    Função que remove um diretório do indice
'''
def removeDir(args):
    folderPath = " ".join(args) # pega o path do diretório

    if not arquivo.doesPathExists(folderPath): # verifica se o caminho existe
        print("O diretório informado não existe.")
        print("Verifique se o caminho passado está correto e tente novamente.")
        print("Um exemplo de caminho válido: C:\\Users\\Antonio\\Documents\\pasta")
        return
    status = arquivo.removeIndexPath(folderPath, indexPath) # remove o diretório do indice

    if not status: # se o diretório não existir
        print("O diretório informado não está no indice.")
        print("Verifique se o caminho passado está correto e tente novamente.")
        print("Um exemplo de caminho válido: C:\\Users\\Antonio\\Documents\\pasta")
        return

    print("O diretório foi removido com sucesso do indice!")

'''
    Função que remove um arquivo do indice
'''
def removeFile(args):
    filePath = " ".join(args) # pega o path do arquivo
    folderPath = "\\".join(filePath.split("\\")[:-1]) # pega o path do diretório

    folderPathName = folderPath.replace("\\", "__").replace(":", "__")+".txt" # pega o nome do arquivo de indice

    indexes = arquivo.getFolderFilesPath(indexPath) # pega todos os arquivos indexados

    folderIndex = indexPath+folderPathName # cria o caminho do arquivo de indice

    if folderIndex in indexes: # se o caminho existir no indice
        dicionario = arquivo.indexFileToDict(folderIndex) # transforma o arquivo do indice em um dicionario
        
        for word, arr in dicionario.copy().items(): # para cada (palavra, lista) do dicionario
            for path, count in arr: # para cada valor da lista
                if path == filePath: # se o arquivo for encontrado
                    arr.remove((path, count)) # remove o arquivo da lista

            if len(arr) == 0: # se o dicionário estiver vazio
                del dicionario[word] # remove a palavra do dicionário
            else:
                dicionario[word] = arr # se não, atualiza o dicionário

        arquivo.saveIndexToFile(dicionario, folderPath, indexPath) # salva o dicionário no arquivo de indice
        print("Arquivo removido com sucesso do indice!")
        return
    print("O arquivo informado não está no indice.")
    print("Verifique se o caminho passado está correto e tente novamente.")
    print("Você pode verificar todos os diretórios no indice com a opção --listDirs")

def listDirs():
    print("----------- Lista de Diterórios -----------")
    indexes = arquivo.getFolderFilesPath(indexPath) # pega todos os arquivos indexados
    if len(indexes) == 0: # se não houver arquivos indexados
        print("Não há diretórios indexados.")
        print("Você pode adicionar diretórios com a opção --addDir")
        return
    for index in indexes: # para cada arquivo indexado
        path = arquivo.indexNameToPath(index, indexPath) # pega o path do diretório
        print(path) # imprime o path do diretório

'''
    Função que retorna a lista de aquivos indexados
'''
def listFiles():
    print("----------- Lista de Arquivos Indexados -----------")
    indexes = arquivo.getFolderFilesPath(indexPath) # pega todos os arquivos indexados

    files = []
    for path in indexes: # para cada arquivo indexado
        dicionario = arquivo.indexFileToDict(path)# transforma o arquivo do indice em um dicionario

        for word, lista in dicionario.items(): # para cada (palavra, lista) do dicionario
            for value in lista: # para cada valor da lista
                if value[0] not in files: # se o path do arquivo não estiver na lista
                    files.append(value[0]) # adiciona o path do arquivo na lista

    if len(files) == 0: # se não houver arquivos indexados
        print("Não há arquivos indexados.")
        print("Você pode adicionar diretórios com a opção --addDir")
        return
    
    for file in files: # para cada arquivo indexado
        print(file)

'''
    Função que busca por palavras no indice
'''
def search(args):
    palavra = " ".join(args) # pega a palavra a ser buscada e junta ela

    reversedIndex = {} # dicionário que irá conter as palavras do indice invertido
    indexes = arquivo.getFolderFilesPath(indexPath) # pega todos os indices salvos

    for path in indexes: # para cada indice
        dicionario = arquivo.indexFileToDict(path) # transforma o arquivo do indice em um dicionario
        for word, lista in dicionario.items(): # para cada (termo, ocorrencias) do dicionario
            if word in reversedIndex: # se a palavra já existir no dicionario invertido
                reversedIndex[word] += lista # adiciona a lista de ocorrencias
                # adiciona a ocorrencia na lista
            else:
                reversedIndex[word] = lista # se a palavra não existir, adiciona a palavra e a ocorrencia na lista


    res = arquivo.search(palavra, reversedIndex) # busca a palavra no dicionario invertido e retorna uma lista ordenada por quantidade de ocorrencias

    if len(res) == 0: # se não encontrar nenhum resultado
        print("Não há arquivos com a palavra informada.")
        return
    else: # se encontrar algum resultado
        print(f"----------- Lista de Arquivos com a palavra {palavra} -----------")
        for path, count in res: # para cada resultado
            print(f"{path} ({count}x)") # imprime o caminho do arquivo e a quantidade de ocorrencias

'''
    Função que trata com os argumentos passados na linha de comando
'''
def handleArgs(args):
    if len(args) == 0: # se não houver argumentos
        print(HELP)
        return

    # comandos que nao precisam de argumentos adicionais
    if args[0] == '--listDirs': # lista os diretórios indexados
        return listDirs()
    elif args[0] == '--listFiles': # lista os arquivos indexados
        return listFiles()
    elif args[0] == '--help': # mostra a ajuda
        return print(HELP) 
    elif args[0] == '--updateDirs': # atualiza os diretórios indexados
        return updateDirs()

    if len(args) <= 1: # se não houver argumentos adicinais
        return print(HELP)

    if args[0] == '--addDir': # adiciona ou atualiza um diretório ao indice
        return addDir(args[1:])
    elif args[0] == '--rmvDir': # remove um diretório do indice
        return removeDir(args[1:]) 
    elif args[0] == '--rmvFile': # remove um arquivo do indice
        return removeFile(args[1:])
    elif args[0] == '--showIndex': # mostra o indice do diretório
        return showIndex(args[1:])
    elif args[0] == '--search': # busca por palavras no indice
        return search(args[1:])
    else:
        return print(HELP)
    

def init(args):
    with open(currentPath+"/help.txt", "r", encoding="utf-8") as helpFile: # le o arquivo de ajuda
        global HELP # globaliza a ajuda
        HELP = helpFile.read() # seta HELP como o conteúdo do arquivo
    handleArgs(args) # chama a função de tratamento de argumentos