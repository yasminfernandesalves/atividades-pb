#!/bin/bash
#
###########################################################################################
# Processamento_de_vendas.sh
#
# Autor: Yasmin Fernandes Alves
# Data de criação:20/10/2024
#
# ########################################################################################

# definindo PATH 
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"



# data atual
DATA=$(date +%Y%m%d)


mkdir -p vendas
cp /home/yaxmin/ecommerce/dados_de_vendas.csv /home/yaxmin/ecommerce/vendas/


# criando o subdiretório backup
mkdir -p vendas/backup


#renomeando o arquivo de vendas do diretório de vendas
mv vendas/dados_de_vendas.csv vendas/dados-${DATA}.csv


# copiando o arquivo renomeado para o diretório backup
cp vendas/dados-${DATA}.csv vendas/backup/backup-dados-${DATA}.csv


# criando o arquivo relatorio.txt dentro do diretório backup e adicionando informações a ele
{
	echo "Data e hora do SO: $(date +%Y/%m/%d\ %H:%M)"
	echo "Data do primeiro registro de venda: $(tail -n +2 vendas/dados-${DATA}.csv |head -n 1 | cut -d ',' -f5 )"
	echo "Data do último registro de venda: $(tail -n +2 vendas/dados-${DATA}.csv | cut -d ',' -f5 | sort -t '/' -k3,3 -k2,2 -k1,1 | awk 'END {print}')"
	echo "Quantidade de itens diferentes:" $(tail -n +2 vendas/dados-${DATA}.csv | cut -d ',' -f1 | sort | uniq | wc -l)
	echo ""
        echo "10 primeiras linhas do documento:"
        head -n 11 vendas/dados-${DATA}.csv
} > vendas/backup/relatorio-${DATA}.txt


# compactando o arquivo modificado localizado em backup
zip /home/yaxmin/ecommerce/vendas/backup/backup-dados-${DATA}.zip vendas/backup/backup-dados-${DATA}.csv

# removendo arquivos 
rm -r vendas/backup/backup-dados-${DATA}.csv
rm -r vendas/dados-${DATA}.csv

# fim do Script :)


