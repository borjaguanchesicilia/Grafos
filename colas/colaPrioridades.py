from math import inf


class ColaPrioridades:
    
    def __init__(self):
        self.vect = []
        self.primero = 0
        self.ultimo = -1

    def vacia(self):
        if self.ultimo < self.primero:
           return True
        else:
            return False

    def tamCola(self):
        print ("\nEl tamaño de la cola es: " + str((self.ultimo - self.primero) + 1))

    def push(self, dato):    
        self.ultimo  += 1
        self.vect.append(dato)

    def pop(self):
        assert (self.ultimo > self.primero) or (self.ultimo == self.primero), 'La cola está vacía'
        self.ultimo  -= 1
        menor = self.vect[0][1][0]
        j = 0
        if (len(self.vect) != 1):
            for i in range(len(self.vect)):
                if(self.vect[i][1][0] < menor):
                    menor = self.vect[i][1][0]
                    j = i

        menor = self.vect[j][0]
        self.vect.pop(j)
        return menor
    
    def mostrar(self):
        print ("\nLa cola es:\n")
        for i in reversed(self.vect):
            print([i[0]+1, i[1]], end=" ")

        print ("\n")