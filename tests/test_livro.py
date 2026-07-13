import pytest
from biblioteca.livro import Livro


# ── Testes existentes ─────────────────────────────────────────────────────

def test_criar_livro():
    livro = Livro("Dom Casmurro", "Machado de Assis", "978-85-359-0277-5")
    assert livro.titulo == "Dom Casmurro"
    assert livro.autor == "Machado de Assis"
    assert livro.disponivel is True


def test_emprestar_livro_disponivel():
    livro = Livro("O Cortico", "Azevedo", "978-85-001-0001-1")
    livro.emprestar()
    assert livro.disponivel is False


def test_emprestar_livro_ja_emprestado_levanta_erro():
    livro = Livro("Memorias Postumas", "Machado de Assis", "978-85-001-0002-2")
    livro.emprestar()
    with pytest.raises(ValueError):
        livro.emprestar()


# ── Complete os testes abaixo ─────────────────────────────────────────────

def test_devolver_livro_emprestado():
    livro = Livro("O Cortico", "Azevedo", "978-85-001-0001-1")
    livro.emprestar()
    livro.devolver()
    assert livro.disponivel is True


def test_devolver_livro_ja_disponivel_levanta_erro():
    livro = Livro("O Alquimista", "Paulo Coelho", "978-85-359-0000-0")
    with pytest.raises(ValueError):
        livro.devolver()


def test_representacao_string_livro():
    livro = Livro("Neuromancer", "William Gibson", "978-85-359-1111-1")
    formato_esperado = "'Neuromancer' de William Gibson (ISBN:978-85-359-1111-1) [Disponivel]"
    assert str(livro) == formato_esperado
