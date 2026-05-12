#comenzando proyecto
#MODULO DE INGRESO DE MERCADERIA
def ingreso_mercaderia(entradas):
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    repartidor = input("Nombre del repartidor: ")
    boleta = input("¿Dejó boleta? (S/N): ").upper() == "S"

    entradas.append({
        "producto": producto,
        "cantidad": cantidad,
        "repartidor": repartidor,
        "boleta": boleta
    })

    print("Ingreso registrado correctamente")
    
ingreso_mercaderia()

#MODULO DE VENTAS
def registrar_venta(historial_ventas):
    venta = []
    total_venta = 0

    while True:
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))

        subtotal = cantidad * precio
        total_venta += subtotal

        venta.append({
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal
        })

        print(f"Subtotal: {subtotal}")

        resp = input("¿Agregar otro producto? (S/N): ").upper()
        if resp == "N":
            break

    print(f"Total de la venta: {total_venta}")

    metodo_pago = input("Metodo de pago (Efectivo/Tarjeta): ")

    historial_ventas.append({
        "productos": venta,
        "total": total_venta,
        "metodo_pago": metodo_pago
    })
registrar_venta()

#CIERRE DE CAJA
def cierre_caja(historial_ventas):
    ingreso_total = sum(v["total"] for v in historial_ventas)
    cantidad_transacciones = len(historial_ventas)

    print("Ingreso bruto total:", ingreso_total)
    print("Cantidad total de ventas:", cantidad_transacciones)
cierre_caja()


#CONTEO TOTAL DE PROVEEDORES