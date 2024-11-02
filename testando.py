# %%
def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    media_vendas = avg(vendas)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))

# %%
import re
 
# Initialising string
ini_string1 = '1234556'
ini_string2 = 'ab123bc'
# Regular expression to find if the string is only digits and/or ','
regex = r'^(\d+)(,\s*\d+)*$'
 
# printing initial string
print ("Initial Strings : ", ini_string1, ini_string2)
 
# Using regex()
if re.match(regex, ini_string1):
    print ("String1 contains all numbers")
else:
    print ("String1 doesn't contains all numbers")
     
if re.match(regex, ini_string2):
    print ("String2 contains all numbers")
else:
    print ("String2 doesn't contains all numbers")
    
# %%
def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem:
        if count > max_count:
            max_count = count
            max_produto = produto     
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = entrada.split(', ')
    
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))

# %%
class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())

class Bar(Foo):
    def hello(self):
        return super().hello()

bar = Bar()
bar.hello()

# %%
class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
            # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
            total += venda.quantidade * venda.valor
            
        return total


def main():
    relatorio = Relatorio()
    
    # A entrada consiste em dados de vendas com as seguintes colunas:
    # - Produto (string)
    # - Quantidade (inteiro)
    # - Valor (decimal)
    
    
    for i in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    print(f"Total de vendas: {relatorio.calcular_total_vendas()}")
    


if __name__ == "__main__":
    main()
    
    
# %%
class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    # TODOS: Implementar o método adicionar_venda para adicionar uma venda à lista de vendas:
    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)

    # TODOS: Implementar o método total_vendas para calcular e retornar o total das vendas
    def total_vendas(self):
        total = 0
        for venda in self.vendas:
            # total += venda.quantidade * venda.valor
            total += venda.valor
    

        return total

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # TODOS: Adicione a venda à categoria usando o método adicionar_venda:
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        # TODOS: Exibir o total de vendas usando o método total_vendas:
        print(f"Vendas em {categoria.nome}: {categoria.total_vendas()}")

if __name__ == "__main__":
    main()
    
    
# %%
def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = reversed(lista_visuais.split(", "))
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    conjunto = set([visual.title() for visual in visuais])
    lista_final = list(conjunto)
    
    
    # TODO: Converta o conjunto de volta para uma lista ordenada:
    lista_final.sort()
    
    
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)

# %%
def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    # TODO: Extraia o ano de cada data e cria uma nova lista com os anos
    anos = [data.split("-")[0] for data in lista_datas]
    
    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)


entrada = input()

# TODO: Chame a função para imprimir o resultado:
saida = extrair_anos(entrada)

print(saida)