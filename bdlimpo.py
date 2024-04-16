import pandas as pd


dados = pd.read_csv(r'C:\Users\A\Documents\GitHub\moddados\dados\microdados_ed_basica_2023.csv', encoding="latin1", sep=';', on_bad_lines='skip')


col = [
    'TP_SITUACAO_FUNCIONAMENTO',
    'TP_DEPENDENCIA',
    'DT_ANO_LETIVO_INICIO',
    'DT_ANO_LETIVO_TERMINO',
    'NO_ENTIDADE',
    'TP_LOCALIZACAO',
    'CO_REGIAO',
    'NO_REGIAO',
    'CO_UF',
    'NO_UF',
    'NO_MICRORREGIAO',
    'IN_SECRETARIA',
    'IN_LABORATORIO_CIENCIAS',
    'IN_SALA_PROFESSOR',
    'IN_BIBLIOTECA',
    'IN_SALA_DIRETORIA',
    'IN_ACESSIBILIDADE_INEXISTENTE',
    'IN_REFEITORIO',
    'IN_ESGOTO_INEXISTENTE',
    'IN_TRATAMENTO_LIXO_INEXISTENTE',
    'IN_ENERGIA_INEXISTENTE',
    'IN_AGUA_INEXISTENTE',
    'IN_BANHEIRO',
    'IN_BANHEIRO_PNE',
    'IN_QUADRA_ESPORTES',
    'IN_PARQUE_INFANTIL',
    'IN_PATIO_COBERTO',
    'IN_PATIO_DESCOBERTO',
    'CO_MUNICIPIO',
    'NO_BAIRRO',
    'NO_MUNICIPIO',
    'CO_CEP',
    'DS_ENDERECO',
    'NU_ENDERECO',
    'CO_ENTIDADE'
]

# Crie um DataFrame com apenas as colunas desejadas
dados_limpos = dados[col]

# Salve o DataFrame em um novo arquivo CSV
dados_limpos.to_csv('colunas_essenciais.csv', index=False)