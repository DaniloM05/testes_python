import re
import pandas as pd

def valida_CEP(cep: str, cidade: str) -> bool:
    cep_limpo = re.sub(r'\D', '', cep)
    
    if not re.fullmatch(r'^\d{8}$', cep_limpo):
        raise ValueError("Formato do CEP inválido. Deve conter 8 dígitos.")

    if not re.fullmatch(r'^[A-Za-zÀ-ÿ\s\-]{3,100}$', cidade.strip()):
        raise ValueError("Formato da cidade inválido. Deve ter entre 3 e 100 caracteres.")

    data = pd.ExcelFile("./ceps.xlsx")
    df = pd.read_excel(data, 'LOCALIDADES')

    cep_int = int(cep_limpo)
    cidade_lower = cidade.lower().strip()

    for _, row in df.iterrows():
        localidade = str(row['LOCALIDADE_SEM_ACENTOS']).lower().strip()
        cep_inicial = int(re.sub(r'\D', '', str(row['CEP_INICIAL'])))
        cep_final = int(re.sub(r'\D', '', str(row['CEP_FINAL'])))

        if localidade == cidade_lower:
            if cep_inicial <= cep_int <= cep_final:
                return True
            else:
                raise ValueError("CEP informado não pertence à cidade especificada.")

    raise ValueError("Cidade informada não encontrada no banco de dados.")