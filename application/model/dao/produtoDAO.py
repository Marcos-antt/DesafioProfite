from application.model.entity.produto import Produto
import json 

class ProdutoDAO():
    
    def dict_to_list(self, lista_prod):
        lista = []
        for produto_item in lista_prod:
            produto = Produto()
            produto.set_id(produto_item["id"])
            produto.set_name(produto_item["name"])
            produto.set_imagens(produto_item["image"])
            produto.set_preco_antigo(produto_item["oldPrice"])
            produto.set_preco(produto_item["price"])
            produto.set_descricao(produto_item["description"])           
            prestacao=produto_item["installments"]
            produto.set_prestacao(prestacao["count"])
            produto.set_valorPrestacao(prestacao["value"])
            lista.append(produto)
        return lista

    def produto_list(self):
        list = []
        with open("products.json", "r") as file:
            produto_list = json.load(file)
            list = self.dict_to_list(produto_list)
        return list 
