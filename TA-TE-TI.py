


def pintar_tablero(matriz):
    print('|' + str(matriz[0][0]) + '|' + str(matriz[0][1]) + '|' + str(matriz[0][2]) + '|')
    print('|' + str(matriz[1][0]) + '|' + str(matriz[1][1]) + '|' + str(matriz[1][2]) + '|')
    print('|' + str(matriz[2][0]) + '|' + str(matriz[2][1]) + '|' + str(matriz[2][2]) + '|')


print("TATETI o bien conocido como el gato")


ocupacion = 0
while True:
    try:
       print("Para jugar ingrese la opcion 1 para jugar o 2 para terminar el juego")
       opcion = int(input("Opcion: "))
    except:
        print("El valor ingresado no es numérico!")
    else:
        if opcion == 1:
            print("Empezemos a jugar")
            l = '_' 
            tablero = [
                [l,l,l],
                [l,l,l],
                [l,l,l]
            ]
            pintar_tablero(tablero)
            while True:
                estado = input("Ingrese el simbolo a jugar (X/O): ")
                if 'X' == estado or estado.upper() == 'X':
                    print("Las X empiezan adelante")
                    
                    while True:
                        entrada = input('Ingrese la coordenada en formato fila-columna: ')
                        coordenadas = entrada.split('-')
                        f = int(coordenadas[0])
                        c = int(coordenadas[1])
                        if tablero[f][c] == "X" or tablero[f][c] == "O":
                                print("La posición ingresada ya se encuentra ocupada")
                            
                        else:          
                            tablero[f][c] = 'X'              
                            pintar_tablero(tablero)
                            ocupacion += 1
                            print("Le toca al jugador 2")
                            break
                        
                        


                    
                elif estado == "O" or estado.upper() == "O":
                    print("Las O comienzan adelante")
                    
                    while True: 
                        
                        entrada = input('Ingrese la coordenada en formato fila-columna: ')
                        coordenadas = entrada.split('-')
                        f = int(coordenadas[0])
                        c = int(coordenadas[1])
                        if tablero[f][c] == "X" or tablero[f][c] == "O":
                            print("La posición ingresada ya se encuentra ocupada")
                            
                        else:          
                            tablero[f][c] = 'O'              
                            pintar_tablero(tablero)
                            ocupacion += 1
                            print("Le toca al jugador 1")
                            break

                if  (tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X") or (tablero[0][0] == "O" and tablero[0][1] == "O" and tablero[0][2] == "O"):
                    print("ganaste") 
                    break
                elif (tablero[1][0] == 'X' and tablero[1][1] == 'X' and tablero[1][2] == 'X') or (tablero[1][0] == 'O' and tablero[1][1] == 'O' and tablero[1][2] == 'O'):
                    print("ganaste")
                    break
                elif (tablero[2][0] == 'X' and tablero[2][1] == 'X' and tablero[2][2] == 'X') or (tablero[2][0] == 'O' and tablero[2][1] == 'O' and tablero[2][2] == 'O'):
                    print("ganaste")
                    break
                elif  (tablero[0][0] == 'X' and tablero[1][0] == 'X' and tablero[2][0] == 'X') or (tablero[0][0] == 'O' and tablero[1][0] == 'O' and tablero[2][0] == 'O'):
                    print("ganaste")
                    break 
                elif (tablero[0][1] == 'X' and tablero[1][1] == 'X' and tablero[2][1] == 'X') or (tablero[0][1] == 'O' and tablero[1][1] == 'O' and tablero[2][1] == 'O'):
                    print("ganaste")
                    break 
                elif (tablero[0][2] == 'X' and tablero[1][2] == 'X' and tablero[2][2] == 'X') or (tablero[0][2] == 'O' and tablero[1][2] == 'O' and tablero[2][2] == 'O'):
                    print("Ganaste")
                    break 
                elif (tablero[0][0] == 'X' and tablero[1][1] == 'X' and tablero[2][2] == 'X') or (tablero[0][0] == 'O' and tablero[1][1] == 'O' and tablero[2][2] == 'O'):
                    print("ganaste")
                    break 
                elif (tablero[0][2] == 'X' and tablero[1][1] == 'X' and tablero[2][0] == 'X') or (tablero[0][2] == 'O' and tablero[1][1] == 'O' and tablero[2][0] == 'O'):
                    print("ganaste")
                    break

                if ocupacion == 9:
                    print("EMPATE")
                    break
         
         


        elif opcion == 2: 
            print("gracias por jugar")
            break
                    
                

