#libreria para introducir la fecha actual
from datetime import datetime
from os import system
import msvcrt



#variable que nos ayuda a simplificar la funcion
now = datetime.now()

#variable del año actual
año_act = now.year

#proceso para limpiar terminal
def clear():
    system("cls")
#llama el proceso clear
clear()

        
def codigo():
############################################# INICIO ###########################
#proceso de inicio del programa
    def inicio():
#defino variables para que se puedan usar fuera del ciclo con el mismo valor
        global edad
        global año_usu
#imprime en pantalla para sacar la informacion
        print("Año de nacimiento")

#lee y guarda el año inscrito en la variable

        año_usu = int(input())

#operacion para calcular la edad
        edad = (año_act - año_usu)
#llama proceso inicio
    inicio()





############################################# CATEGORIAS ########################
    def categorias():
#variable que almacena la categoria
        global categoria
        categoria= str()
    
#categoría infantil
        if edad < 15 and edad > 0:
            categoria= ("categoría infantil")
       
#categoría Junior
        elif edad >= 15 and edad <= 18:
            categoria=("categoría Junior")
       
#categoría Amateur
        elif edad > 18 and edad <= 120:
            categoria=("categoría Amateur")
        else: 
            while edad >= 120 or edad <=0:
                clear()
                print("Error: ingresar el año correcto")
                inicio()
                categorias()

############################################# RESULTADO ###########################
#proceso para mostrar los resultados y mensaje final
    def resultado():
        clear()
#escribe todos los resultados
        print("Año de nacimiento: ", año_usu)
        print("Tu edad es: ",edad," años")
        print("categoria: ", categoria)

    categorias()
#llama al proceso resultado
    resultado()
codigo()
print("")
print("Desea continuar?")
print("1.Si")
print("2.No")
global restar
restar=int(input())

while restar ==1:
    clear()
    codigo()
    print("")
    print("Desea continuar?")
    print("1.Si")
    print("2.No")
    restar=int(input())
print("")
print("Gracias")

loquitas



