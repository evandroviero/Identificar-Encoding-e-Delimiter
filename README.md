# Visão Geral

Este script Python contém três funções projetadas para lidar com arquivos CSV: list_csv_files, detect_encoding e detect_encoding. Cada função serve a um propósito específico relacionado à manipulação de arquivos CSV e detecção de codificação.

Funções

## list_csv_files
**Descrição**: Esta função lista todos os arquivos CSV em uma pasta especificada.
**Parâmetros**: `folder_path`: O caminho para a pasta contendo os arquivos CSV.
**Retorno**: Uma lista de caminhos para os arquivos CSV encontrados na pasta especificada.

```python
list_csv_files(folder_path)
```

## detect_encoding
**Descrição**: Esta função detecta a codificação de um arquivo de texto fornecido.
**Parâmetros**: `folder_path`: O caminho para a pasta contendo os arquivos CSV.
**Retorno**: Encoding do arquivo selecionado.

``` python
detect_encoding(caminho_do_arquivo)
```
## detect_delimiter
**Descrição**: Esta função detecta a delimitador de um arquivo de texto fornecido.
**Parâmetros**: `folder_path`: O caminho para a pasta contendo os arquivos CSV.
**Retorno**: Delimitador do arquivo selecionado.

``` python
detect_delimiter(caminho_do_arquivo)
```
