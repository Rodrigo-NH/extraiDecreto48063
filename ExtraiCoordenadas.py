# SPDX-License-Identifier: BSD-2-Clause

def load_txt():
    textoDecreto  = open('DecretoTextoCoordenadas.txt', 'r', encoding='utf-8')
    textoDecreto = textoDecreto.read()
    textoDecreto = textoDecreto.replace(" ", "")
    vertices = open('vertices.txt', 'w')
    vertices.write('vertice,x,y' + '\n')

    srch = 'ovérticev'
    start = fcurr = 0
    while start >= 0:
        pos = textoDecreto.find(srch, start)
        if pos < 0:
            break
        vertice = textoDecreto[pos:pos+54] # Seleciona substring com extensão suficiente que contenha todos dados de interesse + marcadores padrão do texto
        trimverticeIndex = vertice.find(',')
        verticetxt = vertice[0:trimverticeIndex]
        verticetxtLen = len(verticetxt)
        verticeNumber = verticetxt[9:verticetxtLen]
        trimcoordx = vertice.find('sN')
        verticecoords = vertice[trimcoordx+2:len(vertice)]
        verticeYindf = verticecoords.find('me')
        verticeY = verticecoords[0:verticeYindf]
        verticeXp = verticecoords[verticeYindf+3:]
        verticeXindf1 = verticeXp.find('m')
        verticeX = verticeXp[0:verticeXindf1]
        linhaVertice = verticeNumber + ',' + verticeX + ',' + verticeY
        vertices.write(linhaVertice + '\n')
        fcurr += 1
        start = pos + len(srch)

    vertices.close()

if __name__ == '__main__':
    load_txt()