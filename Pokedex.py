import os, sys
import pickle, json
import requests,webbrowser
import urllib.parse


#FUNCIONES
def Menu():
    print("\n Menu Principal")
    print("\n  A -  Agregar un Pokemon ")
    print("\n  V -  Ver Pokemones")
    print("\n  R -  Reportes")
    print("\n  E - Exportar Pokemones")
    print("\n  M - Exportar Mapa")
    print("\n  S -  Salir")

    while True:
        Accion = input("\n  ¿Que desea hacer? [Seleccione la letra correspondiente]: ")

        if Accion == 'A' or Accion == 'a':
            Agregar()
            break

        elif Accion == 'V' or Accion == 'v':
            Ver()
            break

        elif Accion == 'R' or Accion == 'r':
            Reportes()
            break

        elif Accion == 'E' or Accion == 'e':
            Exportar()
            break

        elif Accion == 'M' or Accion == 'm':
            Mapa()
            break

        elif Accion == 'S' or Accion == 's':
            sys.exit()

        else:
            print("\n  La letra ingresada no esta en el menu, intente nuevamente")

def Agregar():

    os.system('cls')

    #NOMBRE Y VALIDACION
    while True:
        print("\n  Agregar un pokemon ")
        nombre = input("\n  Ingresa el nombre del pokemon: ")

        url = 'https://pokeapi.co/api/v2/pokemon/'+(nombre.lower())
        print("\n  Verificando si "+nombre+" es un pokemon...")
        peticion = requests.get(url)
        validacion = peticion.text

        if not os.path.exists("datos.pickle"):
            pass

        else:
            pickle_in = open("datos.pickle","rb")
            pokemones = pickle.load(pickle_in)

            for pokemon in pokemones:
                if pokemon[0] == nombre:
                    variantes = 2 + len(pokemones) - len(pokemones)
                    nombre = nombre+"_"+str(variantes)



        if validacion == """{"detail":"Not found."}""" or nombre == "":
            print("\n  No existe un Pokemon llamado",nombre)
            print("\n  Porfavor intente nuevamente ")
        else:
            print("\n  El nombre es valido")
            break

    #FECHA DE NACIMIENTO

    #AÑO
    while True:
        Año = int(input("\n  Ingrese el año en que nació su pokemon: "))

        if Año < 1000:
            print("\n  Lo siento mucho su pokemon ha fallecido")
            print("\n  Intentelo nuevamente")

        elif Año > 2018:
            print("\n  Su pokemon viene del futuro o que?, sea mas serio")
            print("\n  Intentelo nuevamente")

        else:
            print("\n  El año se ha agregado correctamente")
            break
    #MES Y DIA [DIA DEPENDE DEL MES]
    month = True
    while month == True:
        Mes = input("\n  Ingrese el mes literal en que nació su pokemon: ")

        #SI EL MES INGRESADO TIENE 31 DIAS
        if Mes.lower() == 'enero' or Mes.lower() == 'marzo' or Mes.lower() == 'mayo' or Mes.lower() == 'julio' or Mes.lower() == 'agosto' or Mes.lower() == 'octubre' or Mes.lower() == 'diciembre':
            while True:
                Dia = int(input("\n  Ingrese el dia: "))
                if Dia < 1 or Dia > 31:
                    print("\n  El dia ingresado no es correcto")
                    print("\n  Porfavor intentelo de nuevo")
                else:
                    #APPEND DEL DIA Y EL MES
                    print("\n  La fecha de nacimiento se ha agregado correctamente")
                    month = False
                    break


        #SI EL MES INGRESADO TIENE 30 DIAS
        elif  Mes.lower() == 'abril' or Mes.lower() == 'junio' or Mes.lower() == 'septiembre' or Mes.lower() == 'noviembre':
            while True:
                Dia = int(input("\n  Ingrese el dia: "))
                if Dia < 1 or Dia > 30:
                    print("\nEl dia ingresado no es correcto")
                    print("\nPorfavor intentelo de nuevo")
                else:
                    #APPEND DEL DIA Y EL MES
                    print("\n  La fecha de nacimiento se ha agregado correctamente")
                    month = False
                    break


        #SI EL MES INGRESADO ES FEBRERO
        elif Mes.lower() == 'febrero':
            while True:
                Dia = int(input("\n  Ingrese el dia: "))
                if Dia < 1 or Dia > 28:
                    print("\n  El dia ingresado no es correcto")
                    print("\n  Porfavor intentelo de nuevo")
                else:
                    #APPEND DEL DIA Y EL MES
                    print("\n  La fecha de nacimiento se ha agregado correctamente")
                    month = False
                    break


    #LATITUD
    Latitud = input("\n  Ingrese la latitud donde usted encontró este pokemon[ex: 34]: ")

    #LONGITUD
    Longitud = input("\n  Ingrese la longitud donde usted encontró este pokemon[ex: 15]: ")

    #COMIDA FAVORITA
    Comida = input("\n  Ingrese la comida favorita de su pokemon: ")

    #TIPO DE SANGRE
    Sangre = input("\n  Ingrese el tipo de sangre que tiene su pokemon[ex: R+]: ")



    #SIGNOS DEL ZODIACO!!!!!
        #ACUARIO
    if Mes.lower() == 'enero' and Dia >= 20 and Dia <= 31:
        Zodiacal = "Acuario"

    elif Mes.lower() == 'febrero' and Dia >= 1 and Dia  <=18:
        Zodiacal = "Acuario"

        #PISCIS
    elif Mes.lower() == 'febrero' and Dia >= 18 and Dia <= 28:
        Zodiacal = "Piscis"

    elif Mes.lower() == 'marzo' and Dia >= 1 and Dia <= 20:
        Zodiacal = "Piscis"

        #ARIES
    elif Mes.lower() == 'marzo' and Dia >= 21 and Dia <= 31:
        Zodiacal = "Aries"

    elif Mes.lower() == 'abril' and Dia >= 1 and Dia <= 19:
        Zodiacal = "Aries"


        #TAURO
    elif Mes.lower() == 'abril' and Dia >= 20 and Dia <= 30:
        Zodiacal = "Tauro"

    elif Mes.lower() == 'mayo' and Dia >= 1 and Dia <= 20:
        Zodiacal = "Tauro"

        #GÉMINIS
    elif Mes.lower() == 'mayo' and Dia >= 21 and Dia <= 31:
        Zodiacal = "Géminis"

    elif Mes.lower() == 'junio' and Dia >= 1 and Dia <= 20:
        Zodiacal = "Géminis"

        #CÁNCER
    elif Mes.lower() == 'junio' and Dia >= 21 and Dia <= 30:
        Zodiacal = "Cáncer"

    elif Mes.lower() == 'julio' and Dia >= 1 and Dia <= 22:
        Zodiacal = "Cáncer"

        #LEO
    elif Mes.lower() == 'julio' and Dia >= 23 and Dia <= 31:
        Zodiacal = "Leo"

    elif Mes.lower() == 'agosto' and Dia >= 1 and Dia <= 22:
        Zodiacal = "Leo"

        #VIRGO
    elif Mes.lower() == 'agosto' and Dia >= 23 and Dia <= 31:
        Zodiacal = "Virgo"

    elif Mes.lower() == 'septiembre' and Dia >= 1 and Dia <= 22:
        Zodiacal = "Virgo"

        #LIBRA
    elif Mes.lower() == 'septiembre' and Dia >= 23 and Dia <= 30:
        Zodiacal = "Libra"

    elif Mes.lower() == 'octubre' and Dia >= 1 and Dia <= 22:
        Zodiacal = "Libra"

        #ESCORPION
    elif Mes.lower() == 'octubre' and Dia >= 23 and Dia <= 31:
        Zodiacal = "Escorpio"

    elif Mes.lower() == 'noviembre' and Dia >= 1 and Dia <= 21:
        Zodiacal = "Escorpio"

        #SAGITARIO
    elif Mes.lower() == 'noviembre' and Dia >= 22 and Dia <= 30:
        Zodiacal = "Sagitario"

    elif Mes.lower() == 'diciembre' and Dia >= 1 and Dia <= 21:
        Zodiacal = "Sagitario"

        #CAPRICORNIO
    elif Mes.lower() == 'diciembre' and Dia >= 22 and Dia <= 31:
        Zodiacal = "Capricornio"

    elif Mes.lower() == 'enero' and Dia >= 1 and Dia <= 19:
        Zodiacal = "Capricornio"


    #TIPO Y FOTO DE POKEMON
    print("\n  Procesando informacion de",nombre)

    data = requests.get(url).json()

    Tipo = data['types'][0]['type']['name']
    Foto = data['sprites']['front_default']

    #TRADUCCION HECHA POR FRANK OROZCO XD
    if Tipo == 'normal':
        Tipo = 'Normal'
    elif Tipo == 'fire':
        Tipo = "Fuego"
    elif Tipo == 'water':
        Tipo = "Agua"
    elif Tipo == 'grass':
        Tipo = "Planta"
    elif Tipo == 'electric':
        Tipo = "Electrico"
    elif Tipo == 'ice':
        Tipo = "Hielo"
    elif Tipo == 'fighting':
        Tipo = "Peleador"
    elif Tipo == 'poison':
        Tipo = "Veneno"
    if Tipo == 'ground':
        Tipo = "Tierra"
    elif Tipo == 'flying':
        Tipo = "Volador"
    elif Tipo == 'psychic':
        Tipo = "Psiquico"
    elif Tipo == 'bug':
        Tipo = "Bicho"
    if Tipo == 'rock':
        Tipo = "Roca"
    elif Tipo == 'ghost':
        Tipo = "Fantasma"
    elif Tipo == 'dragon':
        Tipo = "Dragon"
    elif Tipo == 'dark':
        Tipo = "Oscuro"
    elif Tipo == 'steel':
        Tipo = "Acero"
    elif Tipo == 'fairy':
        Tipo = "Hada"


    #AGREGANDO LOS DATOS
    pokemon = []

    pokemon.append(nombre.lower())
    pokemon.append(str(Dia)+"/"+Mes.lower()+"/"+str(Año))
    pokemon.append(Latitud)
    pokemon.append(Longitud)
    pokemon.append(Comida)
    pokemon.append(Sangre)
    pokemon.append(Zodiacal)
    pokemon.append(Tipo)
    pokemon.append(Mes.lower())
    pokemon.append(Año)
    pokemon.append(Foto)


    input("\n  PRESIONE 'ENTER' PARA GUARDAR LOS DATOS")

    #CARGAR PICKLE

    #SI EXISTE EL ARCHIVO DE SERIALIZACION
    if os.path.exists("datos.pickle"):
        pickle_in = open("datos.pickle","rb")
        pokemones = pickle.load(pickle_in)

        pokemones.append(pokemon)
        pickle_out = open("datos.pickle","wb")
        pickle.dump(pokemones,pickle_out)
        pickle_out.close()

    #SI NO EXISTE
    else:
        pokemones = []
        pokemones.append(pokemon)
        pickle_out = open("datos.pickle","wb")
        pickle.dump(pokemones,pickle_out)
        pickle_out.close()

    os.system('cls')

    Menu()

def Ver():

    os.system('cls')

    if not os.path.exists("datos.pickle"):
        print("\n  No has creado ningun pokemon")


    else:
        print("  ")
        print("  ")
        print("\n                                               Ver Pokemones")
        pickle_in = open("datos.pickle","rb")
        pokemones = pickle.load(pickle_in)

        #pokemon[0] NOMBRE
        #pokemon[1] FECHA
        #pokemon[5] SANGRE
        #pokemon[6] ZODIACAL
        #pokemon[7] TIPO

        print("")
        print("         | NOMBRE DEL POKEMON | FECHA DE NACIMIENTO | SANGRE | SIGNO ZODIACAL | TIPO DE POKEMON |")
        print("          --------------------------------------------------------------------------------------")

        for pokemon in pokemones:
            print("         |",pokemon[0]," "*(17-len(pokemon[0])),"|",pokemon[1]," "*(18-len(pokemon[1])),"|",pokemon[5],
            " "*(5-len(pokemon[5])),"|",pokemon[6]," "*(13-len(pokemon[6])),"|",pokemon[7]," "*(14-len(pokemon[7])),"|")



    print("\n ")
    input("\n                           PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

    os.system('cls')

    Menu()




    #CARGA LOS DATOS



    input()

def Reportes():

    os.system('cls')

    print("\n  Reportes")
    print("\n  M -  Cumpleaños por mes ")
    print("\n  T -  Pokemones por tipo")
    print("\n  C -  Comida por tipo")
    print("\n  V -  Volver al Menu Principal")

    while True:
        Accion = input("\n  ¿Que desea hacer? [Seleccione las letras correspondiente]: ")

        if Accion == 'M' or Accion == 'm':
            Cumpleaños()
            break

        elif Accion == 'T' or Accion == 't':
            Tipo()
            break

        elif Accion == 'C' or Accion == 'c':
            Comida()
            break

        elif Accion == 'V' or Accion == 'v':
            os.system('cls')
            Menu()
            break

        else:
            print("\n  La letra ingresada no esta en el menu, intente nuevamente")

def Exportar():


    os.system('cls')

    if not os.path.exists("datos.pickle"):
        print("\n  No has creado ningun pokemon")


    else:

        pickle_in = open("datos.pickle","rb")
        pokemones = pickle.load(pickle_in)
        nombres = []

        print("\n  Exportar pokemon")

        print("\n  Estos son tus pokemones: ")

        for pokemon in pokemones:
            print("\n  ",pokemon[0])

        elegir = True
        encontrado = False
        while elegir == True:

            exp = input("\n  Ingresa el nombre del pokemon que desea exportar: ")

            for pokemon in pokemones:
                name = pokemon[0]

                if name == exp.lower():
                    nombre = (pokemon[0])
                    tipo = (pokemon[7])
                    edad = (2018 - pokemon[9])
                    sangre = (pokemon[5])
                    fecha = (pokemon[1])
                    latitud = (pokemon[2])
                    longitud = (pokemon[3])
                    comida = (pokemon[4])
                    signo = (pokemon[6])
                    foto = (pokemon[10])

                    datos = """<tr>
                    <td>"""+nombre+"""</td>
                    <td>"""+tipo+"""</td>
                    <td>"""+str(edad)+"""</td>
                    <td>"""+sangre+"""</td>
                    <td>"""+fecha+"""</td>
                    <td>"""+latitud+"""</td>
                    <td>"""+longitud+"""</td>
                    <td>"""+comida+"""</td>
                    <td>"""+signo+"""</td>
                    <td><img src="""+foto+"""></td>
                    </tr>
                    """

                    while True:
                        h = input("\n  Ingresa el nombre del archivo html: ")

                        if os.path.exists("Pokemones/"+h+".html"):
                            print("\n  Ya hay un archivo con ese nombre.")
                            print("\n  Intentelo nuevamente")

                        else:

                            file = open("Base/base.html").read()
                            s = file.replace('<!-- DATOS -->', datos)

                            f = open("Pokemones/"+h+".html", 'w')
                            f.write(s)
                            f.close()
                            encontrado = True
                            elegir = False
                            break

                else:
                    pass

            if encontrado == False:
                print("\n  El pokemon que intentas exportar no esta aun creado o no existe ")
            else:
                pass

        print("\n  Pokemon importado correctamente!")

    input("\n  PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")
    os.system('cls')

    Menu()

def Mapa():
    os.system('cls')

    if not os.path.exists("datos.pickle"):
        print("\n  No has creado ningun pokemon")

    else:
        #BORRANDO DATOS ANTIGUOS

        datos = """ <!DOCTYPE html>
            <html>
        	<head>
        		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        		<title>Ejemplo de mapa</title>
        		<link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css">
        		<script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>
        	</head>
        	<body style="background-color:#78909C">
        		<center><h2 style="margin-top:10%;">UBICACION DE MIS POKEMONES</h2></center>

        		<div id="divMap" class="map map-home" style="margin:12px 10% 0px 10%;height:400px;width:80%"></div>
        		<script>
        			var osmUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        				osmAttrib = '&copy; <a href="http://adamix.net">Amadis Suarez</a> contributors',
        				osm = L.tileLayer(osmUrl, {maxZoom: 20, attribution: osmAttrib});
        			var map = L.map('divMap').setView([19.4398315,-70.8132746], 8).addLayer(osm);

              // DATOS

        		</script>
        		<p>
        			<center>Mapa realizado por Amadis</center>
        		</p>
                </body>
                </html>
                    """

        file = open("mapa.html").read()
        f = open("mapa.html", 'w')
        f.write(datos)
        f.close()


        #CARGANDO DATOS

        print("\n  Exportar en Mapa")
        pickle_in = open("datos.pickle","rb")
        pokemones = pickle.load(pickle_in)

        #ESCRIBIENDO EN EL MAPA

        for pokemon in pokemones:
            nombre = (pokemon[0])
            edad = (2018 - pokemon[9])
            latitud = (pokemon[2])
            longitud = (pokemon[3])

            datos = """ L.marker(["""+latitud+""","""+longitud+"""])
            			.addTo(map)
            			.bindPopup('Nombre: """+nombre+""" ,edad: """+str(edad)+"""');

                        // DATOS
                        """

            file = open("mapa.html").read()
            s = file.replace('// DATOS', datos)
            f = open("mapa.html", 'w')
            f.write(s)
            f.close()

        os.system('mapa.html')

        print("\n  El Mapa se ha exportado correctamente")

    input("\n  PRESIONE ENTER PARA VOLVER AL MENU PRINCIPAL")

    os.system('cls')

    Menu()


#SUB-FUNCIONES [REPORTES]

def Cumpleaños():

    os.system('cls')

    if not os.path.exists("datos.pickle"):
        print("\n  No has creado ningun pokemon")

        input("\n  PRESIONE ENTER PARA VOLVER A REPORTES")
        os.system('cls')

        Reportes()

    else:
        print("\n  Cumpleaños por Mes: ")

        pickle_in = open("datos.pickle","rb")
        pokemones = pickle.load(pickle_in)



        cumpleaños = True
        hay = False
        while cumpleaños == True:
            cant = []
            hay = False
            mes = input("\n  Ingrese un mes: ")

            for pokemon in pokemones:
                if pokemon[8] == mes.lower():
                    cant.append(pokemon[0])
                    hay = True

            if hay == True and len(cant) > 1:
                print("\n  Los pokemones que cumplen años en",mes,"son:",cant)

            elif len(cant) == 1 and hay == True:
                print("\n El unico pokemon que cumple año en",mes,"es:",cant[0])

            else:
                print("\n  Ninguno de los pokemones cumplen año en ese mes")

            while True:
                continuar = input("\n  Desea volver a intentarlo? [S/N]: ")
                if continuar == 'S' or continuar == 's':

                    os.system('cls')
                    break

                elif continuar == 'N' or continuar == 'n' :
                    cumpleaños = False
                    break

                else:
                    print("\n  Tiene que especificar Si con S, o No con N ")

    Reportes()

def Tipo():

    os.system('cls')

    if not os.path.exists("datos.pickle"):
        print("\n  No has creado ningun pokemon")

        input("\n  PRESIONE ENTER PARA VOLVER A REPORTES")
        os.system('cls')

        Reportes()

    else:
        print("\n                                   Pokemones por tipo")

        pickle_in = open("datos.pickle","rb")
        pokemones = pickle.load(pickle_in)

        normal = []
        fuego = []
        agua = []
        planta = []
        electrico = []
        hielo = []
        peleador = []
        veneno = []
        tierra = []
        volador = []
        psiquico = []
        bicho = []
        roca = []
        fantasma = []
        dragon = []
        oscuro = []
        acero = []
        hada = []


        #TIPOS DE POKEMONES

        print("")
        print("                             | CANTIDAD | TIPO DE POKEMON |")
        print("                             ------------------------------")

        for pokemon in pokemones:
            if pokemon[7] == 'Normal':
                normal.append(1)
            elif pokemon[7] == 'Fuego':
                fuego.append(1)
            elif pokemon[7] == 'Agua':
                agua.append(1)
            elif pokemon[7] == 'Planta':
                planta.append(1)
            if pokemon[7] == 'Electrico':
                electrico.append(1)
            elif pokemon[7] == 'Hielo':
                hielo.append(1)
            elif pokemon[7] == 'Peleador':
                peleador.append(1)
            elif pokemon[7] == 'Veneno':
                veneno.append(1)
            if pokemon[7] == 'Tierra':
                tierra.append(1)
            elif pokemon[7] == 'Volador':
                volador.append(1)
            elif pokemon[7] == 'Psiquico':
                psiquico.append(1)
            elif pokemon[7] == 'Bicho':
                bicho.append(1)
            if pokemon[7] == 'Roca':
                roca.append(1)
            elif pokemon[7] == 'Fantasma':
                fantasma.append(1)
            elif pokemon[7] == 'Dragon':
                dragon.append(1)
            elif pokemon[7] == 'Oscuro':
                oscuro.append(1)
            elif pokemon[7] == 'Acero':
                acero.append(1)
            elif pokemon[7] == 'Hada':
                hada.append(1)

                #SI EXISTE


        if len(normal) == 0:
            pass
        else:
            print("                             |",len(normal)," "*(15-len(pokemon[7])),"|","Normal"," "*(14-len("Normal")),"|")

        if len(fuego) == 0:
            pass
        else:
            print("                             |",len(fuego)," "*(15-len(pokemon[7])),"|","Fuego"," "*(14-len("Fuego")),"|")

        if len(agua) == 0:
            pass
        else:
            print("                             |",len(agua)," "*(15-len(pokemon[7])),"|","Agua"," "*(14-len("Agua")),"|")

        if len(planta) == 0:
            pass
        else:
            print("                             |",len(planta)," "*(15-len(pokemon[7])),"|","Planta"," "*(14-len("Planta")),"|")


        if len(electrico) == 0:
            pass
        else:
            print("                             |",len(electrico)," "*(15-len(pokemon[7])),"|","Electrico"," "*(14-len("Electrico")),"|")


        if len(hielo) == 0:
            pass
        else:
            print("                             |",len(hielo)," "*(15-len(pokemon[7])),"|","Hielo"," "*(14-len("Hielo")),"|")


        if len(peleador) == 0:
            pass
        else:
            print("                             |",len(peleador)," "*(15-len(pokemon[7])),"|","Peleador"," "*(14-len("Peleador")),"|")


        if len(veneno) == 0:
            pass
        else:
            print("                             |",len(veneno)," "*(15-len(pokemon[7])),"|","Veneno"," "*(14-len("Veneno")),"|")


        if len(tierra) == 0:
            pass
        else:
            print("                             |",len(tierra)," "*(15-len(pokemon[7])),"|","Tierra"," "*(14-len("Tierra")),"|")


        if len(volador) == 0:
            pass
        else:
            print("                             |",len(volador)," "*(15-len(pokemon[7])),"|","Volador"," "*(14-len("Volador")),"|")


        if len(psiquico) == 0:
            pass
        else:
            print("                             |",len(psiquico)," "*(15-len(pokemon[7])),"|","Psiquico"," "*(14-len("Psiquico")),"|")


        if len(bicho) == 0:
            pass
        else:
            print("                             |",len(bicho)," "*(15-len(pokemon[7])),"|","Bicho"," "*(14-len("Bicho")),"|")


        if len(roca) == 0:
            pass
        else:
            print("                             |",len(roca)," "*(15-len(pokemon[7])),"|","Roca"," "*(14-len("Roca")),"|")


        if len(fantasma) == 0:
            pass
        else:
            print("                             |",len(fantasma)," "*(15-len(pokemon[7])),"|","Fantasma"," "*(14-len("Fantasma")),"|")


        if len(dragon) == 0:
            pass
        else:
            print("                             |",len(dragon)," "*(15-len(pokemon[7])),"|","Dragon"," "*(14-len("Dragon")),"|")


        if len(oscuro) == 0:
            pass
        else:
            print("                             |",len(oscuro)," "*(15-len(pokemon[7])),"|","Oscuro"," "*(14-len("Oscuro")),"|")


        if len(acero) == 0:
            pass
        else:
            print("                             |",len(acero)," "*(15-len(pokemon[7])),"|","Acero"," "*(14-len("Acero")),"|")

        if len(hada) == 0:
            pass
        else:
            print("                             |",len(hada)," "*(15-len(pokemon[7])),"|","Hada"," "*(14-len("Hada")),"|")


    print("\n ")
    input("\n                           PRESIONE ENTER PARA VOLVER A REPORTES")
    Reportes()

def Comida():
    os.system('cls')

    if not os.path.exists("datos.pickle"):
        print("\n  No has creado ningun pokemon")

        input("\n  PRESIONE ENTER PARA VOLVER A REPORTES")
        os.system('cls')

        Reportes()

    else:
        print("\n")
        print("\n                             Tipos de pokemones y su comida favorita")

        pickle_in = open("datos.pickle","rb")
        pokemones = pickle.load(pickle_in)

        normal = []
        fuego = []
        agua = []
        planta = []
        electrico = []
        hielo = []
        peleador = []
        veneno = []
        tierra = []
        volador = []
        psiquico = []
        bicho = []
        roca = []
        fantasma = []
        dragon = []
        oscuro = []
        acero = []
        hada = []

        for pokemon in pokemones:
            if pokemon[7] == "Normal":
                normal.append(pokemon[4])
            elif pokemon[7] == "Fuego":
                fuego.append(pokemon[4])
            elif pokemon[7] == "Agua":
                agua.append(pokemon[4])
            elif pokemon[7] == "Planta":
                planta.append(pokemon[4])
            elif pokemon[7] == "Electrico":
                electrico.append(pokemon[4])
            elif pokemon[7] == "Hielo":
                hielo.append(pokemon[4])
            elif pokemon[7] == "Peleador":
                peleador.append(pokemon[4])
            elif pokemon[7] == "Veneno":
                veneno.append(pokemon[4])
            elif pokemon[7] == "Tierra":
                tierra.append(pokemon[4])
            if pokemon[7] == "Volador":
                volador.append(pokemon[4])
            elif pokemon[7] == "Psiquico":
                psiquico.append(pokemon[4])
            elif pokemon[7] == "Bicho":
                bicho.append(pokemon[4])
            elif pokemon[7] == "Roca":
                roca.append(pokemon[4])
            elif pokemon[7] == "Fantasma":
                fantasma.append(pokemon[4])
            if pokemon[7] == "Dragon":
                dragon.append(pokemon[4])
            elif pokemon[7] == "Oscuro":
                oscuro.append(pokemon[4])
            elif pokemon[7] == "Acero":
                acero.append(pokemon[4])
            elif pokemon[7] == "Hada":
                hada.append(pokemon[4])



        print("\n")
        print("                             |   TIPO DE POKEMON  |  COMIDA FAVORITA  ")
        print("                             ------------------------------------------")

        if len(normal) > 0:
            print("                             |","Normal"," "*(17 - len("Normal")),"|",normal)

        if len(fuego) > 0:
            print("                             |","Fuego"," "*(17 - len("Fuego")),"|",fuego)
        if len(agua) > 0:
            print("                             |","Agua"," "*(17 - len("Agua")),"|",agua)

        if len(planta) > 0:
            print("                             |","Planta"," "*(17 - len("Planta")),"|",planta)

        if len(electrico) > 0:
            print("                             |","Electrico"," "*(17 - len("Electrico")),"|",electrico)

        if len(hielo) > 0:
            print("                             |","Hielo"," "*(17 - len("Hielo")),"|",hielo)
        if len(peleador) > 0:
            print("                             |","Peleador"," "*(17 - len("Peleador")),"",peleador)

        if len(veneno) > 0:
            print("                             |","Veneno"," "*(17 - len("Veneno")),"|",veneno)

        if len(tierra) > 0:
            print("                             |","Tierra"," "*(17 - len("Tierra")),"|",tierra)

        if len(volador) > 0:
            print("                             |","Volador"," "*(17 - len("Volador")),"|",volador)

        if len(psiquico) > 0:
            print("                             |","Psiquico"," "*(17 - len("Psiquico")),"|",psiquico)

        if len(bicho) > 0:
            print("                             |","Bicho"," "*(17 - len("Bicho")),"|",bicho)

        if len(roca) > 0:
            print("                             |","Roca"," "*(17 - len("Roca")),"|",roca)

        if len(fantasma) > 0:
            print("                             |","Fantasma"," "*(17 - len("Fantasma")),"|",fantasma)

        if len(dragon) > 0:
            print("                             |","Dragon"," "*(17 - len("Dragon")),"|",dragon)

        if len(oscuro) > 0:
            print("                             |","Oscuro"," "*(17 - len("Oscuro")),"|",oscuro)

        if len(acero) > 0:
            print("                             |","Acero"," "*(17 - len("Acero")),"|",acero)

        if len(hada) > 0:
            print("                             |","Hada"," "*(17 - len("Hada")),"|",hada)

    print("\n ")
    input("\n                                PRESIONE ENTER PARA VOLVER A REPORTES")
    Reportes()


#INICIO DEL PROGRAMA
print("\n BIENVENIDO AL POKEDEX CREADO POR FRANK OROZCO")

Menu()
