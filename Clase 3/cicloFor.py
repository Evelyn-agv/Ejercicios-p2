class For:
    def __init__(self):
        pass

    def usoFor(self):
        datos=["Evelyn", 20, True]
        numeros= (2,20,4,7,8,15.2)
        docente= {"nombre": "Daniel", "Edad": 50, "FAC": "Faci"}
        registroN= [(30,45), [15,71], (43,53)]
        registroA= [{"nombre": "Maria", "Nota": 75}, {"nombre": "Carlos", "Nota": 86}, {"nombre": "Michael", "Nota": 96}]
        for i in range(5):  #rango(0,1,2,3,4)
            print("i= {}" .format(i))
        for i in range(2,10):  
            print("i= {}" .format(i))
        for i in range(4,10,2):  
            print("i= {}" .format(i), end= " ")
        for i in range(12,2,-3):
            print("i= {}" .format(i), end= " ")
    
        contar= len(datos)
        # j=0
        # while j < contar:
        #     print("while", datos[j])
        #     j+=1
        for i in range(contar-1,-1,-1):
            print("for", datos[i])
        for dato in numeros:
            print(dato)
        for dato in ['H','O','L', 'A', 'como','estas']:
            print(dato)
        print("\nDiccionario de notas")
        for clave, valor in docente.items():
            print(clave, ":", valor, end= " ")
        
        for alumnos in registroA:
            for clave, valor in alumnos.items():
                print(clave, ":", valor, end= " ")

for1= For()
for1.usoFor()