class For:
    def __init__(self):
        pass

    def usoFor(self):
        registroN= [(30,40), [20,40,20], (50,40,20,10,5)]
        sum=0
        long=0
        for notas in registroN:
            parcial=0
            print(notas, end=" ")
            for x in notas:
                print(x)
                long+=1
                sum+= x
                parcial+= x
            promedioP= parcial/len(notas)
            print("Notas parciales= {} - Promedio Parcial={}" .format(parcial, promedioP))
        r= sum/long
        print("Total notas= {} - #Notas general={} : Promedio general={}" .format(sum, long, r))
        
        print("Segunda parte")

        registroA= [{"nombre": "Maria", "Nota": 70}, {"nombre": "Carlos", "Nota": 60}, {"nombre": "Michael", "Nota": 90}]
        acum=0
        cont= 0
        for alumnos in registroA:
            print(alumnos)
            for clave, valor in alumnos.items():
               print(clave, ":", valor, end= " ")
               if clave=="final": acum+=valor
            cont+=1
        print(acum/cont)
        
        print("Tercera parte")
        
        frase= "Hola como estas"
        vocales=[]
        for car in frase:
            if car in ("a","e","i","o","u"):
                vocales.append(car)
        print(vocales)

        print([car for car in "Hola como estas"  if car in ("a","e","i","o","u") ])
  

for1= For()
for1.usoFor()
