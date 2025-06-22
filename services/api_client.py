import requests
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from config import URL_COTACOES, URL_SELIC_BASE, URL_HISTORICO_BASE

def coletar_dados_moedas():
    url = URL_COTACOES
    
    # Requisição HTTP
    resposta = requests.get(url, timeout=5)
    
    # Verifica se deu tudo certo (erro se código 4xx ou 5xx)
    resposta.raise_for_status()
    
    # Converte para dicionário Python
    dados = resposta.json()
    moedas_legiveis = {
        "USDBRL": "Dólar[USD]",
        "EURBRL": "Euro[EUR]",
        "BTCBRL": "Bitcoin[BTC]"
    }

    cotacoes = {}

    for codigo_api, dados_moeda in dados.items():
        nome_legivel = moedas_legiveis.get(codigo_api, codigo_api)
        valor = float(dados_moeda["bid"])
        cotacoes[nome_legivel] = valor

    return cotacoes

def coletar_taxa_selic():
    hoje = datetime.today()
    inicio = (hoje - relativedelta(months=6)).replace(day=1)
    fim = hoje

    data_inicial = inicio.strftime("%d/%m/%Y")
    data_final = fim.strftime("%d/%m/%Y")

    url = f"{URL_SELIC_BASE}?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
    resposta = requests.get(url, timeout=5)

    try:
        dados = resposta.json()
    except:
        dados = json.loads(resposta.text)

    selic_mensal = {}

    for item in dados:
        data_str = item.get("data")
        valor_str = item.get("valor")

        if data_str and valor_str:
            data_obj = datetime.strptime(data_str, "%d/%m/%Y")
            chave_mes = data_obj.strftime("%m/%Y")  # exemplo: "05/2025"

            # Último valor do mês vai sobrescrever os anteriores
            valor = float(valor_str.replace(",", "."))
            selic_mensal[chave_mes] = valor

    return selic_mensal

def coletar_historico_moeda(moeda="USD", dias=30):
    url = f"{URL_HISTORICO_BASE}/{moeda}-BRL/{dias}"
    resposta = requests.get(url, timeout=5)

    try:
        dados = resposta.json()
    except:
        dados = json.loads(resposta.text)

    historico = {}

    for item in dados:
        data_str = item.get("create_date")
        if data_str:
            # Pega só a data no formato YYYY-MM-DD
            data_formatada = data_str.split(" ")[0]
        else:
            # Usa o timestamp unix
            ts = item.get("timestamp")
            if ts:
                data_formatada = datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%d")
            else:
                continue  # pula se não tiver data

        valor = float(item.get("bid", 0))
        historico[data_formatada] = valor

    # Ordenar por data (mais antigo primeiro)
    historico_ordenado = dict(sorted(historico.items()))

    return historico_ordenado