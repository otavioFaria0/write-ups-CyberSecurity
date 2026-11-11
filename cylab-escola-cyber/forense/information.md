# information

**Autor:** Otavio Faria  
**Categoria:** Forense  
**Plataforma:** CyLab Security Academy  
**Desafio:** [information](https://learn.cylabacademy.org/library/186)  
**Arquivo:** [cat.jpg](https://challenge-files.cylabacademy.net/library/c585b4adbdaa06f409db7bf5012c2e58e9aab24669764a5f1cf0f9ce0d60dcfd/cat.jpg)

## Objetivo

Encontrar a flag escondida nas informações do arquivo de imagem.

## Análise

Um JPG pode armazenar metadados além dos pixels exibidos. No arquivo fornecido, o campo de licença dos metadados XMP contém uma sequência que pode ser decodificada em Base64.

O trecho relevante é:

```
<cc:license rdf:resource='YWNhZGVteXt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>
```

## Resolução

Uma ferramenta apropriada para inspecionar esses campos é o ExifTool:

```bash
exiftool cat.jpg
```

Após identificar o valor de `License`, decodificar a sequência com Python:

```python
import base64

valor = "YWNhZGVteXt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"
print(base64.b64decode(valor).decode())
```

A reprodução incluída nesta entrega faz as duas etapas sem depender do ExifTool: localiza o campo `cc:license` no arquivo e decodifica seu valor.

```bash
python scripts/resolver.py information
```

## Resultado

```text
Metadado: cc:license / rdf:resource
Base64: YWNhZGVteXt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Flag: academy{the_m3tadata_1s_modified}
```

[Registro da execução](../evidencias/information.txt).

## Conclusão

A flag estava nos metadados, sem necessidade de alterar a imagem ou analisar seus pixels. Base64 é uma codificação reversível, sem chave secreta. A inspeção dos metadados deve fazer parte da análise inicial de arquivos em desafios de forense.
