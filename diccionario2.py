mi_diccionario = {}
import os
sw = True

def fnt_agregar(diccionario, codigo, nombres, apellidos, contacto, correo, edad, estrato, direccion):
    if codigo  == '' or edad == '' or apellidos == '' or estrato  == '' :
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[codigo] = {'nombres': nombres,'apellidos': apellidos, 'contacto': contacto, 'correo': correo, 'edad': edad, 'estrato': estrato, 'direccionario': direccion}
        enter = input(f'\nLa persona {nombres} ha sido registrada con éxito <ENTER>')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        nombres = input('Nombres  ')
        apellidos = input('apellidos:  ')
        contacto = input('contacto:  ')
        correo = input('correo: ')
        edad = input ('edad:  ')
        estrato = input('estrato:  ')
        direccion = input('direccion:  ')
        codigo = input('codigo:  ')
        fnt_agregar(mi_diccionario, nombres, apellidos,contacto, correo, edad, estrato, direccion, codigo )
        
while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for codigo, valor in mi_diccionario.items():
            print(f"{codigo}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False