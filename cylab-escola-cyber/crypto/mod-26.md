# Mod 26

**Autor:** Otavio Faria  
**Categoria:** Crypto / Cryptography  
**Plataforma:** CyLab Security Academy  
**Desafio:** [Mod 26](https://learn.cylabacademy.org/library/144)  
**Arquivo:** [values.txt](https://challenge-files.cylabacademy.net/library/4fcb791279e59f04dfab5d84570e0521973b63b01a5ba24cb69c7ea737cae863/values.txt)

## Objetivo

Decodificar o texto fornecido no anexo e recuperar a flag.

## Análise

O enunciado indica **ROT13**, uma cifra de substituição que desloca cada letra 13 posições no alfabeto de 26 letras. Ela preserva maiúsculas e minúsculas e mantém os números e símbolos.

Como dois deslocamentos de 13 completam 26 posições, a mesma operação serve para codificar e decodificar.

O anexo contém:

```text
npnqrzl{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_5p5s5o36}
```

O prefixo `npnqrzl` se transforma em `academy`, o que confirma a escolha da transformação para esta versão do desafio.

## Resolução

Após baixar `values.txt`, usar a implementação de ROT13 da biblioteca padrão do Python:

```python
from pathlib import Path
import codecs

texto = Path("values.txt").read_text().strip()
print(codecs.decode(texto, "rot_13"))
```

Também é possível reproduzir diretamente com o script desta entrega:

```bash
python scripts/resolver.py mod26
```

## Resultado

```text
academy{next_time_I'll_try_2_rounds_of_rot13_5c5f5b36}
```

[Registro da execução](../evidencias/mod26.txt).

## Conclusão

ROT13 pode ser reconhecido pelo padrão de substituição e não depende de uma chave secreta. Aplicá-lo duas vezes recupera o texto de entrada, portanto repetir a operação não aumenta a proteção.
