import pytest
import os
from unittest import mock
from repository.database import Database

@mock.patch.dict(os.environ, {"EQUIP_SUPABASE_URL": "", "EQUIP_SUPABASE_KEY": ""})
def test_database_missing_env_vars():
    with pytest.raises(ValueError) as exc:
        Database()
    assert "As variáveis EQUIP_SUPABASE_URL e EQUIP_SUPABASE_KEY precisam estar configuradas" in str(exc.value)
