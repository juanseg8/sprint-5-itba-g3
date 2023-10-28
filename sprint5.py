import json
import re

class Transacciones:
    def __init__(self, estado, tipo, cuentaNumero, permitidoActualParaTransaccion, monto, fecha, numero):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.permitidoActualParaTransaccion = permitidoActualParaTransaccion
        self.monto = monto
        self.fecha = fecha
        self.numero = numero

    def __str__(self):
        return f"{self.estado} {self.tipo} {self.cuentaNumero} {self.permitidoActualParaTransaccion} {self.monto} {self.fecha} {self.numero}"

def ingresar_tipo_transaccion():
        print("1-RETIRO_EFECTIVO_CAJERO_AUTOMATICO")
        print("2-RETIRO_EFECTIVO_POR_CAJA")
        print("3-COMPRA_EN_CUOTAS_TARJETA_CREDITO_")
        print("4-COMPRA_TARJETA_CREDITO_")
        print("5-ALTA_TARJETA_CREDITO_")
        print("6-ALTA_TARJETA_DEBITO")
        print("7-ALTA_CHEQUERA")
        print("8-ALTA_CUENTA_CTE_")
        print("9-ALTA_CAJA_DE_AHORRO_")
        print("10-ALTA_CUENTA_DE_INVERSION")
        print("11-COMPRA_DOLAR")
        print("12-VENTA_DOLAR")
        print("13-TRANSFERENCIA_ENVIADA_")
        print("14-TRANSFERENCIA_RECIBIDA_")
        numero = int(input("Ingrese el numero correspondiente al tipo de transaccion (1-14): "))
        if numero == 1:
                return "RETIRO_EFECTIVO_CAJERO_AUTOMATICO"
        elif numero == 2:
                return "RETIRO_EFECTIVO_POR_CAJA"
        elif numero == 3:
                return "COMPRA_EN_CUOTAS_TARJETA_CREDITO_"
        elif numero == 4:
                return "COMPRA_TARJETA_CREDITO_"
        elif numero == 5:
                return "ALTA_TARJETA_CREDITO_"
        elif numero == 6:
                return "ALTA_TARJETA_DEBITO"
        elif numero == 7:
                return "ALTA_CHEQUERA"
        elif numero == 8:
                return "ALTA_CUENTA_CTE_"
        elif numero == 9:
                return "ALTA_CAJA_DE_AHORRO_"
        elif numero == 10:
                return "ALTA_CUENTA_DE_INVERSION"
        elif numero == 11:
                return "COMPRA_DOLAR"
        elif numero == 12:
                return "VENTA_DOLAR"
        elif numero == 13:
                return "TRANSFERENCIA_ENVIADA_"
        elif numero == 14:
                return "TRANSFERENCIA_RECIBIDA_"
        else:
                return "Tipo invalido"

class Cliente:
    def __init__(self,tipo):
        self.numero = int(input("Ingrese el numero del cliente: "))
        self.validar_nombre()
        self.validar_apellido()
        self.validar_dni()
        self.tipo = tipo
        self.transacciones = []

    def validar_nombre(self):
        while True:
            nombre = input("Ingrese el nombre del cliente: ")
            if nombre.isalpha():
                self.nombre = nombre
                break
            else:
                print("El nombre debe contener solo letras. Intentelo de nuevo.")

    def validar_apellido(self):
        while True:
            apellido = input("Ingrese el apellido del cliente: ")
            if apellido.isalpha():
                self.apellido = apellido
                break
            else:
                print("El apellido debe contener solo letras. Intentelo de nuevo.")    

    def validar_dni(self):
        while True:
            dni = input("Ingrese el DNI del cliente: ")
            if dni.isdigit() and len(dni) == 8:
                self.dni = dni
                break
            else:
                print("El DNI debe contener 8 digitos numericos. Intentelo de nuevo.")

    def info(self):
        cliente_dict = {
            "numero": self.numero,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "tipo": self.tipo,
            "transacciones": [trans.__dict__ for trans in self.transacciones]
            }
        
        cliente_json = json.dumps(cliente_dict, indent=4)
        print(cliente_json)

    def validar_estado_transaccion(self, estado):
        while estado not in ["ACEPTADA", "RECHAZADA", "aceptada", "rechazada"]:
            print("El estado de la transaccion debe ser 'ACEPTADA' o 'RECHAZADA.")
            estado = input("Ingrese el estado de la transaccion: (ACEPTADA-RECHAZADA) ")
        return estado

    def ingresar_transacciones(self):
        print("TRANSACCIONES: ")
        numero = int(input("Ingrese el numero de transacciones: "))
        for i in range(numero):
            estado = input("Ingrese el estado de la transaccion (ACEPTADA-RECHAZADA): ")
            estado = self.validar_estado_transaccion(estado)
            tipo = ingresar_tipo_transaccion()
            cuentaNumero = int(input("Ingrese el numero de cuenta: "))
            permitidoActualParaTransaccion = int(input("Ingrese el permitido actual para la transaccion: "))
            monto = int(input("Ingrese el monto de la transaccion: "))
            fecha = self.validar_formato_fecha()            
            numero = int(input("Ingrese el numero de la transaccion: "))
            transaccion = Transacciones(estado, tipo, cuentaNumero, permitidoActualParaTransaccion, monto, fecha, numero)
            self.transacciones.append(transaccion)

    def validar_formato_fecha(self):
        fecha = input("Ingrese la fecha de la transacción (dd/mm/yyyy): ")
        while not re.match(r'\d{2}/\d{2}/\d{4}', fecha):
            print("Formato de fecha incorrecto. Debe ser dd/mm/yyyy.")
            fecha = input("Ingrese la fecha de la transacción (dd/mm/yyyy): ")
        return fecha

    def __str__(self):
        return f"{self.numero} {self.nombre} {self.apellido} {self.dni} {self.tipo} {self.transacciones}"

    def calcular_monto_total(self):
        monto = int(input("Ingrese el monto de dolares que desea comprar: "))
        precio_dolar = 365.50
        impuesto_pais = 0.35  
        ganancias = 0.45
        monto_total = (precio_dolar + (precio_dolar * impuesto_pais) + (precio_dolar * ganancias)) * monto
        print(f'{monto_total}') 

    def descontar_comision(self):
        monto = int(input("Ingresar el monto a descontar: "))
        comision_porcentaje = 0.5
        comision = (monto * comision_porcentaje) / 100
        monto_descontado = monto - comision
        print(f'{monto_descontado}')

    def calcular_monto_plazo_fijo(self):
        monto = int(input("Ingrese el monto que desea poner en plazo fijo: "))
        interes = 1.20
        monto_con_interes = monto + (monto * interes)
        print(f'{monto_con_interes}')


class Classic(Cliente):
    def __init__(self):
        super().__init__("Classic")

    def tarjeta_debito(self):
        tarjeta_debito=1
        print(f"Puede tener {tarjeta_debito} tarjeta de debito.")
    
    def caja_ahorro(self):
        caja_ahorro="pesos"
        print(f"Puede tener una caja de ahorro en {caja_ahorro} o opcionalmente de dolares con cargo mensual.")
    
    def retiros(self):
        retiros=5
        limite=10000
        print(f"Puede tener {retiros} retiros sin comisiones, luego se aplican una tarifa y tienes un limite de {limite} pesos por cajero.")
    
    def tarjeta_credito(self):
        print("No tienes acceso a tarjeta de credito")
    
    def transferencias(self):
        print("Comisión del 1% por transferencias salientes y 0.5% por transferencias entrantes.")

class Gold(Cliente):
    def __init__(self):
        super().__init__("Gold")

    def tarjeta_debito(self):
        tarjeta_debito=1
        print(f"Puede tener {tarjeta_debito} tarjeta de debito.")
    
    def caja_ahorro(self):
        n_caja_ahorro=2
        caja_ahorro="pesos"
        print(f"Puede tener hasta {n_caja_ahorro} cajas de ahorro en {caja_ahorro} o opcionalmente de dolares con cargo mensual y una cuenta corriente sin cargos adicionales.")
    
    def retiros(self):
        retiros="ilimitados"
        limite=20000
        print(f"Puede tener  retiros {retiros} sin comisiones y tienes un limite de {limite} pesos en retiros diarios.")
    
    def tarjeta_credito(self):
        tartejas_credito="VISA, Mastercard y/o American Express"
        extensiones=5
        limite_un_pago=150000
        limite_cuotas=100000
        print(f"Tiene tarjetas {tartejas_credito} con {extensiones} extensiones cada una y un limite de {limite_un_pago} pesos en un pago y limite de {limite_cuotas} pesos en cuotas")
    
    def transferencias(self):
        print("Comisión del 0.5% por transferencias salientes y 0.1% por transferencias entrantes.")

class Black(Cliente):
    def __init__(self):
        super().__init__("Black")
    def tarjeta_debito(self):
        tarjeta_debito=5
        print(f"Puede tener {tarjeta_debito} tarjetas de debito.")
    
    def caja_ahorro(self):
        n_caja_ahorro=5
        caja_ahorro="pesos"
        caja_ahorro_usd="dolares"
        print(f"Puede tener hasta {n_caja_ahorro} cajas de ahorro en {caja_ahorro} o {caja_ahorro_usd} sin comisiones, luego se aplica uncargo extra.")
    
    def cuenta_corrinete(self):
        n_cuenta_corriente=3
        print(f"Hasta {n_cuenta_corriente}  cuentas corrientes sin cargos adicionales.")
    
    def retiros(self):
        retiros="ilimitados"
        limite=100000
        print(f"Puede tener  retiros {retiros} sin comisiones y tienes un limite de {limite} pesos en retiros diarios.")
    
    def tarjeta_credito(self):
        tartejas_credito="VISA, Mastercard y/o American Express"
        extensiones=10
        limite_un_pago=500000
        limite_cuotas=600000
        print(f"Tiene tarjetas {tartejas_credito} con {extensiones} extensiones cada una y un limite de {limite_un_pago} pesos en un pago y limite de {limite_cuotas} pesos en cuotas")
    
    def cuentas_inversion(self):
        print("Tiene acceso a cuentas inversiones.")

    def chequeras(self):
        print("Posibilidad de tener hasta 2 chequeras.")

    def transferencias(self):
        print("No se aplican comisiones en las transferencias.")

cliente1 = Classic()
cliente1.calcular_monto_total()
cliente1.descontar_comision()
cliente1.calcular_monto_plazo_fijo()
cliente1.ingresar_transacciones()
cliente1.info()

cliente2 = Gold()
cliente2.info()

cliente3 = Black()
cliente3.info()
