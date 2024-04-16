import streamlit as st
import pandas as pd
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
def quantidade_nulos_colunas(df):
    #df = pd.read_csv(data)
    null_counts = df.isnull().sum()
    return null_counts
def valores_unicos_colunas(data):
    df = pd.read_csv(data)
    unique_values = {}
    for column in df.columns:
        unique_values[column] = df[column].unique()
    return unique_values
def mostrar_cabecalho(dataset_path, linhas=5):

   
    df = pd.read_csv(dataset_path, encoding="latin1", sep = ';', on_bad_lines='skip')
    st.write(df.head(linhas))


def main():
    st.title("Visualizador de Dados")
    arquivo_path = "colunas_essenciais.csv"
    mostrar_cabecalho(arquivo_path)

if __name__ == "__main__":
    main()
