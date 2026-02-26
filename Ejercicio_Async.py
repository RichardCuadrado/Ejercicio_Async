import asyncio
import random

async def generar_numeros(cantidad, minimo, maximo, paridad ,numero_sublista):
    numeros = []

    while len(numeros) < cantidad:
        numero = random.randint(minimo, maximo)
        
        if paridad == "par" and numero % 2 == 0:
            numeros.append(numero)
        elif paridad == "impar" and numero % 2 != 0:
            numeros.append(numero)
    suma = sum(numeros)

    print(f"Suma sublista{numero_sublista} ({minimo}-{maximo}, {paridad}): {suma}")
    return suma

async def main():
    cantidad_por_lista = 250  

    tarea1 = generar_numeros(cantidad_por_lista, 0, 4999, "par", 1)
    tarea2 = generar_numeros(cantidad_por_lista, 0, 4999, "impar",2)
    tarea3 = generar_numeros(cantidad_por_lista, 5000, 9999, "par", 3)
    tarea4 = generar_numeros(cantidad_por_lista, 5000, 9999, "impar",4)

    # finish 
    resultados = await asyncio.gather(
        tarea1, tarea2, tarea3, tarea4
    )

    # Suma total dentro del finish
    suma_total = sum(resultados)
    print(f"\nSuma total de las 4 sublistas: {suma_total}")

    # Sumar 5000
    resultado_final = suma_total + 5000
    print(f"Resultado final (+5000): {resultado_final}")


asyncio.run(main())