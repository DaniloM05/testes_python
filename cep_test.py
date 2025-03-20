import pytest
from cep import valida_CEP  

def test_validacao_cep_sucesso():
    """Teste com um CEP válido e cidade correspondente."""
    assert valida_CEP("69945000", "Acrelandia")

def test_validacao_cep_formato_invalido():
    """Teste para um CEP em formato inválido."""
    with pytest.raises(ValueError, match="Formato do CEP inválido"):
        valida_CEP("06730-000000", "Sorocaba")

def test_validacao_cidade_formato_invalido():
    """Teste para um nome de cidade em formato inválido (muito curto)."""
    with pytest.raises(ValueError, match="Formato da cidade inválido"):
        valida_CEP("69932000", "A")

def test_validacao_cidade_vazia():
    """Teste para um nome de cidade vazio."""
    with pytest.raises(ValueError, match="Formato da cidade inválido"):
        valida_CEP("0673000000000", "")

def test_validacao_cep_nao_pertence_a_cidade():
    """Teste para um CEP que não pertence à cidade informada."""
    with pytest.raises(ValueError, match="CEP informado não pertence à cidade especificada"):
        valida_CEP("06730000", "Brasileia")

def test_validacao_cidade_nao_existente():
    """Teste para uma cidade que não está na base de dados."""
    with pytest.raises(ValueError, match="Cidade informada não encontrada no banco de dados"):
        valida_CEP("12345678", "CidadeInexistente")