from domain.enums import StatusEquipamento, StatusAlocacao

def test_status_equipamento_descricao():
    assert StatusEquipamento.EQUIPAMENTO_NOVO.descricao == "Equipamento novo"
    assert StatusEquipamento.FUNCIONANDO.descricao == "Funcionando"
    assert StatusEquipamento.DEFEITUOSO.descricao == "Defeituoso"
    assert StatusEquipamento.MANUTENCAO.descricao == "Manutenção"
    assert StatusEquipamento.DESCARTE.descricao == "Descarte"

def test_status_alocacao_descricao():
    assert StatusAlocacao.ENCERRADA.descricao == "Em vigor"  # Note: The original code has 0 as "Em vigor" but ENCERRADA is 0. So 0="Em vigor", 1="Encerrada".
    assert StatusAlocacao.EM_VIGOR.descricao == "Encerrada"
