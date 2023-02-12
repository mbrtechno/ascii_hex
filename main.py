arquivo = open("dados.txt", "r")
result = open("resultado.bin", "w")
for linha in arquivo:
    linha = linha.replace("\n", "")
    print(linha)
    result.write(bytes.fromhex(linha).decode("ASCII"))  # testar isso para transformar em xxx.bin
arquivo.close()
result.close()
