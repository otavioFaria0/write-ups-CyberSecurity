# First Find

**Autor:** Otavio Faria  
**Categoria:** Misc / General Skills  
**Plataforma:** CyLab Security Academy  
**Desafio:** [First Find](https://learn.cylabacademy.org/library/320)  
**Arquivo:** [files.zip](https://challenge-files.cylabacademy.net/library/72ca8cb60e55a597886dfb8e20bdb28d3ea7e73ca72987eb813a3558a8dd22bf/files.zip)

## Objetivo

Localizar o arquivo `uber-secret.txt` dentro do ZIP fornecido e ler seu conteúdo.

## Análise

O nome do arquivo procurado é informado no enunciado. Uma busca pelo nome resolve o desafio sem abrir manualmente cada pasta. O caminho contém o diretório `.secret`, que costuma ficar oculto em listagens comuns no Linux.

## Resolução

Em um terminal Linux, após baixar o anexo:

```bash
unzip files.zip -d extraido
find extraido -type f -name 'uber-secret.txt'
```

A busca encontra:

```text
extraido/files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

O comando `find` também percorre diretórios cujos nomes começam com ponto. Para ler o arquivo encontrado:

```bash
cat extraido/files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

Para reproduzir no Windows ou Linux sem instalar ferramentas adicionais além de Python 3:

```bash
python scripts/resolver.py first-find
```

Esse script consulta a lista de arquivos do ZIP e lê diretamente a entrada `uber-secret.txt`, sem precisar extrair todo o conteúdo.

## Resultado

```text
academy{f1nd_15_f457_ab443fd1}
```

[Registro da execução, com o caminho encontrado](../evidencias/first-find.txt).

## Conclusão

Uma busca recursiva por nome permite localizar rapidamente arquivos em estruturas grandes. Uma pasta oculta altera a forma como o conteúdo é exibido, mas não fornece proteção contra leitura ou pesquisa.
