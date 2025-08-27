inventario = {}

def criptografar(texto, chave=3):
    return "".join(chr((ord(char) + chave - 32) % 95 + 32) for char in texto)

def descriptografar(texto, chave=3):
    return "".join(chr((ord(char) - chave - 32) % 95 + 32) for char in texto)


def adicionar_produto():
    while True:
        try:
            id_produto = int(input("ID do produto (apenas números): "))
            if id_produto in inventario:
                print("Erro: Este ID já está cadastrado. Tente novamente.")
                continue
            break  # Sai do loop se o ID for válido
        except ValueError:
            print("Erro: O ID deve ser um número inteiro. Tente novamente.")

    nome = input("Nome: ")
    while True:
        try:
            quantidade = int(input("Quantidade (número inteiro): "))
            preco = float(input("Preço (número decimal): "))
            break  # Sai do loop se as entradas forem válidas
        except ValueError:
            print("Erro: Quantidade e preço devem ser números válidos. Tente novamente.")

    importado = input("Importado (s/n): ").strip().lower() == 's'
    inventario[id_produto] = {
        "nome": nome,
        "quantidade": criptografar(str(quantidade)),
        "preco": criptografar(f"{preco:.2f}"),
        "importado": importado
    }
    print(f"Produto '{nome}' adicionado com sucesso!")

def remover_produto():
    id_produto = int(input("ID do produto para remover: "))
    inventario.pop(id_produto, None)

def listar_produtos():
    if not inventario:
        print("Nenhum produto no inventário.")
        return

    print("\nProdutos cadastrados:")
    for id_produto, detalhes in inventario.items():
        quantidade = int(descriptografar(detalhes["quantidade"]))  # Converte para inteiro
        preco = float(descriptografar(detalhes["preco"]))  # Converte para float
        print(f"ID: {id_produto}, Nome: {detalhes['nome']}, "
              f"Quantidade: {quantidade}, Preço: R${preco:.2f}, Importado: {detalhes['importado']}")

def ordenar_inventario():
    lista = [{"id": k, **v} for k, v in inventario.items()]
    if len(lista) <= 100:
        bubble_sort(lista)  # Usa Bubble Sort para listas pequenas
    else:
        merge_sort(lista)  # Usa Merge Sort para listas grandes
    return lista

def busca_linear(nome):
    for id_produto, detalhes in inventario.items():
        if detalhes["nome"].lower() == nome.lower():
            quantidade = int(descriptografar(detalhes["quantidade"]))
            preco = float(descriptografar(detalhes["preco"]))
            print(f"Produto encontrado: ID {id_produto}, Nome: {detalhes['nome']}, "
                  f"Quantidade: {quantidade}, Preço: R${preco:.2f}, Importado: {detalhes['importado']}")
            return
    print("Produto não encontrado.")


def busca_binaria(lista_ordenada, nome):
    inicio, fim = 0, len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio]["nome"].lower() == nome.lower():
            return lista_ordenada[meio]
        elif lista_ordenada[meio]["nome"].lower() < nome.lower():
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

def bubble_sort(L):
    n = len(L)
    while n > 1:
        empurra(L, n)
        n -= 1

def empurra(L, n):
    i = 0
    while i < n-1:
        if L[i] > L[i+1]:
            troca(L, i, i+1)
        i += 1

def troca(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i]["nome"] < direita[j]["nome"]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1


def menu_busca():
    print("\nBusca por produto:")
    print("1. Busca Linear")
    print("2. Busca Binária")
    opcao = input("Escolha o método de busca: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        busca_linear(nome)
    elif opcao == "2":
        nome = input("Digite o nome do produto: ")
        lista_ordenada = ordenar_inventario()
        resultado = busca_binaria(lista_ordenada, nome)
        if resultado:
            quantidade = int(descriptografar(resultado["quantidade"]))
            preco = float(descriptografar(resultado["preco"]))
            print(f"Produto encontrado: ID {resultado['id']}, Nome: {resultado['nome']}, "
                  f"Quantidade: {quantidade}, Preço: R${preco:.2f}, Importado: {resultado['importado']}")
        else:
            print("Produto não encontrado.")
    else:
        print("Opção inválida.")

def main():
    while True:
        try:
            print("\nMenu:")
            print("1. Adicionar Produto")
            print("2. Remover Produto")
            print("3. Buscar Produto")
            print("4. Listar Produtos")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                adicionar_produto()
            elif opcao == "2":
                remover_produto()
            elif opcao == "3":
                
                menu_busca()
            elif opcao == "4":
                listar_produtos()
            elif opcao == "5":
                print("Encerrando o sistema.")
                break
            else:
                print("Erro: Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Retornando ao menu principal.")

main()
    
