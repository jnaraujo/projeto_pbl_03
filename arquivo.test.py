import os
import arquivo



def test():
    currentPath = arquivo.getMainPath()

    assert currentPath == os.path.abspath(os.getcwd()), "Erro no caminho atual"

    arquivos = arquivo.getFoulderFilesPath(currentPath+"/pasta")

    assert len(arquivos) == 2, "Erro no número de arquivos"

    txt = arquivo.readFile(arquivos[0])

    txtList = arquivo.textToList(txt)

    assert txtList == ['teste', 'cavalo', 'cavalo', 'mesa', 'mesa', 'mesa', 'cavalo', 'cavalo-marinho', 'bom', 'dia', 'brasil'], "Erro na conversão de texto para lista"


    cWords = arquivo.countWords(txtList)

    assert cWords == {'teste': 1, 'cavalo': 3, 'mesa': 3, 'bom': 1, 'dia': 1, 'brasil': 1, 'cavalo-marinho': 1}, "Erro na contagem de palavras"

    arquivo.countDictToIndexFile(cWords, currentPath+"/indices/indice.txt")

    dicionario = arquivo.indexFileToDict(currentPath+"/indices/indice.txt")

    assert dicionario == cWords, "Erro na conversão de arquivo para dicionário"

    print(dicionario)




if __name__ == '__main__':
    test()