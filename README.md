# extraiDecreto48063
Script para extração de coordenadas a partir do texto do Decreto Estadual (MG) 48.063 (10/2020)
# Procedimentos
- Arquivo de origem PDF oficial do Diário Oficial de MG (16/10/2020) https://www.jornalminasgerais.mg.gov.br/?dataJornal=2020-10-16
- PDF exportado para MS Word (.DOC) para facilitar manipulação
- Do arquivo DOC foi selecionado o texto que contém coordenadas (Anexo Cauaia) e salvo em arquivo de texto ('DecretoTextoCoordenadas.txt', 'utf-8')
- Aplicação do script python 'python ExtraiCoordenadas.py'
- O script extrai os vértices e grava em arquivo de saída pronto para importação em ambiente SIG (vertices.txt)