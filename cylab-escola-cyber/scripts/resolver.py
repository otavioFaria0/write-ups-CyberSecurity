#!/usr/bin/env python3
"""Reproduz seis resoluções do CyLab com a biblioteca padrão do Python 3."""
import argparse
import ast
import base64
import codecs
import hashlib
import html
import http.cookiejar
import io
import re
import struct
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

SOURCES = {
    "crackme-py": "https://challenge-files.cylabacademy.net/library/1eb77f4c882ea622da246f47b4359567016b423c143d85816ccd9c58d7e5d95b/crackme_gen.py",
    "first-find": "https://challenge-files.cylabacademy.net/library/72ca8cb60e55a597886dfb8e20bdb28d3ea7e73ca72987eb813a3558a8dd22bf/files.zip",
    "information": "https://challenge-files.cylabacademy.net/library/c585b4adbdaa06f409db7bf5012c2e58e9aab24669764a5f1cf0f9ce0d60dcfd/cat.jpg",
    "mod26": "https://challenge-files.cylabacademy.net/library/4fcb791279e59f04dfab5d84570e0521973b63b01a5ba24cb69c7ea737cae863/values.txt",
    "so-meta": "https://challenge-files.cylabacademy.net/library/8179732d3bcbaaf9dadfc7fe08aa5b7fbf1d3189b0a2dc90eca34dca38a85b4a/pico_img.png",
}


def read_source(challenge, local_file):
    if local_file:
        data = Path(local_file).read_bytes()
        print("Arquivo:", Path(local_file).name)
    else:
        url = SOURCES[challenge]
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
        print("Fonte:", url)
    print("SHA-256:", hashlib.sha256(data).hexdigest())
    return data


def solve_file(challenge, data):
    if challenge == "crackme-py":
        # Lê somente o literal da variável; não executa o programa recebido.
        tree = ast.parse(data.decode("utf-8"))
        secret = next(
            ast.literal_eval(node.value)
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == "bezos_cc_secret" for t in node.targets)
        )
        print("Segredo:", secret)
        print("Transformação: ROT47")
        return "".join(
            chr(33 + (ord(c) - 33 + 47) % 94) if 33 <= ord(c) <= 126 else c
            for c in secret
        )
    if challenge == "first-find":
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            names = [name for name in archive.namelist() if name.rsplit("/", 1)[-1] == "uber-secret.txt"]
            if len(names) != 1:
                raise ValueError("Era esperado exatamente um arquivo uber-secret.txt.")
            print("Caminho:", names[0])
            return archive.read(names[0]).decode("utf-8").strip()
    if challenge == "information":
        match = re.search(rb"<cc:license\b[^>]*\brdf:resource=['\"]([^'\"]+)['\"]", data)
        if not match:
            raise ValueError("Campo cc:license não encontrado.")
        encoded = match.group(1)
        print("Metadado: cc:license / rdf:resource")
        print("Base64:", encoded.decode("ascii"))
        return base64.b64decode(encoded, validate=True).decode("utf-8")
    if challenge == "mod26":
        text = data.decode("utf-8").strip()
        print("Texto cifrado:", text)
        print("Transformação: ROT13")
        return codecs.decode(text, "rot_13")
    if challenge == "so-meta":
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            raise ValueError("O arquivo não tem a assinatura PNG.")
        offset = 8
        while offset + 12 <= len(data):
            length = struct.unpack(">I", data[offset:offset + 4])[0]
            kind = data[offset + 4:offset + 8]
            end = offset + 8 + length
            if end + 4 > len(data):
                raise ValueError("Chunk PNG incompleto.")
            if kind == b"tEXt":
                key, _, value = data[offset + 8:end].partition(b"\0")
                if key == b"Artist":
                    print("Chunk PNG: tEXt")
                    print("Metadado: Artist")
                    return value.decode("latin-1")
            offset = end + 4
        raise ValueError("Metadado Artist não encontrado.")
    raise ValueError("Desafio desconhecido.")


def solve_cookies(url):
    # Use exclusivamente a URL da instância do laboratório Cookies.
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError("Informe uma URL HTTP ou HTTPS completa.")
    base = f"{parsed.scheme}://{parsed.netloc}"
    body = urllib.parse.urlencode({"name": "snickerdoodle"}).encode()
    request = urllib.request.Request(base + "/search", data=body)
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    with opener.open(request, timeout=15) as response:
        endpoint = response.geturl()
        response.read()
    endpoint_parsed = urllib.parse.urlparse(endpoint)
    if (endpoint_parsed.scheme, endpoint_parsed.netloc) != (parsed.scheme, parsed.netloc):
        raise ValueError("O formulário redirecionou para outro domínio.")
    print("Instância:", base)
    print("Rota após a pesquisa:", endpoint_parsed.path)
    print("Cookie após a pesquisa:", next((f"{c.name}={c.value}" for c in jar if c.name == "name"), "não informado"))
    for value in range(32):
        request = urllib.request.Request(endpoint, headers={"Cookie": f"name={value}"})
        with urllib.request.urlopen(request, timeout=15) as response:
            page = html.unescape(response.read().decode("utf-8"))
        flag = re.search(r"academy\{[^{}\r\n]+\}", page)
        print(f"name={value}: {'flag encontrada' if flag else 'sem flag'}")
        if flag:
            return flag.group(0)
    raise ValueError("Nenhuma flag encontrada nos valores de 0 a 31.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("desafio", choices=[*SOURCES, "cookies"])
    parser.add_argument("--arquivo", help="Usa uma cópia local em vez de baixar o anexo oficial.")
    parser.add_argument("--url", help="URL atual da instância Cookies, exibida após Launch Instance.")
    args = parser.parse_args()
    if args.desafio == "cookies":
        if not args.url or args.arquivo:
            parser.error("Cookies requer --url e não usa --arquivo.")
        flag = solve_cookies(args.url)
    else:
        if args.url:
            parser.error("--url é usado apenas em Cookies.")
        flag = solve_file(args.desafio, read_source(args.desafio, args.arquivo))
    print("Flag:", flag)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, SyntaxError, StopIteration, zipfile.BadZipFile) as error:
        raise SystemExit(f"Erro: {error}")
