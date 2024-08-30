import requests

paths_validos = []
url_base = input("Digite o Alvo: ")


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
    
def fetch_prefixo(request_url_prefixo):
    
    try:
        response = requests.get(request_url_prefixo)
        if response.status_code == 200:
            with open("arquivos_validos2.txt", "a") as arquivo:
                arquivo.write("\n" + request_url_prefixo )

    except requests.exceptions.RequestException as e:
        return None
    

with open("paths.txt", "r") as arquivo:
    for i, linha in enumerate(arquivo):
        linha = linha.strip()
        # print(linha)
        full_url = f"Http://www.{url_base}/{linha}"  
        fetch_data(full_url)


with open("arquivos.txt", "r") as arquivo:
    for linha1 in arquivo:
        linha1 = linha1.strip()
        full_url_arquivo = f"Http://www.{url_base}{linha1}"
        fetch_paths(full_url_arquivo)

with open("test2.txt", "r") as arquivo:
    for i, linha in enumerate(arquivo):
        linha = linha.strip()
        # print(linha)
        # Formata a URL completa com o prefixo 'https://' e o sufixo base URL
        full_url = f"http://{linha}.{url_base}"  
        data = fetch_prefixo(full_url)
        # if data:
        #     print(data)
        # else:
        #     break

print("-----------------------------------------------------------")
print("\nPaths Válidos:")
for path in paths_validos:
    print(path)

print("-----------------------------------------------------------")
print("\nArquivos Válidos:")
with open("arquivos_validos.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        print(linha)

print("-----------------------------------------------------------")
print("\nPrefixos Válidos:")
with open("arquivos_validos2.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        print(linha)
print("-----------------------------------------------------------")


print("Fim do programa ")
