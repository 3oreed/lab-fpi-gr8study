# CREATORS:
# Byron Caices Lima & Aracely Castro Venegas

# IMPORTACION DE MODULOS

import math
import tkinter as tk
from tkinter import ttk, Frame
from PIL import Image, ImageTk

# BLOQUE DE DEFINICIONES #

reps = 0
timer = None

def hide(): #Sin uso
    my_notebook.hide(1)


def show(): #Sin uso
    my_notebook.add(frame1_VAK, text='Red Tab')


def hide_tabs(): 
    for i in range (4,8):
        my_notebook.hide(i)


def gotoVAK():
    my_notebook.select(1)


def gotoPom():
    my_notebook.select(2)


def gotoMetodos():
    my_notebook.select(3)
    for i in range (4,7):
        my_notebook.hide(i)


def gotoVisual():
    my_notebook.select(4)


def gotoAuditivo():
    my_notebook.select(5)


def gotoKine():
    my_notebook.select(6)


def gotoResultados():
    #getResultado()
    my_notebook.select(7)


def our_command(): #Sin uso
    pass

# FUNCIONES VAK


def infoVak():

    ''' Función que entrega el texto sobre la información del test de Vak
        Entrada: No necesita argumentos, solo ser llamada
        Salida: Un string'''

    textInfoVak = "El test de Vak permite cuál de los tres canales de aprendizaje es más acorde a \n \
                la persona. Pudiendo ser el canal visual, auditivo o kinestesico. \n \
                Saber cuál de estas vias preferentes de entrada, procesamiento y \n \
                salida de la información predominan en la persona permitirá elaborar \n \
                una mejor comunicación del aprendizaje por medio de métodos de estudio \n \
                relacionados con ese canal."
                    

    return textInfoVak


def ShowAnswer():

    ''' Función que revisa las opciones seleccionadas por el usuario y los guarda en una variable unica para cada pregunta
        Entrada: No necesita argumentos, solo ser llamanda
        Salida: Retorna un string de la opción escogida para cada pregunta
    '''

    # Se llaman a las globales
    global selection1
    global selection2
    global selection3
    global selection4
    global selection5
    global selection6
    global selection7
    global selection8
    global selection9
    global selection10

    # OPCIONES PARA LA PREGUNTA 1
    if Question1.get() == 1:
        selection1 = "A"

    if Question1.get() == 2:
        selection1 = "B"

    if Question1.get() == 3:
        selection1 = "C"

    #------------------------------------------------------#

    # OPCIONES PARA LA PREGUNTA 2
    
    if Question2.get() == 1:
        selection2 = "A"

    if Question2.get() == 2:
        selection2 = "B"

    if Question2.get() == 3:
        selection2 = "C"

    #------------------------------------------------------#

        # OPCIONES PARA LA PREGUNTA 3
    if Question3.get() == 1:
        selection3 = "A"

    if Question3.get() == 2:
        selection3 = "B"

    if Question3.get() == 3:
        selection3 = "C"

    
    #------------------------------------------------------#

    # OPCIONES PARA LA PREGUNTA 4
    if Question4.get() == 1:
        selection4 = "A"

    if Question4.get() == 2:
        selection4 = "B"

    if Question4.get() == 3:
        selection4 = "C"

    #------------------------------------------------------#

   # OPCIONES PARA LA PREGUNTA 5
    if Question5.get() == 1:
        selection5 = "A"

    if Question5.get() == 2:
        selection5 = "B"

    if Question5.get() == 3:
        selection5 = "C"
    #------------------------------------------------------#

    # OPCIONES PARA LA PREGUNTA 6
    if Question6.get() == 1:
        selection6 = "A"

    if Question6.get() == 2:
        selection6 = "B"

    if Question6.get() == 3:
        selection6 = "C"

    #------------------------------------------------------#

    # OPCIONES PARA LA PREGUNTA 7
    if Question7.get() == 1:
        selection7 = "A"

    if Question7.get() == 2:
        selection7 = "B"

    if Question7.get() == 3:
        selection7 = "C"

    #------------------------------------------------------#

    # OPCIONES PARA LA PREGUNTA 8
    if Question8.get() == 1:
        selection8 = "A"

    if Question8.get() == 2:
        selection8 = "B"

    if Question8.get() == 3:
        selection8 = "C"

    #------------------------------------------------------#

    # OPCIONES PARA LA PREGUNTA 9
    if Question9.get() == 1:
        selection9 = "A"

    if Question9.get() == 2:
        selection9 = "B"

    if Question9.get() == 3:
        selection9 = "C"

    #------------------------------------------------------#

    # OPCIONES PARA LA PREGUNTA 10
    if Question10.get() == 1:
        selection10 = "A"

    if Question10.get() == 2:
        selection10 = "B"

    if Question10.get() == 3:
        selection10 = "C"

    # Imprimir las variables para poder ver como cambiar (se quita después si se quiere)
    print(selection1)
    print(selection2)
    print(selection3)
    print(selection4)
    print(selection5)
    print(selection6)
    print(selection7)
    print(selection8)
    print(selection9)
    print(selection10 + "\n")

    return True


#-------------------------------------------------------------------------------------------------------------------------------------#

def ResultVak(selection1, selection2, selection3, selection4, selection5, selection6, selection7, selection8, selection9, selection10):
    ''' Función que valoriza los resultados de las opciones dadas según su estilo de aprendizaje
        Entrada: Todas las variables string de las preguntas
        Salida: Una lista con los resultado de cada área, o un entero 0 cuando le falto al usuario marcar una opción
    '''

    countVisual = 0
    countAuditory = 0
    countKinesthetic = 0

    # Valores pregunta 1
    if selection1 == "A":
        countAuditory += 1

    elif selection1 == "B":
        countVisual += 1

    elif selection1 == "C":
        countKinesthetic += 1

    else:
        return 0
        
        

    # Valores pregunta 2
    if selection2 == "A":
        countVisual += 1

    elif selection2 == "B":
        countKinesthetic += 1

    elif selection2 == "C":
        countAuditory += 1

    else:
        return 0
        

    # Valores pregunta 3
    if selection3 == "A":
        countAuditory += 1

    elif selection3 == "B":
        countVisual += 1

    elif selection3 == "C":
        countKinesthetic += 1

    else:
        return 0
        

    # Valores pregunta 4
    if selection4 == "A":
        countKinesthetic += 1

    elif selection4 == "B":
        countAuditory += 1

    elif selection4 == "C":
        countVisual += 1

    else:
        return 0
        

    # Valores pregunta 5
    if selection5 == "A":
        countKinesthetic += 1

    elif selection5 == "B":
        countAuditory += 1

    elif selection5 == "C":
        countVisual += 1
    
    else:
        return 0
        

    # Valores pregunta 6
    if selection6 == "A":
        countAuditory += 1

    elif selection6 == "B":
        countVisual += 1

    elif selection6 == "C":
        countKinesthetic += 1
    
    else:
        return 0
        

    # Valores pregunta 7
    if selection7 == "A":
        countVisual += 1
    
    elif selection7 == "B":
        countAuditory += 1

    elif selection7 == "C":
        countKinesthetic += 1

    else:
        return 0
        

    # Valores pregunta 8
    if selection8 == "A":
        countAuditory += 1

    elif selection8 == "B":
        countVisual += 1

    elif selection8 == "C":
        countKinesthetic += 1

    else:
        return 0
        

    # Valores pregunta 9
    if selection9 == "A":
        countVisual += 1
    
    elif selection9 == "B":
        countKinesthetic += 1

    elif selection9 == "C":
        countAuditory += 1

    else:
        return 0
        

    # Valores pregunta 10
    if selection10 == "A":
        countAuditory += 1

    elif selection10 == "B":
        countVisual += 1

    elif selection10 == "C":
        countKinesthetic += 1

    else:
        return 0
        
    # Lista con los valores finales
    lista_EA = [countVisual, countAuditory, countKinesthetic]
    
    print(lista_EA)

    return lista_EA

#------------------------------------------------------------------------------------------#
def makeResults():

    global selection1
    global selection2
    global selection3
    global selection4
    global selection5
    global selection6
    global selection7
    global selection8
    global selection9
    global selection10

    resultado = ''
    lista_EA = ResultVak(selection1, selection2, selection3, selection4,
     selection5, selection6, selection7, selection8, selection9, selection10)

    if (lista_EA[0] > lista_EA[1]) and (lista_EA[0] > lista_EA[2]) :
        resultado = resultado + 'Visual'

    elif (lista_EA[1] > lista_EA[0]) and (lista_EA[1] > lista_EA[2]) :
        resultado = resultado + 'Auditivo'

    elif (lista_EA[2] > lista_EA[0]) and (lista_EA[2] > lista_EA[1]) :
        resultado = resultado + 'Kinestésico'
    else:
        resultado = resultado + 'ERROR'
        
    return resultado


def saveResults():

    gotoResultados()

    resultado = makeResults()
    with open('resultados_vak.txt', 'w') as archivo:
        archivo.write(resultado)
        archivo.close()
    return True


def getResultado():
    resultado = ''
    with open('resultados_vak.txt', 'r') as archivo:
        for linea in archivo:
            resultado = linea.upper()
        archivo.close()

    resultados_canvas.itemconfig(resultados_text, text=resultado)


def bringResultado():
    resultado = ''
    with open('resultados_vak.txt', 'r') as archivo:
        for linea in archivo:
            resultado = linea
        archivo.close()

    return resultado

#-----------------------------------------------#------------------------------------------#

# Variables que guardan la opción escogida para cada pregunta
selection1 = "no tengo valor asignado"
selection2 = "no tengo valor asignado"
selection3 = "no tengo valor asignado"
selection4 = "no tengo valor asignado"
selection5 = "no tengo valor asignado"
selection6 = "no tengo valor asignado"
selection7 = "no tengo valor asignado"
selection8 = "no tengo valor asignado"
selection9 = "no tengo valor asignado"
selection10 = "no tengo valor asignado"


# FUNCIONES POMODORO


def reset_timer():

    ventana.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_timer_state.config(text='Empieza tu Rutina de Estudios', fg=YELLOW)
    check_marks.config(text='')
    global reps
    reps = 0


def start_timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_timer_state.config(text='Muy bien! Descansa un rato :)', fg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_timer_state.config(text='Toma un pequeño descanso', fg=YELLOW)
    else:
        count_down(work_sec)
        title_timer_state.config(text='A trabajar!', fg=RED)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = ventana.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✓'
        check_marks.config(text=marks)


# FUNCIONES ESTILO VISUAL


def imageMC():
    ''' Función que muestra una imagen en especifico
        Entrada: Sin argumentos, solo necesita ser llamada
        Salida: Un boleano True
    '''
    # Etiqueta que muestra la imagen informatival del mapa conceptual
    imageMC2 = Image.open(ROUTEIMAGEMC1)
    imageMC2.show()

    return True


def imageFC():
    ''' Función que muestra una imagen en especifico
        Entrada: Solo necesita ser llamada
        Salida: Un boleano True'''

    # Etiqueta que muestra la imagen informativa de la flash card
    imageFC2 = Image.open(ROUTEIMAGEFC1)
    imageFC2.show()

    return True


def imageTL():
    ''' Función que muestra una imagen en especifico
        Entrada: Solo necesita ser llamada, no necesita argumentos
        Salida: Un boleano True
    '''

    # Etiqueta que muestra la imagen informativa de las lineas de tiempo
    imageTL2 = Image.open(ROUTEIMAGELT1)
    imageTL2.show()

    return True


def InfoVisual():
    ''' Función que entrega texto sobre personas visuales
        Entrada: Solo necesita ser llamada
        Salida: Un string
    '''

    text = "-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°\n\n \
            El Aprendizaje Visual se define como un método de enseñanza-aprendizaje que se caracteriza por manipular \n \
            conocimientos de forma visual ya sea con una serie de conjuntos de diagramas o gráficos usándolos para trabajar \n \
            con ideas y conceptos, que al utilizarlos ayudan a pensar y a aprender más efectivamente. \n\n \
            -°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°"

    return text


def WindowVisual():
    ''' Función que crea una pestaña con contenido Visual
        Entrada: Solo necesita ser llamanda
        Salida: Un boleano True
    '''
    # Crear una nueva pestaña
    newWindow = tk.Toplevel(frame4_Visual)
    newWindow.resizable(0,0)

    newWindow.title('¿Cómo es el aprendizaje visual?')
    newWindow.iconbitmap('gr8_logo_ico.ico')

    # Crear un frame para esa ventana
    frame = tk.Frame(newWindow)
    frame.config(width= "810", height= "500", bg = PINK)
    frame.pack()

    # Etiqueta de texto
    labelText = tk.Label(frame)
    labelText.config(text = InfoVisual(), bg= 'white', font = FONT_NAME)
    labelText.pack()

    return True


#FUNCIONES ESTILO AUDITIVO


def imageMS():
    ''' Función que muestra una imagen en especifico
        Entrada: Sin argumentos, solo necesita ser llamada
        Salida: Un boleano True
    '''
    # Etiqueta que muestra la imagen informatival de musica
    imageMS2 = Image.open(ROUTEIMAGEMS1)
    imageMS2.show()

    return True


def imagePC():
    ''' Función que muestra una imagen en especifico
        Entrada: Solo necesita ser llamada
        Salida: Un boleano True'''

    # Etiqueta que muestra la imagen informativa del podcast
    imagePC2 = Image.open(ROUTEIMAGEPC1)
    imagePC2.show()

    return True


def imageML():
    ''' Función que muestra una imagen en especifico
        Entrada: Solo necesita ser llamada, no necesita argumentos
        Salida: Un boleano True
    '''

    # Etiqueta que muestra la imagen informativa de monologo
    imageML2 = Image.open(ROUTEIMAGEML1)
    imageML2.show()

    return True


def InfoAudio():
    ''' Función que entrega texto sobre personas auditivas
        Entrada: Solo necesita ser llamada
        Salida: Un string
    '''

    text = "-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-\n\n\
            El Aprendizaje Auditivo es un método de enseñanza-aprendizaje cuyo estilo se orienta \n \
            más hacia la asimilación de información a través del oído, depende de escuchar y hablar \n \
            como maneras principales para su aprendizaje, las personas que son más auditivas tienden \n \
            a recordar mejor la información siguiendo y rememorando una explicación oral.\n\n\
            -°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-"

    return text


def WindowAudio():
    ''' Función que crea una pestaña con contenido Auditivo
        Entrada: Solo necesita ser llamanda
        Salida: Un boleano True
    '''
    # Crear una nueva pestaña
    newWindow = tk.Toplevel(frame5_Auditivo)
    newWindow.resizable(0,0)

    newWindow.title('¿Cómo es el aprendizaje auditivo?')
    newWindow.iconbitmap('gr8_logo_ico.ico')

    # Crear un frame para esa ventana
    frame = tk.Frame(newWindow)
    frame.config(width= "810", height= "500", bg = PINK)
    frame.pack()

    # Etiqueta de texto
    labelText = tk.Label(frame)
    labelText.config(text = InfoAudio(), bg= 'white', font = FONT_NAME)
    labelText.pack()

    return True

# FUNCIONES ESTILO KINE


def imagePR():
    ''' Función que muestra una imagen en especifico
        Entrada: Sin argumentos, solo necesita ser llamada
        Salida: Un boleano True
    '''
    # Etiqueta que muestra la imagen informatival 
    imagePR2 = Image.open(ROUTEIMAGEPR1)
    imagePR2.show()

    return True


def imageMI():
    ''' Función que muestra una imagen en especifico
        Entrada: Solo necesita ser llamada
        Salida: Un boleano True'''

    # Etiqueta que muestra la imagen informativa 
    imageMI2 = Image.open(ROUTEIMAGEMI1)
    imageMI2.show()

    return True


def imageDI():
    ''' Función que muestra una imagen en especifico
        Entrada: Solo necesita ser llamada, no necesita argumentos
        Salida: Un boleano True
    '''

    # Etiqueta que muestra la imagen informativa
    imageDI2 = Image.open(ROUTEIMAGEDI1)
    imageDI2.show()

    return True


def InfoKine():
    ''' Función que entrega texto sobre personas kinestesicas
        Entrada: Solo necesita ser llamada
        Salida: Un string
    '''

    text = "-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-\n\n\
            El Aprendizaje Kinestésico es uno de los estilos en qué se procesa la información a partir \n \
            del movimiento del cuerpo, sensaciones, y sentidos, el cuerpo es un medio por el cual podemos \n \
            apropiar y construir conocimiento.\n\n\
            -°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-"

    return text


def WindowKine():
    ''' Función que crea una pestaña con contenido Kinestesico
        Entrada: Solo necesita ser llamanda
        Salida: Un boleano True
    '''
    # Crear una nueva pestaña
    newWindow = tk.Toplevel(frame6_Kine)
    newWindow.resizable(0,0)

    newWindow.title('¿Cómo es el aprendizaje kinestésico?')
    newWindow.iconbitmap('gr8_logo_ico.ico')

    # Crear un frame para esa ventana
    frame = tk.Frame(newWindow)
    frame.config(width= "810", height= "500", bg = PINK)
    frame.pack()

    # Etiqueta de texto
    labelText = tk.Label(frame)
    labelText.config(text = InfoKine(), bg= 'white', font = FONT_NAME)
    labelText.pack()

    return True

# FUNCIONES DE TEXTO LARGO

def InfoPomodoro():

    ''' Función que muestra el texto informativo sobre el método pomodoro
        Entrada: Solo se necesita llamar a la función
        Salida: Un string con el texto a imprimir en la ventana
    '''
    infoTest = ('Los beneficios de la técnica Pomodoro provienen de los descansos frecuentes, que ayudan a \n'+
    'que tu mente se mantenga fresca. Los bloqueos de tiempo enfocados también te obligan a \n'+
    'cumplir con límites fijos, por lo que te animará a completar una tarea más rápidamente o, en el \n'+
    'caso de una tarea grande, extenderla en varios pomodoros.')

    return infoTest


def InfoPerfil():

    ''' Función que muestra el texto de bienvenida en el perfil
        Entrada: Solo se necesita llamar a la función
        Salida: Un string con el texto a imprimir en la ventana
    '''
    info = ('Con "Gr8 Study" conseguirás conocer cuál es tu estilo de aprendizaje \n'+
    'predominante entre los tipos: Visual, Auditivo o Kinestésico, gracias al Test VAK \n \n'+
    'Además podrás utilizar y conocer la "Estrategia Pomodoro", la que te ayudará con tu rutina de estudios \n \n'+
    'Por último en la pestaña "Métodos de estudio" podrás ver diferentes flashcards \n'+
    'con más estrategias para que logres encontrar las que más te acomoden')

    return info


# BLOQUE PRINCIPAL #

# CONSTANTES (aquí podemos definir colores para usar)

PINK= '#e2979c'
RED= '#ef233c'
GREEN = '#9bdeac'
YELLOW = '#FCA311'


PLATINUM = '#FEF9FF' #Platino
DARK_BLUE = '#4034EA'
MARINE_BLUE = '#736CED' #Azul marino
SOFT_RED = '#f4697d'
SOFT_GREEN = '#b5ec90'

TEXT_COLOR = '#29417A'
BG_COLOR = '#FEF9FF' #Platino #E5E5E5
FONT_NAME = 'Bahnschrift'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
ROOT_CENTER = 680

# imagen de mapa mental
ROUTEIMAGEMC = r"mapaConceptual1.png"
ROUTEIMAGEMC1 = r"mapaConceptual2.png"

# imagen de tarjetas de memoria
ROUTEIMAGEFC = r"flashCard1.png"
ROUTEIMAGEFC1 = r"flashCard2.png"

# imagen de lineas de tiempo
ROUTEIMAGELT = r"Timelines1.png"
ROUTEIMAGELT1 = r"Timelines2.png"

# imagen de musica
ROUTEIMAGEMS = r"musica1.png"
ROUTEIMAGEMS1 = r"musica2.png"

# imagen de podcast
ROUTEIMAGEPC = r"podcast1.png"
ROUTEIMAGEPC1 = r"podcast2.png"

# imagen de monologo
ROUTEIMAGEML = r"monologo1.png"
ROUTEIMAGEML1 = r"monologo2.png"

# imagen de practiva
ROUTEIMAGEPR = r"practica1.png"
ROUTEIMAGEPR1 = r"practica2.png"

# imagen de mimica
ROUTEIMAGEMI = r"mimica1.png"
ROUTEIMAGEMI1 = r"mimica2.png"

# imagen de dibujo
ROUTEIMAGEDI = r"dibujo1.png"
ROUTEIMAGEDI1 = r"dibujo2.png"

# PROCESAMIENTO #

# Inicia mainloop de la ventana
ventana = tk.Tk()
ventana.state('zoomed')
ventana.title('GR8 Study')
ventana.iconbitmap('gr8_logo_ico.ico')

# Asignacion de pestañas y frames
my_notebook = ttk.Notebook(ventana)
my_notebook.pack()

frame0_Perfil = Frame(my_notebook, width=1360, height=680, bg=PLATINUM) #my_frame1 -> frame1Perfil
frame1_VAK = Frame(my_notebook, width=1360, height=680, bg=PLATINUM) #my_frame2 -> frame2VAK
frame2_Pomodoro = Frame(my_notebook, width=1360, height=680, bg=PLATINUM)
frame3_Metodos = Frame(my_notebook, width=1360, height=680, bg=PLATINUM)
frame4_Visual = Frame(my_notebook, width=1360, height=680, bg=PLATINUM)
frame5_Auditivo = Frame(my_notebook, width=1360, height=680, bg=PLATINUM)
frame6_Kine = Frame(my_notebook, width=1360, height=680, bg=PLATINUM)
frame7_Resultados = Frame(my_notebook, width=1360, height=680, bg=PLATINUM)

frame0_Perfil.pack(fill='both', expand=1)
frame1_VAK.pack(fill='both', expand=1)
frame2_Pomodoro.pack(fill='both', expand=1)
frame3_Metodos.pack(fill='both', expand=1)
frame4_Visual.pack(fill='both', expand=1)
frame5_Auditivo.pack(fill='both', expand=1)
frame6_Kine.pack(fill='both', expand=1)
frame7_Resultados.pack(fill='both', expand=1)

my_notebook.add(frame0_Perfil, text='Inicio')
my_notebook.add(frame1_VAK, text='Test de Vak')
my_notebook.add(frame2_Pomodoro, text='Pomodoro')
my_notebook.add(frame3_Metodos, text='Métodos de Estudio')
my_notebook.add(frame4_Visual, text='Estilo Visual')
my_notebook.add(frame5_Auditivo, text='Estilo Auditivo')
my_notebook.add(frame6_Kine, text='Estilo Kinestésico')
my_notebook.add(frame7_Resultados, text='Resultados VAK')

hide_tabs()

# UI SETUP


###---------------------UI TAB: PERFIL-------------------###

image_inicio = ImageTk.PhotoImage(Image.open('inicio_design.jpg'))
label_image_inicio = tk.Label(frame0_Perfil, image= image_inicio)
label_image_inicio.place( x = ROOT_CENTER, y = 345, anchor='center')

# BOTONES (frame0_Perfil)
perfil_to_vak_Button = tk.Button(frame0_Perfil, text='Ir a Test VAK',  width=14,
 highlightthickness=1, fg=PLATINUM, bg=MARINE_BLUE, font=(FONT_NAME, 16), command=gotoVAK) #.pack(pady=15)
perfil_to_vak_Button.place(x=ROOT_CENTER-300, y=580, anchor='e')

perfil_to_pom_Button = tk.Button(frame0_Perfil, text='Ir a Pomodoro',  width=14,
 highlightthickness=1, fg=PLATINUM, bg=MARINE_BLUE, font=(FONT_NAME, 16), command=gotoPom) #.pack(pady=15)
perfil_to_pom_Button.place(x=ROOT_CENTER, y=580, anchor='w')

### -------------------------------------------------- ###



###-------------------UI TAB: TEST DE VAK-----------------###

scroll = tk.Scrollbar(frame1_VAK)
canvasScroll = tk.Canvas(frame1_VAK, background= RED, yscrollcommand= scroll.set)
scroll.config(command=canvasScroll.yview)
scroll.pack(side= tk.RIGHT, fill= tk.Y)
frameVak = tk.Frame(canvasScroll)
frameVak.config(bg= PLATINUM)
canvasScroll.pack(side= "left", fill= "both", expand= True)
canvasScroll.create_window((0,0), window= frameVak, anchor= "nw")

#---------------------------Crear contenido del frame-------------------------------------#

# Etiqueta de titulo
labelVakTitle = tk.Label(frameVak)
labelVakTitle.config(text= "TEST DE VAK", fg= PLATINUM, bg= MARINE_BLUE, font=(FONT_NAME, 22, 'bold'))
labelVakTitle.pack(fill= tk.X, pady=15)

# Frame para colocar información sobre el test de VAK
frameInfoVak = tk.Frame(frame1_VAK) #frame1
frameInfoVak.config(width= 826, height= 900, bg=PLATINUM)
frameInfoVak.pack(fill= tk.X)

#------------------------------- Información del frameInfoVak-------------------------------------#

# Etiqueta titulo2 
labelInfoVakTitle = tk.Label(frameInfoVak)
labelInfoVakTitle.config(text= "¿Qué es el test de VAK?", width=100, 
                         fg= PLATINUM, bg= MARINE_BLUE, font=(FONT_NAME, 22, 'bold'))
labelInfoVakTitle.place(x= 400, y= 35, anchor='center')

# Etiqueta con información del test de VAK
labelInfoVakText = tk.Label(frameInfoVak)
labelInfoVakText.config(text=infoVak(), fg=MARINE_BLUE, bg= PLATINUM, font=(FONT_NAME, 12))
labelInfoVakText.place(x= 400, y = 140, anchor='center')

# Etiqueta para agregar imagen EA de estilos de aprendizaje
imageEA = ImageTk.PhotoImage(Image.open('EA.jpeg.jpeg'))
labelImageEA = tk.Label(frame1_VAK, image= imageEA)
labelImageEA.place(x= 750, y= 260)

#------------------------------- Preguntas del test--------------------------------------#

# Etiqueta para la primera pregunta
labelVakQuestion1 = tk.Label(frameVak)
labelVakQuestion1.config(text="1. ¿Cuál de las siguientes actividades disfrutas más?", 
                         fg=MARINE_BLUE, bg= PLATINUM, font= FONT_NAME)
labelVakQuestion1.pack()

# Opciones pregunta 1
Question1 = tk.IntVar()

rbnA1 = tk.Radiobutton(frameVak, text="A: Escuchar música", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question1, value=1, 
                     command= ShowAnswer).pack()

rbnB1 = tk.Radiobutton(frameVak, text="B: Ver películas", fg=DARK_BLUE, 
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question1, value=2, 
                     command= ShowAnswer).pack()

rbnC1 = tk.Radiobutton(frameVak, text="C: Bailar con buena música", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question1, value=3, 
                     command= ShowAnswer).pack()

#-----------------------------------------------#------------------------------------------#

# Etiqueta para la segunda pregunta
labelVakQuestion2 = tk.Label(frameVak)
labelVakQuestion2.config(text="\n 2. ¿Qué programa de televisión prefieres?",
                         fg= MARINE_BLUE, bg= PLATINUM, font= FONT_NAME)
labelVakQuestion2.pack(fill= tk.X)

# Opciones pregunta 2
Question2 = tk.IntVar()

rbnA2 = tk.Radiobutton(frameVak, text="A: Reportajes de descubrimientos y lugares",
                     fg=DARK_BLUE, bg= PLATINUM, font=(FONT_NAME, 10), variable= Question2, value=1, 
                     command= ShowAnswer).pack()

rbnB2 = tk.Radiobutton(frameVak, text="B: Cómico y de entretenimiento",
                     fg=DARK_BLUE, bg= PLATINUM, font=(FONT_NAME, 10), variable= Question2, value=2, 
                     command= ShowAnswer).pack()

rbnC2 = tk.Radiobutton(frameVak, text="C: Noticias del mundo",
                     fg=DARK_BLUE, bg= PLATINUM, font=(FONT_NAME, 10), variable= Question2, value=3, 
                     command= ShowAnswer).pack()

#-----------------------------------------------#------------------------------------------#

# Etiqueta para la tercera pregunta
labelVakQuestion3 = tk.Label(frameVak)
labelVakQuestion3.config(text="\n 3. Cuando conversas con otra persona, tú:",
                         fg=MARINE_BLUE, bg=PLATINUM, font= FONT_NAME)
labelVakQuestion3.pack()

# Opciones pregunta 3
Question3 = tk.IntVar()

rbnA3 = tk.Radiobutton(frameVak, text="A: La escuchas atentamente",
                     fg=DARK_BLUE, bg= PLATINUM, font=(FONT_NAME, 10), variable= Question3, value=1, 
                     command= ShowAnswer).pack()

rbnB3 = tk.Radiobutton(frameVak, text="B: La observas",
                     fg=DARK_BLUE, bg= PLATINUM, font=(FONT_NAME, 10), variable= Question3, value=2, 
                     command= ShowAnswer).pack()

rbnC3 = tk.Radiobutton(frameVak, text="C: Tiendes a tocarla",
                     fg=DARK_BLUE, bg= PLATINUM, font=(FONT_NAME, 10), variable= Question3, value=3, 
                     command= ShowAnswer).pack()

#-----------------------------------------------#------------------------------------------#

# Etiqueta para la cuarta pregunta
labelVakQuestion4 = tk.Label(frameVak)
labelVakQuestion4.config(text="\n 4. Si pudieras adquirir uno de los siguientes artículos, ¿cuál elegirías?",
                         fg= MARINE_BLUE, bg=PLATINUM, font= FONT_NAME)
labelVakQuestion4.pack()

# Opciones pregunta 4
Question4 = tk.IntVar()

rbnA4 = tk.Radiobutton(frameVak, text="A: Un jacuzzi", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question4, value=1, 
                     command= ShowAnswer).pack()

rbnB4 = tk.Radiobutton(frameVak, text="B: Un estéreo", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question4, value=2, 
                     command= ShowAnswer).pack()

rbnC4 = tk.Radiobutton(frameVak, text="C: Un televisor", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question4, value=3, 
                     command= ShowAnswer).pack()

#-----------------------------------------------#------------------------------------------#

# Etiqueta para la quinta pregunta
labelVakQuestion5 = tk.Label(frameVak)
labelVakQuestion5.config(text="\n 5. ¿Qué prefieres hacer un sábado por la tarde?", 
                         fg= MARINE_BLUE, bg= PLATINUM, font= FONT_NAME)
labelVakQuestion5.pack()

# Opciones pregunta 5
Question5 = tk.IntVar()

rbnA5 = tk.Radiobutton(frameVak, text="A: Quedarte en casa", fg=DARK_BLUE,
                     bg=PLATINUM, font=(FONT_NAME, 10), variable= Question5, value=1, 
                     command= ShowAnswer).pack()

rbnB5 = tk.Radiobutton(frameVak, text="B: Ir a un concierto", fg=DARK_BLUE,
                     bg=PLATINUM, font=(FONT_NAME, 10), variable= Question5, value=2, 
                     command= ShowAnswer).pack()

rbnC5 = tk.Radiobutton(frameVak, text="C: Ir al cine", fg=DARK_BLUE,
                     bg=PLATINUM, font=(FONT_NAME, 10), variable= Question5, value=3, 
                     command= ShowAnswer).pack()

#-----------------------------------------------#------------------------------------------#

# Etiqueta para la sexta pregunta
labelVakQuestion6 = tk.Label(frameVak)
labelVakQuestion6.config(text="\n 6. ¿Qué tipo de exámenes se te facilitan más?",
                         fg=MARINE_BLUE, bg=PLATINUM, font= FONT_NAME)
labelVakQuestion6.pack()

# Opciones pregunta 6
Question6 = tk.IntVar()

rbnA6 = tk.Radiobutton(frameVak, text="A: Examen oral", fg=DARK_BLUE,
                         bg= PLATINUM, font=(FONT_NAME, 10), variable= Question6, value=1, 
                         command= ShowAnswer).pack()

rbnB6 = tk.Radiobutton(frameVak, text="B: Examen escrito", fg=DARK_BLUE,
                         bg= PLATINUM, font=(FONT_NAME, 10), variable= Question6, value=2, 
                         command= ShowAnswer).pack()

rbnC6 = tk.Radiobutton(frameVak, text="C: Examen de opción múltiple", fg=DARK_BLUE,
                         bg= PLATINUM, font=(FONT_NAME, 10), variable= Question6, value=3, 
                         command= ShowAnswer).pack()

#-----------------------------------------------#------------------------------------------#

# Etiqueta para la septima pregunta
labelVakQuestion7 = tk.Label(frameVak)
labelVakQuestion7.config(text="\n 7. ¿Cómo te orientas más fácilmente?",
                         fg=MARINE_BLUE, bg=PLATINUM, font= FONT_NAME)
labelVakQuestion7.pack()

# Opciones pregunta 7
Question7 = tk.IntVar()

rbnA7 = tk.Radiobutton(frameVak, text="A: Mediante el uso de un mapa", fg=DARK_BLUE,
                         bg= PLATINUM, font=(FONT_NAME, 10), variable= Question7, value=1, 
                         command= ShowAnswer).pack()

rbnB7 = tk.Radiobutton(frameVak, text="B: Pidiendo Indicaciones", fg=DARK_BLUE,
                         bg= PLATINUM, font=(FONT_NAME, 10), variable= Question7, value=2, 
                         command= ShowAnswer).pack()

rbnC7 = tk.Radiobutton(frameVak, text="C: A través de la intuición", fg=DARK_BLUE,
                         bg= PLATINUM, font=(FONT_NAME, 10), variable= Question7, value=3, 
                         command= ShowAnswer).pack()

#-----------------------------------------------#------------------------------------------#

# Etiqueta para la octava pregunta
labelVakQuestion8 = tk.Label(frameVak)
labelVakQuestion8.config(text="\n 8. ¿En qué prefieres ocupar tu tiempo en un lugar de descanso?",
                         fg=MARINE_BLUE, bg=PLATINUM, font= FONT_NAME)
labelVakQuestion8.pack()

# Opciones pregunta 8
Question8 = tk.IntVar()

rbnA8 = tk.Radiobutton(frameVak, text="A: Pensar", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question8, value=1, 
                     command= ShowAnswer).pack()

rbnB8 = tk.Radiobutton(frameVak, text="B: Caminar por los alrededores", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question8, value=2, 
                     command= ShowAnswer).pack()

rbnC8 = tk.Radiobutton(frameVak, text="C: Descansar", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question8, value=3, 
                     command= ShowAnswer).pack()

#-----------------------------------------------#------------------------------------------#

# Etiqueta para la novena pregunta
labelVakQuestion9 = tk.Label(frameVak)
labelVakQuestion9.config(text="\n 9. ¿Qué te halaga más?",
                         fg=MARINE_BLUE, bg=PLATINUM, font= FONT_NAME)
labelVakQuestion9.pack()

# Opciones pregunta 9
Question9 = tk.IntVar()

rbnA9 = tk.Radiobutton(frameVak, text="A: Que te digan que tienes buen aspecto", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question9, value=1, 
                     command= ShowAnswer).pack()

rbnB9 = tk.Radiobutton(frameVak, text="B: Que te digan que tienes un trato muy agradable", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question9, value=2, 
                     command= ShowAnswer).pack()

rbnC9 = tk.Radiobutton(frameVak, text="C: Que te digan que tienes una conversación interesante", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question9, value=3, 
                     command= ShowAnswer).pack()

#-----------------------------------------------#------------------------------------------#

# Etiqueta para la decima pregunta
labelVakQuestion10 = tk.Label(frameVak)
labelVakQuestion10.config(text="\n 10. ¿Cuál de estos ambientes te atrae más?",
                         fg=MARINE_BLUE, bg=PLATINUM, font= FONT_NAME)
labelVakQuestion10.pack()

# Opciones pregunta 10
Question10 = tk.IntVar()

rbnA10 = tk.Radiobutton(frameVak, text="A: Uno en el que se sienta un clima agradable", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question10, value=1, 
                     command= ShowAnswer).pack()

rbnB10 = tk.Radiobutton(frameVak, text="B: Uno en el que se escuchen las olas del mar", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question10, value=2, 
                     command= ShowAnswer).pack()

rbnC10 = tk.Radiobutton(frameVak, text="C: Uno con una hermosa vista al oceano", fg=DARK_BLUE,
                     bg= PLATINUM, font=(FONT_NAME, 10), variable= Question10, value=3, 
                     command= ShowAnswer).pack()

# Etiqueta para crear un espacio
labelSpace = tk.Label(frameVak)
labelSpace.config(text="\n" * 2)
labelSpace.pack()

#------------------------------------- Terminadas las preguntas, se configura el botón -----------------------------------#

buttonVak = tk.Button(frameInfoVak, text= "Presione aquí una vez terminado el test", command= saveResults)
buttonVak.config(fg=PLATINUM, bg= MARINE_BLUE, font= (FONT_NAME, 16, 'bold'))
buttonVak.place(relwidth= 0.5, relheight= 0.1, x= 200, y= 500)

# Actualiza el scroll

ventana.update()
canvasScroll.config(scrollregion= canvasScroll.bbox("all"))


### -------------------------------------------------- ###



###-------------------UI TAB: POMODORO-----------------###

#TITULO Y DESC DE POMODORO

image_pom_right = ImageTk.PhotoImage(Image.open('pomodoro_design.jpg'))
label_pom_right = tk.Label(frame2_Pomodoro, image= image_pom_right)
label_pom_right.place( x = ROOT_CENTER, y = 345, anchor='center')

# TITULO DINAMICO
title_timer_state = tk.Label(frame2_Pomodoro, text='Empieza tu Rutina de Estudios',
                             fg=YELLOW, bg=PLATINUM, font=(FONT_NAME, 18, 'bold'))
title_timer_state.place(x=ROOT_CENTER, y=300, anchor='center')

# TIMER POMODORO

canvas = tk.Canvas(frame2_Pomodoro, width=190, height=70, bg=SOFT_RED, highlightthickness=0)
timer_text = canvas.create_text(95, 32, text='00:00', fill=PLATINUM, font=(FONT_NAME, 48, 'bold'))
canvas.place(x=ROOT_CENTER, y=380, anchor='center')

# BOTONES (Frame2_Pomodoro) 

start_button = tk.Button(frame2_Pomodoro, text='Comenzar', width=8, highlightthickness=1,
                         fg=PLATINUM, bg=SOFT_GREEN, font=(FONT_NAME, 16), command=start_timer)
start_button.place(x=ROOT_CENTER-25, y=570, anchor='e')

reset_button = tk.Button(frame2_Pomodoro, text='Resetear', width=8, highlightthickness=1,
                         fg=PLATINUM, bg=SOFT_RED, font=(FONT_NAME, 16), command=reset_timer)
reset_button.place(x=ROOT_CENTER+25, y=570, anchor='w')

# CHECKMARKS (Frame2_Pomodoro) 

title_checkmarks = tk.Label(frame2_Pomodoro, text='Contador de Pomodoros:',
                             fg=SOFT_RED, bg=BG_COLOR, font=(FONT_NAME, 12))
title_checkmarks.place(x=ROOT_CENTER, y=460, anchor='center')

check_marks = tk.Label(frame2_Pomodoro, fg=SOFT_RED, bg=BG_COLOR)
check_marks.place(x=ROOT_CENTER, y=490, anchor='center')



### -------------------------------------------------- ###

###--------------UI TAB: MÉTODOS DE ESTUDIO------------###

title_metodos = tk.Label(frame3_Metodos, text='Métodos de Estudio', width=100,
                     fg=PLATINUM, bg=MARINE_BLUE, font=(FONT_NAME, 40, 'bold')) #bold 
title_metodos.place(x=ROOT_CENTER, y=50, anchor='center')

#Visual Auditory Kinesthetic.jpg
main_image = Image.open('Visual Auditory Kinesthetic.jpg')
resized_image = main_image.resize((929,438), Image.ANTIALIAS)
main_resized_image = ImageTk.PhotoImage(resized_image)
label_main_image = tk.Label(frame3_Metodos, image= main_resized_image)
label_main_image.place( x = ROOT_CENTER, y = 345, anchor='center')

image_metodos = ImageTk.PhotoImage(Image.open('metodos_design.jpg'))
label_image_metodos = tk.Label(frame3_Metodos, image= image_metodos)
label_image_metodos.place( x = ROOT_CENTER, y = 345, anchor='center')

#Botones para ir a métodos
goto_visualbt = tk.Button(frame3_Metodos, text='Visual', width=8, highlightthickness=1,
 bg = PINK, fg=PLATINUM, font = (FONT_NAME,20), command= gotoVisual)
goto_visualbt.place(x = ROOT_CENTER-315, y = 480, anchor='center')

goto_auditivobt = tk.Button(frame3_Metodos, text='Auditivo', width=8, highlightthickness=1,
 bg = PINK, fg=PLATINUM, font = (FONT_NAME,20), command= gotoAuditivo)
goto_auditivobt.place(x = ROOT_CENTER, y = 480, anchor='center')

goto_kinebt = tk.Button(frame3_Metodos, text='Kinestésico', width=9, highlightthickness=1,
 bg = PINK, fg=PLATINUM, font = (FONT_NAME,20), command= gotoKine)
goto_kinebt.place(x = ROOT_CENTER+300, y = 480, anchor='center')

### -------------------------------------------------- ###


###-----------------UI TAB: ESTILO VISUAL--------------###

# Etiqueta para titulo
title_visual = tk.Label(frame4_Visual, text = "Metodos de estudio Visual",
 bg= PINK, fg = 'white', font = (FONT_NAME,20))
title_visual.pack(fill = tk.X)

#---------------------------------------- primer método ------------------------------------------------------#

# Crear una imagen de mapa conceptual
imageMC1 = ImageTk.PhotoImage(Image.open(ROUTEIMAGEMC))
labelImageMC = tk.Label(frame4_Visual, image= imageMC1)
labelImageMC.place(x = ROOT_CENTER-430, y = 345, anchor='center')

# Botón del mapa conceptual
buttonMC = tk.Button(frame4_Visual, text="Más Información",
 bg = RED, fg= "white", font = FONT_NAME, command= imageMC)
buttonMC.place(x = ROOT_CENTER-430, y = 560, anchor='center')

#---------------------------------------- segundo método -----------------------------------------------------#

# Crear una imagen para flash card
imageFC1 = ImageTk.PhotoImage(Image.open(ROUTEIMAGEFC))
labelImageFC = tk.Label(frame4_Visual, image = imageFC1)
labelImageFC.place(x = ROOT_CENTER, y = 345, anchor='center')

# Botón de flash card
buttonFC = tk.Button(frame4_Visual, text= "Más información",
 bg = "blue", fg = 'white', font= FONT_NAME, command= imageFC)
buttonFC.place(x = ROOT_CENTER, y = 560, anchor='center')

#---------------------------------------- tercer método -----------------------------------------------------#

# Crear una imagen de lineas de tiempo
imageLT1 = ImageTk.PhotoImage(Image.open(ROUTEIMAGELT))
labelImageLT = tk.Label(frame4_Visual, image= imageLT1)
labelImageLT.place(x = ROOT_CENTER+430, y = 345, anchor='center')

# Botón de linea de tiempo
buttonLT = tk.Button(frame4_Visual, text="Más Información",
 bg = "green", fg= "white", font = FONT_NAME, command= imageTL)
buttonLT.place(x = ROOT_CENTER+430, y = 560, anchor='center')

#------------------------------------------ botón varios -------------------------------------------------#

# Botón de regreso

visual_to_metodos_Button = tk.Button(frame4_Visual, text='REGRESAR', width=10,
 highlightthickness=1, fg='white', bg=PINK, font=(FONT_NAME,16), command=gotoMetodos)
visual_to_metodos_Button.place(x = ROOT_CENTER, y = 64, anchor='center')

# Botón que abre la pestaña de Visual
info_visual_button = tk.Button(frame4_Visual, text = "¿Como es el aprendizaje visual?",
 bg = PINK, fg = "white", font = (FONT_NAME,18), command= WindowVisual)
info_visual_button.place(x = ROOT_CENTER, y = 630, anchor='center')


### -------------------------------------------------- ###

###----------------UI TAB: ESTILO AUDITIVO-------------###

# Etiqueta de titulo
title_auditivo = tk.Label(frame5_Auditivo, text = "Metodos de estudio Auditivos", 
 bg= PINK, fg = 'white', font = (FONT_NAME,20))
title_auditivo.pack(fill = tk.X)

#---------------------------------------- primer método ------------------------------------------------------#

# Crear una imagen de musica
imageMS1 = ImageTk.PhotoImage(Image.open(ROUTEIMAGEMS))
labelImageMS = tk.Label(frame5_Auditivo, image= imageMS1)
labelImageMS.place(x = ROOT_CENTER-430, y = 345, anchor='center')

# Botón del musica
buttonMS = tk.Button(frame5_Auditivo, text="Más Información",
 bg = RED, fg= "white", font = FONT_NAME, command= imageMS)
buttonMS.place(x = ROOT_CENTER-430, y = 560, anchor='center')

#---------------------------------------- segundo método -----------------------------------------------------#

# Crear una imagen para podcast
imagePC1 = ImageTk.PhotoImage(Image.open(ROUTEIMAGEPC))
labelImagePC = tk.Label(frame5_Auditivo, image = imagePC1)
labelImagePC.place(x = ROOT_CENTER, y = 345, anchor='center')

# Botón de podcast
buttonPC = tk.Button(frame5_Auditivo, text= "Más información",
 bg = "red", fg = 'white', font= FONT_NAME, command= imagePC)
buttonPC.place(x = ROOT_CENTER, y = 560, anchor='center')

#---------------------------------------- tercer método -----------------------------------------------------#

# Crear una imagen de monólogo
imageML1 = ImageTk.PhotoImage(Image.open(ROUTEIMAGEML))
labelImageML = tk.Label(frame5_Auditivo, image= imageML1)
labelImageML.place(x = ROOT_CENTER+430, y = 345, anchor='center')

# Botón de monólogo
buttonML = tk.Button(frame5_Auditivo, text="Más Información",
 bg = "blue", fg= "white", font = FONT_NAME, command= imageML)
buttonML.place(x = ROOT_CENTER+430, y = 560, anchor='center')

#------------------------------------------ botón varios -------------------------------------------------#

# Botón de regreso
auditivo_to_metodos_Button = tk.Button(frame5_Auditivo, text='REGRESAR', width=10,
 highlightthickness=1, fg='white', bg=PINK, font=(FONT_NAME,16), command=gotoMetodos)
auditivo_to_metodos_Button.place(x = ROOT_CENTER, y = 64, anchor='center')

# Botón que abre la pestaña de Auditivo
info_auditivo_button = tk.Button(frame5_Auditivo, text = "¿Como es el aprendizaje auditivo?", 
 bg = PINK, fg = "white", font = (FONT_NAME, 18), command= WindowAudio)
info_auditivo_button.place(x = ROOT_CENTER, y = 630, anchor='center')

### -------------------------------------------------- ###

###-----------------UI TAB: ESTILO KINE----------------###

# Etiqueta de titulo
title_kine = tk.Label(frame6_Kine, text = "Metodos de estudio Kinestesicos",
 bg= PINK, fg = 'white', font = (FONT_NAME, 20))
title_kine.pack(fill = tk.X)

#---------------------------------------- primer método ------------------------------------------------------#

# Crear una imagen de práctica
imagePR1 = ImageTk.PhotoImage(Image.open(ROUTEIMAGEPR))
labelImagePR = tk.Label(frame6_Kine, image= imagePR1)
labelImagePR.place(x = ROOT_CENTER-430, y = 345, anchor='center')

# Botón de práctica
buttonPR = tk.Button(frame6_Kine, text="Más Información",bg = RED, fg= "white", font = FONT_NAME, command= imagePR)
buttonPR.place(x = ROOT_CENTER-430, y = 560, anchor='center')

#---------------------------------------- segundo método -----------------------------------------------------#

# Crear una imagen para mimica
imageMI1 = ImageTk.PhotoImage(Image.open(ROUTEIMAGEMI))
labelImageMI = tk.Label(frame6_Kine, image = imageMI1)
labelImageMI.place(x = ROOT_CENTER, y = 345, anchor='center')

# Botón de mimica
buttonMI = tk.Button(frame6_Kine, text= "Más información",
 bg = "red", fg = "white", font= FONT_NAME, command= imageMI)
buttonMI.place(x = ROOT_CENTER, y = 560, anchor='center')

#---------------------------------------- tercer método -----------------------------------------------------#

# Crear una imagen de dibujo
imageDI1 = ImageTk.PhotoImage(Image.open(ROUTEIMAGEDI))
labelImageDI = tk.Label(frame6_Kine, image= imageDI1)
labelImageDI.place(x = ROOT_CENTER+430, y = 345, anchor='center')

# Botón de dibujo
buttonDI = tk.Button(frame6_Kine, text="Más Información",
 bg = RED, fg= "white", font = FONT_NAME, command= imageDI)
buttonDI.place(x = ROOT_CENTER+430, y = 560, anchor='center')

#------------------------------------------ botón varios -------------------------------------------------#

# Botón de regreso
button = tk.Button(frame6_Kine, text= "REGRESAR", width=10, highlightthickness=1,
 fg='white', bg=PINK, font=(FONT_NAME,16), command=gotoMetodos)
button.place(x = ROOT_CENTER, y = 64, anchor='center')

# Botón que abre la pestaña de Kinestesico
buttonK = tk.Button(frame6_Kine, text = "¿Como es el aprendizaje kinestesico?",
 bg = PINK, fg = "white", font = (FONT_NAME,18), command= WindowKine)
buttonK.place(x = ROOT_CENTER, y = 630, anchor='center')

### -------------------------------------------------- ###

###----------------UI TAB: RESULTADOS VAK--------------###

fondo_resultados = ImageTk.PhotoImage(Image.open('background.jpg'))
label_fondo_resultados = tk.Label(frame7_Resultados, image= fondo_resultados)
label_fondo_resultados.place( x = ROOT_CENTER, y = 345, anchor='center')

#TITULO RESULTADOS VAK

title_resultados = tk.Label(frame7_Resultados, text='Resultados Test VAK', width=100,
                         fg=PLATINUM, bg=MARINE_BLUE, font=(FONT_NAME, 40, 'bold')) #bold 
title_resultados.place(x=ROOT_CENTER, y=50, anchor='center')

resultados_label = tk.Label(frame7_Resultados, text='Tu estilo de aprendizaje es:', width=25,
                         fg=MARINE_BLUE, bg=PLATINUM, font=(FONT_NAME, 26)) #bold 
resultados_label.place(x=ROOT_CENTER, y=210, anchor='center')

resultados_canvas = tk.Canvas(frame7_Resultados, width=600, height=70, bg=MARINE_BLUE)
resultados_text = resultados_canvas.create_text(300, 35, text=bringResultado(), 
                             fill=YELLOW, font=(FONT_NAME, 22, 'bold'))
resultados_canvas.place(x=ROOT_CENTER, y=310, anchor='center') 

resultados_button = tk.Button(frame7_Resultados, text='Conocer Mi Resultado',
 bg=MARINE_BLUE, fg=PLATINUM, font = (FONT_NAME, 16), command=getResultado)
resultados_button.place(x=ROOT_CENTER, y=410, anchor='center')

t_resultados1 = 'Descubre metodos de estudio\npara tu estilo de aprendizaje:'

text_resultados1 = tk.Label(frame7_Resultados, text=t_resultados1, width=25,
                         fg=MARINE_BLUE, bg=PLATINUM, font=(FONT_NAME, 14)) #bold 
text_resultados1.place(x=ROOT_CENTER, y=500, anchor='center')

gotometodos_button = tk.Button(frame7_Resultados, text='ir a métodos de estudio',
 bg=MARINE_BLUE, fg=PLATINUM, font = (FONT_NAME, 14), command=gotoMetodos)
gotometodos_button.place(x=ROOT_CENTER, y=560, anchor='center')

### -------------------------------------------------- ###

ventana.mainloop()
