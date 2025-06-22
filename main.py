from services.api_client import coletar_dados_moedas, coletar_taxa_selic, coletar_historico_moeda
from utils.excel_writer import criar_relatorio_excel
from utils.logger import configurar_logger
from datetime import datetime

def main():
    logger = configurar_logger()

    try:
        logger.info("Coletando dados das moedas")
        moedas = coletar_dados_moedas()

        logger.info("Coletando taxa SELIC dos últimos 6 meses")
        selic = coletar_taxa_selic()

        logger.info("Coletando histórico do Dólar (30 dias)")
        historico_dolar = coletar_historico_moeda("USD", 30)

        logger.info("Gerando planilha Excel")
        data_execucao = datetime.now()
        criar_relatorio_excel(moedas, selic, data_execucao, historico_dolar)

        logger.info("Relatório gerado com sucesso")

    except Exception as e:
        logger.error("Erro durante execução", exc_info=True)

if __name__ == "__main__":
    main()