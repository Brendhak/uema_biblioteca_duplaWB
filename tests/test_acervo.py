from biblioteca.livro import Livro
from biblioteca.acervo import Acervo


def test_adicionar_livro_aumenta_total():
    meu_acervo = Acervo("Livros do wes e da brenda")
    total_inicial = meu_acervo.total_livros()
    novo_livro = Livro("Gestao de E-lixo", "C,C.W", "978-85-510-0257-5")
    meu_acervo.adicionar_livro(novo_livro)
    assert meu_acervo.total_livros() == total_inicial + 1


def test_buscar_por_titulo():
    meu_acervo = Acervo("Livros do wes e da brenda")
    livro = Livro("Ingressante em ADS", "C,C.K.B", "978-85-510-0258-2")
    meu_acervo.adicionar_livro(livro)
    resultados = meu_acervo.buscar_por_titulo("Ingressante")
    assert livro in resultados
