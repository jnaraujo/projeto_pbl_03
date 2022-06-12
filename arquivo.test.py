import os
import arquivo



def test2():
    currentPath = arquivo.getMainPath()

    assert currentPath == os.path.abspath(os.getcwd()), "Erro no caminho atual"

    arquivos = arquivo.getFoulderFilesPath(currentPath+"/pasta")

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

    arquivos = arquivo.getFoulderFilesPath(currentPath+"/pasta")

    wordsOfFile = {}

    for path in arquivos:
        filename = path.split("/")[-1]

        texto = arquivo.readFile(path)

        lista = arquivo.textToList(texto)
        #wordsOfFile[filename]
        countWords = arquivo.countWords(lista)
        for word, count in countWords.items():
            if word in wordsOfFile:
                wordsOfFile[word].append((filename, count))
            else:
                wordsOfFile[word] = [(filename, count)]

    # print(wordsOfFile)
    arquivo.saveIndexToFile(wordsOfFile, currentPath+"/indices/")

def test_read_index():
    reversedIndex = {}

    currentPath = arquivo.getMainPath()

    indexes = arquivo.getFoulderFilesPath(currentPath+"/indices")

    for path in indexes:
        dicionario = arquivo.indexFileToDict(path)
        print(dicionario)

    print(indexes)

if __name__ == '__main__':
    test_read_index()