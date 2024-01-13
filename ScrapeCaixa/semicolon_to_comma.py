import pandas as pd
import os
import glob

def converter_csv_pasta(input_folder_path, output_folder_path, input_sep=';', output_sep=',', encoding='ISO-8859-1'):
    """
    Converte todos os arquivos CSV em uma pasta de um separador para outro.

    :param input_folder_path: Caminho da pasta contendo os arquivos CSV de entrada.
    :param output_folder_path: Caminho da pasta para salvar os arquivos CSV convertidos.
    :param input_sep: Separador dos arquivos de entrada. Padrão é ponto e vírgula (;).
    :param output_sep: Separador dos arquivos de saída. Padrão é vírgula (,).
    :param encoding: Codificação dos arquivos de entrada. Padrão é ISO-8859-1.
    """
    # Verifica se a pasta de saída existe, se não, cria
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # Busca por todos os arquivos CSV na pasta de entrada
    for file_path in glob.glob(os.path.join(input_folder_path, '*.csv')):
        file_name = os.path.basename(file_path)  # Definindo file_name aqui para evitar UnboundLocalError
        try:
            # Lendo o arquivo CSV com o separador de entrada e codificação especificada
            df = pd.read_csv(file_path, sep=input_sep, encoding=encoding, on_bad_lines='skip')

            # Construindo o caminho do arquivo de saída
            output_file_path = os.path.join(output_folder_path, file_name)

            # Salvando o DataFrame com o novo separador
            df.to_csv(output_file_path, sep=output_sep, index=False, encoding='ISO-8859-1')

            print(f"Arquivo '{file_name}' convertido com sucesso e salvo em: '{output_file_path}'")
        except Exception as e:
            print(f"Erro ao converter o arquivo '{file_name}': {e}")

# Exemplo de uso do script
input_folder_path = 'downloads'
output_folder_path = 'downloads1'

converter_csv_pasta(input_folder_path, output_folder_path)
