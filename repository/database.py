from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()


class Database:
    def __init__(self):
        self.database_key = os.getenv("EQUIP_SUPABASE_KEY", "")
        self.database_url = os.getenv("EQUIP_SUPABASE_URL", "")
        if not self.database_url or not self.database_key:
            raise ValueError(
                "As variáveis EQUIP_SUPABASE_URL e EQUIP_SUPABASE_KEY precisam estar configuradas no .env"
            )
        self.supabase = create_client(self.database_url, self.database_key)

    def obter_conexao(self):
        return self.supabase
