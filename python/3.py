import requests

paths_validos = []
url_base = "https://www.youtube.com"
import ipdb;ipdb.set_trace()
def fetch_data(request_url):
    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            paths_validos.append(request_url)
    except requests.exceptions.RequestException as e:
        # print(f"Erro ao acessar {request_url}: {e}")
        return None

def fetch_paths(request_url_paths):
    try:
        response = requests.get(request_url_paths)
        if response.status_code == 200:
            with open("arquivos_validos.txt", "a") as arquivo:
                arquivo.write(request_url_paths + "\n")
    except requests.exceptions.RequestException as e:
        # print(f"Erro ao acessar {request_url_paths}: {e}")
        return None

with open("paths.txt", "r") as arquivo:
    for i, linha in enumerate(arquivo):
        linha = linha.strip()
        # print(linha)
        full_url = f"{url_base}/{linha}"  
        fetch_data(full_url)

# Lê todos os arquivos de arquivos.txt e verifica se são válidos
with open("arquivos.txt", "r") as arquivo:
    for linha1 in arquivo:
        linha1 = linha1.strip()
        full_url_arquivo = f"{url_base}{linha1}"
        fetch_paths(full_url_arquivo)

print("\nPaths Válidos:")
for path in paths_validos:
    print(path)

print("\nArquivos Válidos:")
with open("arquivos_validos.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        print(linha)


print("Fim do programa ")
