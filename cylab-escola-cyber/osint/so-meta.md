# So Meta

**Autor:** Otavio Faria  
**Categoria da atividade:** OSINT  
**Categoria na plataforma:** Forensics  
**Plataforma:** CyLab Security Academy  
**Desafio:** [So Meta](https://learn.cylabacademy.org/library/19)  
**Arquivo:** [pico_img.png](https://challenge-files.cylabacademy.net/library/8179732d3bcbaaf9dadfc7fe08aa5b7fbf1d3189b0a2dc90eca34dca38a85b4a/pico_img.png)

## Objetivo

Encontrar a flag no arquivo de imagem fornecido.

## Análise

O título sugere investigar os metadados. Um PNG pode armazenar informações textuais como autor, programa usado e descrição. Esses dados podem revelar informações sem aparecer na imagem exibida.

Neste arquivo, a flag está em texto simples no campo `Artist`. O campo é armazenado em um bloco `tEXt` do PNG.

## Resolução

Após baixar o arquivo original, uma forma de examinar os metadados é:

```bash
exiftool pico_img.png
```

O campo relevante apresenta:

```text
Artist : academy{s0_m3ta_45015e26}
```

Para reproduzir sem instalar ExifTool:

```bash
python scripts/resolver.py so-meta
```

O script verifica a assinatura do PNG, percorre seus blocos e lê a entrada textual de nome `Artist`. Nenhuma decodificação adicional é necessária.

## Resultado

```text
Chunk PNG: tEXt
Metadado: Artist
Flag: academy{s0_m3ta_45015e26}
```

[Registro da execução](../evidencias/so-meta.txt).

## Conclusão

Metadados podem expor informações que não aparecem visualmente em um arquivo. A técnica é útil em OSINT para investigar artefatos disponíveis publicamente, embora o CyLab classifique este desafio como forense. Os campos são editáveis e, em uma investigação real, sua autoria precisaria de confirmação por outras fontes.
