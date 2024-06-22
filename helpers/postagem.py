import json
import re
from urllib import request, parse
import os

TINYURL_API = "https://api.tinyurl.com/create?api_token=" + \
    os.getenv("TINYURL_API_KEY")


def encurtar_url(texto: str):
    """Verifica a existência de uma URL grande e substitui ela por uma versão encurtada.

    Args:
        texto (str): O texto a ser verificado.
    """
    url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
    urls = re.findall(url_extract_pattern, texto)
    lista_urls_novas = []

    for url in urls:
        try:
            if url.index('tinyurl.com'):
                continue
        except Exception:
            body = parse.urlencode({"url": url}).encode()
            requisicao = request.Request(TINYURL_API, data=body)
            resposta = request.urlopen(requisicao)
            dados = json.loads(resposta.read())
            url_encurtada = dados['data']['tiny_url']
            lista_urls_novas.append([url, url_encurtada])

    for item in lista_urls_novas:
        texto = texto.replace(item[0], item[1])

    return texto
