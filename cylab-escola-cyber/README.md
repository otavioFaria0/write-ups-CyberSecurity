# CyLab — Escola de Cyber

**Autor:** Otavio Faria  
**Data da verificação:** 11/11/2026  
**Plataforma:** [CyLab Security Academy](https://learn.cylabacademy.org/library?page=1)

Seis write-ups, com um desafio de cada categoria solicitada na atividade.

| Categoria da atividade | Desafio | Técnica | Write-up |
| --- | --- | --- | --- |
| Rev | crackme-py | Análise de código e ROT47 | [Ler](rev/crackme-py.md) |
| Misc | First Find | Busca de arquivo dentro de um ZIP | [Ler](misc/first-find.md) |
| Forense | information | Metadados XMP e Base64 | [Ler](forense/information.md) |
| Crypto | Mod 26 | Decodificação ROT13 | [Ler](crypto/mod-26.md) |
| Web | Cookies | Alteração do cookie `name` | [Ler](web/cookies.md) |
| OSINT | So Meta | Inspeção do campo `Artist` de um PNG | [Ler](osint/so-meta.md) |

`So Meta` está em OSINT para seguir o enunciado da atividade. Na biblioteca do CyLab, ele é classificado como **Forensics**. `First Find` aparece na plataforma como **General Skills**.

## Como reproduzir

Na pasta que contém este README, com Python 3 instalado:

```bash
python scripts/resolver.py crackme-py
python scripts/resolver.py first-find
python scripts/resolver.py information
python scripts/resolver.py mod26
python scripts/resolver.py so-meta
```

O script usa apenas a biblioteca padrão do Python, baixa o anexo oficial e exibe o resultado. Também aceita um arquivo já baixado, por exemplo:

```bash
python scripts/resolver.py information --arquivo cat.jpg
```

Para `Cookies`, abra o desafio, clique em **Launch Instance** e use a URL exibida:

```bash
python scripts/resolver.py cookies --url http://HOST:PORTA/
```

Substitua `HOST:PORTA` pela instância atual. No Linux, o executável pode se chamar `python3`; no Windows, `py`.

## Evidências e escopo da verificação

As flags documentadas foram obtidas dos anexos atuais do CyLab e, em `Cookies`, de uma requisição à instância do laboratório. Os [registros de execução](evidencias/) incluem a saída dos comandos e o SHA-256 dos anexos utilizados. O endereço de `Cookies` registrado na execução é temporário.

A verificação documentada é a extração das flags; não inclui uma nova submissão das respostas na plataforma. Não foram usados resultados de write-ups antigos como flags desta entrega.

## Entrega

Após revisar os seis textos, adicionar o link desta pasta à pasta pessoal no Teams: **Compartilhado → 003 - Escola de Cyber → pasta com seu nome**.

[Pasta desta atividade no GitHub](https://github.com/otavioFaria0/write-ups-CyberSecurity/tree/main/cylab-escola-cyber)
