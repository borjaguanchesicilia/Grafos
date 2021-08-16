class Cola:
    
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
        valor = self.vect[0]
        self.vect.pop(0)
        return valor
    
    def mostrar(self):
        print ("\nLa cola es:\n")
        for i in reversed(self.vect):
            print(i, end=" ")

        print ("\n")