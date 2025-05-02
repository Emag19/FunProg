#FunProg
class cubo:
    def __init__(self, aresta):
        self.getRadius = aresta
    
    def getRadios(self):
        return self.getRadius
        
    def faceArea(self):
        return self.getRadius * self.getRadius
    
    def surfaceArea(self):
        return ((self.getRadius * self.getRadius) * 6)
    
    def volume (self):
        return (self.getRadius * self.getRadius * self.getRadius)

print("Digite o Valor da aresta do cubo")
n = float(input())

a = cubo(n)
print(f"Aresta = {a.getRadios()}, Área da Face = {a.faceArea()} , Área da Superfície = {a.surfaceArea()}, Volume = {a.volume()}")