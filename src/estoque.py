from produto import Produto


class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, preco, quantidade):
        self.produtos[nome] = Produto(nome, preco, quantidade)

    def salvar_arquivo(self):
        with open('Estoque.txt', 'w') as arq:
            for produto in self.produtos.values():
                arq.write(f'{produto.nome},{produto.preco},{produto.quantidade}\n')

    def ler_arquivo(self):
        with open("Estoque.txt", "r") as arq:
            for linha in arq:
                nome, preco, quantidade = linha.strip().split(',')
                self.adicionar_produto(nome, float(preco), int(quantidade))

    def imprimir_estoque(self):
        for produto in self.produtos.values():
            print(f'nome: {produto.nome}, preco: {produto.preco}, quantidade: {produto.quantidade}')
