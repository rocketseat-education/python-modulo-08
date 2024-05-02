'''
exc_type: O tipo exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_val: O valor da exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_tb: O traceback (rastreamento de pilha) associado à exceção que ocorreu,
se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None
'''


class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self):
        print("Estou saindo")
