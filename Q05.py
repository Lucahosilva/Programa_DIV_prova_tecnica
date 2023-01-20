
from pymongo import MongoClient


def get_collection_mongodb(url_conexao, colecao):
    db = MongoClient(url_conexao)
    col = db[colecao]
    return col



if __name__ == '__main__':

    url_conexao = 'mongodb+srv://lucashosilva:OsmuSe232j1n38eA@sandbox.nc0gzpu.mongodb.net/gama?retryWrites=true&w=majority'
    colecao = 'produto'

    x = get_collection_mongodb(url_conexao, colecao)
    print(x)

