respuesta = input('¿Estás en ayunas? (si/no): ').strip().lower()
ayunas = respuesta == 'si'  

if ayunas:
    print('No se puede donar si estás en ayunas')
else:
    edad = int(input('Introduzca la edad: '))
    if (edad >= 18 and edad <= 50):
        peso = float(input('Peso: '))
        if (peso > 50):
            tensionDiastolica = int(input('Introduzca la tensión diastólica: '))
            if (tensionDiastolica >= 50 and tensionDiastolica <= 100):
                tensionSistolica = int(input('Introduzca la tensión sistólica: '))
                if (tensionSistolica >= 90 and tensionSistolica <= 180):
                    pulso = int(input('Introduzca la frecuencia cardíaca: '))
                    if (pulso >= 50 and pulso <= 180):
                        plaquetas = int(input('Introduzca las plaquetas totales: '))
                        if (plaquetas > 150000):
                            proteinas = int(input('Introduzca las proteínas totales: '))
                            if (proteinas > 6):
                                sexo = input('Introduzca el sexo "M" o "F": ')
                                hemoglobina = int(input('Introduzca el valor de hemoglobina: '))
                                match sexo:
                                    case 'F':
                                        if (hemoglobina > 12.5):
                                            print('Es apto para donar sangre')
                                        else:
                                            print('No ha podido donar sangre')
                                    case 'M':
                                        if (hemoglobina > 13.5):
                                            print('Es apto para donar sangre')
                                        else:
                                            print('No ha podido donar sangre')
                            else:
                                print('No se puede donar con esas proteínas')
                        else:
                            print('Las plaquetas deben ser mayores de 150000')
                    else:
                        print('No se puede donar con ese pulso')
                else:
                    print('No se puede donar con esa tensión')
            else:
                print('No se puede donar con esa tensión')
        else:
            print('No se puede donar con este peso')
    else:
        print('No se puede donar con esa edad')