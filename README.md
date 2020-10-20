# extraiDecreto48063
Script para extração de coordenadas a partir do texto do Decreto Estadual (MG), Decreto Nº 48.063, de 15 de Outubro de 2020.
# Procedimentos
- Arquivo de origem PDF obtido do Diário Oficial de MG (16/10/2020) https://www.jornalminasgerais.mg.gov.br/?dataJornal=2020-10-16
- PDF exportado para MS Word (.DOC) para facilitar manipulação
- Do arquivo PDF foi selecionado o texto que contém coordenadas (Anexo) copiado e salvo em arquivo de texto (codificação 'utf-8) 'TextoDecretoCauaia.txt', 'TextoDecretoSerraDaLagoaDourada.txt', 'TextoDecretoSerraDeBaldim.txt'
- Aplicação do script python 'python ExtraiCoordenadas.py'
- O script extrai os vértices e grava em arquivo de saída pronto para importação em ambiente SIG ('verticesTextoDecretoCauaia', 'verticesTextoDecretoSerraDaLagoaDourada.txt', 'verticesTextoDecretoSerraDeBaldim.txt')
- A pasta 'saidas' contem os arquivos resultantes do processamento do script bem como arquivos KMZ após importacao em SIG
