import os
import arquivo



def test2():
    currentPath = arquivo.getMainPath()

    assert currentPath == os.path.abspath(os.getcwd()), "Erro no caminho atual"

    arquivos = arquivo.getfolderFilesPath(currentPath+"/pasta")

    assert len(arquivos) == 2, "Erro no número de arquivos"

    txt = arquivo.readFile(arquivos[0])

    txtList = arquivo.textToList(txt)

    assert txtList == ['teste', 'cavalo', 'cavalo', 'mesa', 'mesa', 'mesa', 'cavalo', 'cavalo-marinho', 'bom', 'dia', 'brasil'], "Erro na conversão de texto para lista"

    cWords = arquivo.countWords(txtList)

    assert cWords == {'teste': 1, 'cavalo': 3, 'mesa': 3, 'bom': 1, 'dia': 1, 'brasil': 1, 'cavalo-marinho': 1}, "Erro na contagem de palavras"
    
    arquivo.saveIndexToFile(cWords, currentPath+"/indices/")


    


    
    
    # arquivo.countDictToIndexFile(cWords, currentPath+"/indices/indice.txt")

    # dicionario = arquivo.indexFileToDict(currentPath+"/indices/indice.txt")

    # assert dicionario == cWords, "Erro na conversão de arquivo para dicionário"
    indexFiles = arquivo.readIndexFiles()

    print(indexFiles)

    for path in indexFiles:
        print(arquivo.indexFilenameToPath(path))
    
    # print(dicionario)

def test_create_and_write_index():
    currentPath = arquivo.getMainPath()


    folderPath = currentPath+"/pasta"
    savePath = currentPath+"/indices/"

    arquivos = arquivo.getfolderFilesPath(folderPath)

    wordsOfFile = {}

    for path in arquivos:
        filename = path.split("/")[-1]

        texto = arquivo.readFile(path)

        lista = arquivo.textToList(texto)
        #wordsOfFile[filename]
        countWords = arquivo.countWords(lista)
        for word, count in countWords.items():
            if word in wordsOfFile:
                wordsOfFile[word].append((path, count))
            else:
                wordsOfFile[word] = [(path, count)]

    # print(wordsOfFile)
    arquivo.saveIndexToFile(wordsOfFile, folderPath, savePath)

def test_create_and_write_index_other_folder():
    currentPath = arquivo.getMainPath()

    savePath = currentPath+"/indices/"
    folderPath = "/home/jnaraujo/Documentos/testefiles/"


    arquivos = arquivo.getfolderFilesPath(folderPath)

    print(arquivos)

    wordsOfFile = {}

    for path in arquivos:
        filename = path.split("/")[-1]

        texto = arquivo.readFile(path)

        lista = arquivo.textToList(texto)
        #wordsOfFile[filename]
        countWords = arquivo.countWords(lista)
        for word, count in countWords.items():
            if word in wordsOfFile:
                wordsOfFile[word].append((path, count))
            else:
                wordsOfFile[word] = [(path, count)]

    # print(wordsOfFile)
    arquivo.saveIndexToFile(wordsOfFile, folderPath, savePath)

def test_read_index():
    reversedIndex = {}

    currentPath = arquivo.getMainPath()

    indexes = arquivo.getfolderFilesPath(currentPath+"/indices")

    for path in indexes:
        dicionario = arquivo.indexFileToDict(path)

        for word, lista in dicionario.items():
            if word in reversedIndex:
                reversedIndex[word].append(lista)
            else:
                reversedIndex[word] = [lista]

    # print(reversedIndex)

    res = arquivo.search("olá", reversedIndex)

    print("Locais onde a palavra aparece:")
    for item in res:
        path, count = item
        print(f"{path} - {count}x")
if __name__ == '__main__':
    # test_create_and_write_index()
    # test_create_and_write_index_other_folder()
    test_read_index()