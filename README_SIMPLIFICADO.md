
# Projeto: Coleta de Dados de Moedas e Relatório em Excel

Este projeto automatiza a coleta de dados financeiros, como cotações de moedas e taxas de juros, e gera um relatório em Excel com múltiplas abas.

## Funcionalidades

- Coleta de cotações atualizadas (Dólar, Euro, Bitcoin)
- Coleta da taxa SELIC dos últimos 6 meses
- Coleta do histórico dos últimos 30 dias do Dólar
- Geração de um arquivo Excel com:
  - Aba "Resumo Atual"
  - Aba "Taxas de Juros"
  - Aba "Log de Execução"
  - Aba "Histórico - Dólar"
- Geração de log de execução (.log)
- Tratamento de erros e falhas de conexão
- Preenchimento de datas faltantes no histórico com o último valor

## Requisitos

- Python 3.7 ou superior
- Bibliotecas necessárias:

```bash
pip install requests openpyxl python-dateutil
```

## Como Executar

1. Instale as dependências com o comando acima.
2. Execute o arquivo `main.py`:

```bash
python main.py
```

3. O arquivo `relatorio_moedas.xlsx` será gerado na pasta principal do projeto.
4. Um log da execução será salvo na pasta `logs`.

## Configurações

O arquivo `config.py` armazena os parâmetros usados no projeto:

```python
URL_COTACOES = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
URL_SELIC_BASE = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados"
URL_HISTORICO_BASE = "https://economia.awesomeapi.com.br/json/daily"
ARQUIVO_EXCEL = "relatorio_moedas.xlsx"
MESES_SELIC = 6
```

## Observações

- Fins de semana e feriados não possuem cotação. O sistema pode preencher essas datas com o último valor conhecido.
- Logs de execução ajudam a identificar possíveis falhas de conexão ou problemas com as APIs.

## Autor

Vitor Emanuel
