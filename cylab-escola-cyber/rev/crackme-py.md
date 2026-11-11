# crackme-py

**Autor:** Otavio Faria  
**Categoria:** Rev / Reverse Engineering  
**Plataforma:** CyLab Security Academy  
**Desafio:** [crackme-py](https://learn.cylabacademy.org/library/175)  
**Arquivo:** [crackme_gen.py](https://challenge-files.cylabacademy.net/library/1eb77f4c882ea622da246f47b4359567016b423c143d85816ccd9c58d7e5d95b/crackme_gen.py)

## Objetivo

Analisar o programa Python fornecido e recuperar a informação escondida no código.

## Análise

O programa termina chamando `choose_greatest()`, que pede dois valores e mostra o maior. Essa interação não revela a flag. A parte relevante é a variável `bezos_cc_secret` e a função `decode_secret(secret)`.

A própria função identifica a transformação como **ROT47**. O alfabeto contém os 94 caracteres imprimíveis de `!` até `~`. Cada caractere avança 47 posições, voltando ao início quando necessário:

```python
original_index = (index + 47) % len(alphabet)
```

Como 47 é metade de 94, aplicar a transformação novamente recupera o texto original.

## Resolução

1. Abrir `crackme_gen.py` em um editor de texto.
2. Localizar `bezos_cc_secret` e `decode_secret`.
3. Trabalhar em uma cópia e substituir a última chamada `choose_greatest()` por:

```python
decode_secret(bezos_cc_secret)
```

4. Executar a cópia com Python 3. A função já implementada imprime o segredo decodificado.

Uma alternativa é usar o script desta entrega, que lê o segredo e aplica ROT47 sem executar o arquivo recebido:

```bash
python scripts/resolver.py crackme-py
```

## Resultado

```text
Segredo: 24256>JL`>0c0Abc?FE02a_53e7fe7af5gN
Transformação: ROT47
Flag: academy{1m_4_p34nut_a20db6f76f27d8}
```

[Registro da execução](../evidencias/crackme-py.txt).

## Conclusão

A análise do código mostrou que a interação principal desviava a atenção da função responsável pelo segredo. ROT47 é uma transformação reversível e sem chave secreta; deixar o valor e a rotina de decodificação no mesmo arquivo permite recuperar a informação.
