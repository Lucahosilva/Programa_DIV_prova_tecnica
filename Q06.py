from pymongo import MongoClient

url_conexao = 'mongodb+srv://lucashosilva:OsmuSe232j1n38eA@sandbox.nc0gzpu.mongodb.net/'
client = MongoClient(url_conexao)

collection = client.gama.produto


def ajustar_estoque(sku, estoque, collection):
    collection.update_one({"sku": sku}, {"$set": {"estoque": estoque}})


if __name__ == '__main__':
    sku = input('Digite o sku ')
    estoque = int(input('Qual o estoque '))

    ajustar_estoque(sku, estoque, collection)
