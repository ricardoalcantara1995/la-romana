ventas = []           
inventario = []       

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese un número entero válido.")

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingrese un número decimal válido.")

def registrar_venta():
    venta = []
    total = 0
    respuesta = "S"

    while respuesta.upper() != "N":
        producto = input("Producto: ")
        cantidad = pedir_entero("Cantidad (en kg o unidad): ")
        precio = pedir_float("Precio unitario S/: ")

        subtotal = cantidad * precio
        total += subtotal

        venta.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal
        })

        respuesta = input("¿Agregar otro producto? (S/N): ")

    metodo_pago = input("Método de pago (Efectivo/Tarjeta): ")

    if metodo_pago.upper() == "EFECTIVO":
        print(f"Total : S/. {total:.2f}")
        monto_cliente = pedir_float("Monto entregado por el cliente: ")
        vuelto = monto_cliente - total
        print(f"Vuelto: S/. {vuelto:.2f}")
    else:
        vuelto = 0

    ventas.append({
        "items": venta,
        "total": total,
        "metodo_pago": metodo_pago,
        "vuelto": vuelto
    })

    print("\n=== Venta registrada ===")
    print(f"Total a pagar: S/. {total:.2f}")
    print(f"Método de pago: {metodo_pago}\n")


def recepcion_mercaderia():
    respuesta = "S"
    while respuesta.upper() != "N":
        proveedor = input("Proveedor: ")
        producto = input("Producto: ")
        cantidad = pedir_entero("Cantidad: ")

        inventario.append({
            "proveedor": proveedor,
            "producto": producto,
            "cantidad": cantidad
        })

        respuesta = input("¿Agregar otra mercadería? (S/N): ")

    print("\n=== Recepción registrada correctamente ===\n")


def cierre_caja():
    print("\n=== CIERRE DE CAJA ===")
    print("| Producto | Cant | Precio | Subtotal | Pago |")
    print("|----------|------|--------|----------|------|")

    ingreso_total = 0
    efectivo_total = 0
    tarjeta_total = 0

    for v in ventas:
        for item in v["items"]:
            print(f"| {item['producto']} | {item['cantidad']} | S/. {item['precio']:.2f} | S/. {item['subtotal']:.2f} | {v['metodo_pago']} |")
        ingreso_total += v["total"]
        if v["metodo_pago"].upper() == "EFECTIVO":
            efectivo_total += v["total"]
        else:
            tarjeta_total += v["total"]

    print("\n--- Totales ---")
    print(f"Ingreso bruto total: S/. {ingreso_total:.2f}")
    print(f"Ventas en efectivo: S/. {efectivo_total:.2f}")
    print(f"Ventas con tarjeta: S/. {tarjeta_total:.2f}")
    print(f"Cantidad de ventas: {len(ventas)}\n")


def cierre_ingreso_proveedores():
    print("\n=== Cierre de Ingreso de Proveedores ===")
    for item in inventario:
        print(f"- {item['proveedor']} | {item['producto']} | {item['cantidad']} unidades")
    print()


def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Venta")
        print("2. Recepción de Mercadería")
        print("3. Cierre de Caja")
        print("4. Cierre de Ingreso de Proveedores")
        print("5. Salir")

        opc = input("Seleccione opción: ")

        if opc == "1":
            registrar_venta()
        elif opc == "2":
            recepcion_mercaderia()
        elif opc == "3":
            cierre_caja()
        elif opc == "4":
            cierre_ingreso_proveedores()
        elif opc == "5":
            print("Gracias por usar el sistema.")
            break
        else:
            print(" Opción inválida. Intente nuevamente.\n")

menu()
