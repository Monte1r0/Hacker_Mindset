with open ("test.txt", "r") as arquivo:
    # import ipdb;ipdb.set_trace()
    for i, linha in enumerate(arquivo):
        if i < 10:
            print(f'senha: {linha.strip()}')
        else:
            break
    