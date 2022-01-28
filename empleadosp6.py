from cargosp6 import Cargosp6
from departamentosp6 import Departamentosp6

class Empleadosp6:
    secuencia_empleadosp6 = 2
    empleadossp6 = [{"codigo":1,"nombre":"Luis","cedula":"0806532142","cargo":1,"departamento":1,"sueldo":400.00}]

    def __init__(self,nombre,cedula,codCargo,codDepartamento,sueldo):
        Empleadosp6.secuencia_empleadosp6 += 1
        self.codigo_empleado = Empleadosp6.secuencia_empleadosp6
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = codCargo
        self.departamento = codDepartamento
        self.sueldo = sueldo

    def mostrar_empleadosp6(self):
            print("{} - {} - {} - {}".format(self.codigo_empleado,self.nombre,self.cedula,self.cargo,self.departamento))

    def registro_empleadosp6(self):
        return{"codigo":self.codigo_empleado,"nombre":self.nombre,"cedula":self.cedula,"cargo":self.cargo,"departamento":self.departamento,"sueldo":self.sueldo}
