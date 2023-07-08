class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

    def exibir_produtos(self):
        for produto in self.produtos:
            print(f"Nome: {produto.nome}, Preço: {produto.preco}")


# Testando a classe CarrinhoDeCompras
carrinho = CarrinhoDeCompras()

produto1 = Produto("Camiseta", 29.90)
produto2 = Produto("Calça", 79.90)

carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)

carrinho.exibir_produtos()

total_compra = carrinho.calcular_total()
print(f"Valor total da compra: R$ {total_compra:.2f}")