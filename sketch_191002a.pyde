import random

barva_r = 0
barva_g = 0
barva_b = 0

def setup():
    size(1191, 842)
    stroke(barva_r, barva_g, barva_b)
    frameRate(1)
    background(255)
      
def draw():
    zacetniX = 0

    #while  zacetniX < 2000:
        #randomStrokeWeight = random.randint(1, 4)
       # strokeWeight(2)
        #randint = random.randint(2, 29 + zacetniX)
     #  line(randint, 0, randint, 842)
    #    zacetniX += 30
    stevec = 39
    g = 30
    d = 30
    stevec1 = 0
    
    line_x1 = 0

    while stevec > 0:
        rectRandom = random.randint(600, 900)
        fill(barva_r, barva_g, barva_b)
        stroke(barva_r, barva_g, barva_b + 30)
        rect(g, rectRandom, d, 842)
        g += 30
        stevec -= 1
    fill(255)
    rect(0,0, 40, 842)
    #rect(1191, 0, 1191, 842)
    
    while stevec1 < 50:
        line(line_x1, 0, line_x1, 842)
        line_x1 += 30
        stevec1 += 1

    

     
def mousePressed():
    saveFrame("output.png")
