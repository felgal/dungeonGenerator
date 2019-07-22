import numpy
from PIL import Image
import random

class sala:
    def __init__(self, xInit,yInit,tam):
        self.xI=xInit
        self.yI=yInit
        self.xF=xInit+tam
        self.yF=yInit+tam
        self.cor=[0,0,0]

def intAleatorio(seed,min,max):
    random.seed(seed)
    return random.randint(min,max)

#valores inicais
seed=""
tamDungeon=128
minSalas=16
maxSalas=25
minTamSalas=6
maxTamSalas=15

#inicializa imagem
data = numpy.zeros((tamDungeon, tamDungeon, 3), dtype=numpy.uint8)


#geracao de um seed aleatorio caso seed esteja vazio
if(seed==""):
    seed = random.randint(1000000000,2147000000)
print("Seed atual: "+str(seed))

#geração da dungeon
dungeon = []
for i in range(0,tamDungeon):
    dungeon.append([0]*tamDungeon)
print("Tamanho da dungeon: "+str(len(dungeon))+"x"+str(len(dungeon[0])))

#geração das salas
salas =[]
contadorSala=seed
while len(salas)<minSalas:
    tentativaCriacao=0
    while tentativaCriacao<10 and len(salas)<maxSalas:
        xInicial = intAleatorio(contadorSala,0,tamDungeon)
        contadorSala+=1
        yInicial = intAleatorio(contadorSala,0,tamDungeon)
        contadorSala+=1
        tamAtual = intAleatorio(contadorSala,minTamSalas,maxTamSalas)
        contadorSala+=1
        #salaAtual= sala(xInicial,yInicial,tamAtual)
        colisao=False
        if(yInicial+tamAtual>tamDungeon or xInicial+tamAtual>tamDungeon):
            colisao=True
        for s in salas:
            if (xInicial<=s.xI and xInicial+tamAtual>=s.xF  and ((yInicial>=s.yI and yInicial<=s.yF))) or (xInicial+tamAtual/2>=s.xI and xInicial+tamAtual/2<=s.xF  and ((yInicial>=s.yI and yInicial<=s.yF) or (yInicial+tamAtual>=s.yI and yInicial+tamAtual<=s.yF))) or(xInicial>=s.xI and xInicial<=s.xF  and ((yInicial>=s.yI and yInicial<=s.yF) or (yInicial+tamAtual>=s.yI and yInicial+tamAtual<=s.yF))) or (xInicial+tamAtual>=s.xI and xInicial+tamAtual<=s.xF and ((yInicial>=s.yI and yInicial<=s.yF) or (yInicial+tamAtual>=s.yI and yInicial+tamAtual<=s.yF))) or (xInicial<=s.xI and xInicial+tamAtual>=s.xF and yInicial<=s.yI and yInicial+tamAtual>=s.yF):
                colisao = True
                break
        if(not colisao):
            salas.append(sala(xInicial,yInicial,tamAtual))
        else:
            tentativaCriacao+=1

print("Quantidade de salas: "+ str(len(salas)))
#gera cores para a sala e preenche a dungeon
for s in salas:
    s.cor = [intAleatorio(contadorSala+1,0,255),intAleatorio(contadorSala+2,0,255),intAleatorio(contadorSala+3,0,255)]
    contadorSala+=3
    for x in range(s.xI, s.xF):
        for y in range(s.yI, s.yF):
            dungeon[x][y] = s.cor

#preenche data com base nas salas
for x in range(0,tamDungeon):
    for y in range(0,tamDungeon):
        if(dungeon[x][y]!=0):
            data[x,y]=dungeon[x][y]




#transforma o array em imagem e mostra
image = Image.fromarray(data)
image.show()