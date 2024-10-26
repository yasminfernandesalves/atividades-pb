#!/bin/bash
#
####################################################################
#
#consolidador de processamento de vendas - concatenando os relatórios gerados na execução dos quatro dias
#
#criador: Yasmin Fernandes Alves
#data de criação: 21/10/2024
#
#####################################################################


# criando o relatorio final e adicionando o cabeçalho a ele
{
	echo "Relatório final do processamento de vendas"
	echo "Data:$(date +%Y/%m/%d\ %H:%M )"
	echo ""
} > /home/yaxmin/ecommerce/vendas/backup/relatorio_final.txt


# loop que procura arquivos seguem o padrão relatorio-*.txt e então concatenando os relatórios encontrados no relatório final
for relatorio in /home/yaxmin/ecommerce/vendas/backup/relatorio-*.txt; do
	{
		echo $(basename "$relatorio")
		cat $relatorio
		echo ""
		echo "============================================================="
	} >> /home/yaxmin/ecommerce/vendas/backup/relatorio_final.txt
done


# fim do script :D
