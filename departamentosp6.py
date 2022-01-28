class Departamentosp6:
    secuencia_deparsp6 = 2
    departamentos = [{"codigo":1,"departamento":"Reporte Técnico"},{"codigo":2,"departamento":"Talento Humano"}]
    def __init__(self,deparsp6):
        Departamentosp6.secuencia_deparsp6 += 1
        self.codigo_deparsp6 = Departamentosp6.secuencia_deparsp6
        self.deparsp6 = deparsp6

    def registro_depsp6(self):
        return {"codigo":self.codigo_deparsp6,"departamento":self.deparsp6}

    def mostrar_depsp6(self):
        print("{} - {}".format(self.codigo_deparsp6,self.deparsp6))

    def datos_depsp6(self):
        return [self.codigo_deparsp6,self.deparsp6]