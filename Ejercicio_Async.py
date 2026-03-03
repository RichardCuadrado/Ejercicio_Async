import asyncio
import random
import time

async def generar_numeros(cantidad, minimo, maximo, paridad, numero_sublista):
    numeros = []

    while len(numeros) < cantidad:
        numero = random.randint(minimo, maximo)
        
        if paridad == "par" and numero % 2 == 0:
            numeros.append(numero)
        elif paridad == "impar" and numero % 2 != 0:
            numeros.append(numero)
        
        await asyncio.sleep(0)  # Cede el control al event loop

    suma = sum(numeros)
    print(f"Suma sublista {numero_sublista} ({minimo}-{maximo}, {paridad}): {suma}")
    return suma

async def main():
    print("\nEjecutando versión paralela\n")
    cantidad_por_lista = 250

    # Paralela
    inicio_paralelo = time.perf_counter()

    tarea1 = generar_numeros(cantidad_por_lista, 0, 4999, "par", 1)
    tarea2 = generar_numeros(cantidad_por_lista, 0, 4999, "impar", 2)
    tarea3 = generar_numeros(cantidad_por_lista, 5000, 9999, "par", 3)
    tarea4 = generar_numeros(cantidad_por_lista, 5000, 9999, "impar", 4)

    resultados = await asyncio.gather(tarea1, tarea2, tarea3, tarea4)

    fin_paralelo = time.perf_counter()
    tiempo_paralelo = fin_paralelo - inicio_paralelo

    suma_total = sum(resultados)
    print(f"\nSuma total de las 4 sublistas: {suma_total}")
    resultado_final = suma_total + 5000
    print(f"Resultado final (+5000): {resultado_final}")

    # Secuencial
    print("\nEjecutando versión secuencial\n")
    inicio_secuencial = time.perf_counter()

    t1 = await generar_numeros(cantidad_por_lista, 0, 4999, "par", 1)
    t2 = await generar_numeros(cantidad_por_lista, 0, 4999, "impar", 2)
    t3 = await generar_numeros(cantidad_por_lista, 5000, 9999, "par", 3)
    t4 = await generar_numeros(cantidad_por_lista, 5000, 9999, "impar", 4)

    fin_secuencial = time.perf_counter()
    tiempo_secuencial = fin_secuencial - inicio_secuencial

    suma_total_secuencial = t1 + t2 + t3 + t4
    resultado_final_secuencial = suma_total_secuencial + 5000
    print(f"\nSuma total de las 4 sublistas : {suma_total_secuencial}")
    print(f"Resultado final (+5000) : {resultado_final_secuencial}")


    # WORK Y SPAN
    # Work  = suma del tiempo de todas las tareas 
    # Span  = tiempo de la tarea más larga 
    tiempos_individuales = [t1, t2, t3, t4]  # reutilizamos los resultados
    work = tiempo_secuencial                  # Work ≈ tiempo secuencial total
    span = tiempo_paralelo                    # Span ≈ tiempo paralelo (tarea crítica)
    paralelismo = work / span                 # Paralelismo = Work / Span

    # Resumen
    print("\n════════════════════════════════════════")
    print(f"  Tiempo paralelo   (Span) : {tiempo_paralelo:.6f} s")
    print(f"  Tiempo secuencial (Work) : {tiempo_secuencial:.6f} s")
    print(f"  Paralelismo (Work/Span)  : {paralelismo:.2f}x")
    print("════════════════════════════════════════")


asyncio.run(main())