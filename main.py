import streamlit as st
import pandas as pd

def mostrar_cabecalho(dataset_path, linhas=5):

   
    df = pd.read_csv('dados\microdados_ed_basica_2023.csv', encoding="latin1", sep = ';', on_bad_lines='skip')
    st.write(df.head(linhas))


def main():
    st.title("Visualizador de Dados")
    arquivo_path = "dados\microdados_ed_basica_2023.csv"
    mostrar_cabecalho(arquivo_path)

if __name__ == "__main__":
    main()
