from menusp6 import Menusp6
from cargosp6 import Cargosp6
from departamentosp6 import Departamentosp6
from empleadosp6 import Empleadosp6
import os

def buscacargo(codC):
    cargsp6 = 0
    for bcar in range(0,len(Cargosp6.cargos)):
        car = Cargosp6.cargos[bcar]
        if car["codigo"] == codC:
            cargsp6 = car["cargo"]
            break
    return cargsp6

def buscadepartamento(codD):
    depasp6 = 0
    for bdepa in range(0,len(Departamentosp6.departamentos)):
        depar = Departamentosp6.departamentos[bdepa]
        if depar["codigo"] == codD:
            depasp6 = depar["departamento"]
            break
    return depasp6

def sueldod(sueldo):
    try:
        float(sueldo)
        return True
    except ValueError:
        return False

menu_sp6 = Menusp6()
list = ["1. Cargo","2. Departamento","3. Empleados","4. Salir"]
opcion = ""
while True:
    os.system("cls")
    opcion = menu_sp6.menu(list,"*** Menú Ficha Personal ***")
    if opcion == "1":
        op1 = ""
        while True:
            os.system("cls")
            op1 = Menusp6.menu("",["1). Ingreso","2). Consulta","3). Salir"],"Mantenimiento de cargos")
            os.system("cls")
            if op1 == "1":
                print(" *** Ingreso de Cargos *** ")
                cargo = input("Cargo a Ingresar: ").strip().capitalize()
                while len(cargo) > 20 or len(cargo) == 0:
                    print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                    cargo = input("Esriba el nombre del cargo: ").strip().capitalize()
                cargo1 = Cargosp6(cargo)
                cargo2 = cargo1.registro_cargosp6()
                Cargosp6.cargos.append(cargo2)
                input("Su ingreso se ha realizaco con éxito // Presione una tecla cualquiera para volver al Menú")
            elif op1 == "2":
                print(" *** Lista de cargos *** ")
                print("Código"," "*7,"Descripción")
                for cargo1 in Cargosp6.cargos:
                    codCar = cargo1["codigo"]
                    desCar = cargo1["cargo"]
                    print(" "*1,codCar," "*(12-len(str(codCar))),desCar)
                input("Presione una tecla cualquiera para volver al Menú")
            elif op1 == "3":
                break
    elif opcion == "2":
        op1 = ""
        while op1 != "3":
            os.system("cls")
            op1 = Menusp6.menu("",["1. Ingreso","2. Consulta","3. Salir"],"Mantenimiento De Departamentos")
            os.system("cls")
            if op1 == "1":
                print(" *** Ingreso de Departamentos *** ")
                departamento = input("Escriba el nombre del departamento: ").strip().capitalize()
                while len(departamento) > 20 or len(departamento) < 5:
                    print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                    departamento = input("Escriba el nombre del departamento: ").strip().capitalize()
                depa = Departamentosp6(departamento)
                depar = depa.registro_depsp6()
                Departamentosp6.departamentos.append(depar)
                input("Su ingreso se ha realizaco con éxito // Presione una tecla cualquiera para volver al Menú")
            elif op1 == "2":
                print(" *** Lista de departamentos ***")
                print("Código"," "*7,"Descripción")
                for depa in Departamentosp6.departamentos:
                    codDep = depa["codigo"]
                    desDep = depa["departamento"]
                    print(" "*1,codDep," "*(12-len(str(codDep))),desDep)
                input("Presione una tecla cualquiera para volver al Menú")
    elif opcion == "3":
        op1 = ""
        while op1 != "3":
            os.system("cls")
            op1 = Menusp6.menu("",["1. Ingreso","2. Consulta","3. Salir"],"Mantenimiento De Empleados")
            os.system("cls")
            if op1 == "1":
                print(" *** Ingreso de Empleados *** ")
                nombre = input("Nombre: ").strip().capitalize()
                while len(nombre) < 3 or len(nombre) > 20:
                    print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                    nombre = input("Nombre: ").strip().capitalize()
                cedula = input("Cédula: ")
                while cedula.isdigit() == False:
                    print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                    cedula = input("Cédula: ")
                if cedula.isdigit() == True:
                    while len(cedula) < 10 or len(cedula) > 10:
                        print("Error: No ha ingresado la cantidad de caracteres requeridos o ha excedido el valor")
                        cedula = input("Cédula: ")
                cargo2 = int(input("Ingrese el código del Cargo: "))
                cargo3 = buscacargo(cargo2)
                while cargo3 == 0:
                    print("Error: Código no existe. Ingrese uno válido")
                    cargo2 = int(input("Ingrese el código del Cargo: "))
                    cargo3 = buscacargo(cargo2)
                departamento2 = int(input("Ingrese el código del Departamento: "))
                departamento3 = buscacargo(departamento2)
                while departamento3 == 0:
                    print("Error: Código no existe. Ingrese uno válido")
                    departamento2 = int(input("Ingrese el código del Departamento: "))
                    departamento3 = buscacargo(departamento2)
                sueldo1 = input("Sueldo: $")
                while sueldod(sueldo1) is False:
                    print("Error: No es correcto el tipo de dato que ingreso en el sueldo")
                    sueldo1 = input("Sueldo: $")
                sueldo1 = round(float(sueldo1),2)
                empleado1 = Empleadosp6(nombre,cedula,cargo2,departamento2,sueldo1)
                empleado2 = empleado1.registro_empleadosp6()
                Empleadosp6.empleadossp6.append(empleado2)
                input("Su ingreso se ha realizaco con éxito // Presione una tecla cualquiera para volver al Menú")
            elif op1 == "2":
                print(" *** Lista de Empleados *** ")
                print("Código"," "*7,"Nombre"," "*18,"Cédula"," "*13,"Cargo"," "*11,"Departamento", " "*5,"Sueldo")
                for empleado1 in Empleadosp6.empleadossp6:
                    codEmp = empleado1["codigo"]
                    nomb = empleado1["nombre"]
                    cedu = empleado1["cedula"]
                    cargo4 = empleado1["cargo"]
                    cargdes = buscacargo(cargo4)
                    depar1 = empleado1["departamento"]
                    depardes = buscadepartamento(depar1)
                    sueldo2 = empleado1["sueldo"]
                    print(" "*2,codEmp," "*8,nomb," "*(23-len(nomb)),cedu," "*(22-len(str(cedu))),cargdes," "*(16-len(str(cargdes))),depardes," "*(16-len(str(depardes))),sueldo2)
                input("Presione una tecla cualquiera para volver al Menú")
    elif opcion == "4":
        print("\nGRACIAS POR USAR EL SISTEMA")

        break            
    


