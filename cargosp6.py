class Cargosp6:
    secuencia_cargosp6 = 2
    cargos = [{"codigo":1,"cargo":"Tester"},{"codigo":2,"cargo":"Director"}]
    def __init__(self,cargo_sp6):
        Cargosp6.secuencia_cargosp6 += 1
        self.codigo_sp6 = Cargosp6.secuencia_cargosp6
        self.cargo_sp6 = cargo_sp6

    def registro_cargosp6(self):
        return {"codigo":self.codigo_sp6,"cargo":self.cargo_sp6}

    def mostrar_cargosp6(self):
        print("{} - {}".format(self.codigo_sp6,self.cargo_sp6))

    def datos_cargosp6(self):
        return [self.codigo_sp6,self.cargo_sp6]
