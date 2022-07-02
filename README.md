# Sistema de busca e indexamento de documentos

Projeto criado como terceira avaliação da disciplina de MI de Algoritmos da Universidade Estadual de Feira de Santana.

## 🚀 Rodando localmente

1; Clone o projeto

```sh
git clone https://github.com/jnaraujo/projeto_pbl_03.git
```

2; Abra a pasta do projeto

```sh
cd projeto_pbl_03
```

3; Rode localmente

```sh
python main.py
```

## 💻 Tech Stack

1. Python

## Sobre o projeto

O projeto visa a criação de um sistema que permita ao usuário procurar palavras-chave em arquivos-texto previamente indexados.

Além disso, é possível remover diretórios e arquivos do índice; atualizar diretórios indexados; visualizar índices; etc.

Para tal, foi utilizado o conceito de índice invertido. Essa estrutura de dado permite que determinadas chaves sejam vinculadas ao local onde ela aparece.

Por exemplo:

```txt
jacaré -> /arquivos/animais.txt ; /notas/brasil.txt
```

Nesse exemplo, a palavra `jacaré` aparece em dois arquivos (animais.txt e brasil.txt).

Isso permite que a busca de palavras seja muito rápida. Por outro lado, a escrita pode se tornar lenta. Isso porque para escrever o índice invertido é necessário transformar o conteúdo do arquivo de texto em uma lista de palavras. Desse modo, em um diretório com milhares de arquivos, o sistema irá passar por todos eles.

Como consequência, o arquivo de índice criado cresce de acordo com o tamanho do diretório. A depender do tamanho do diretório original, o índice invertido pode ser até mesmo maior - isso porque é necessário salvar, além da palavra, o caminho do arquivo e quantidade de vezes que a palavra aparece.
