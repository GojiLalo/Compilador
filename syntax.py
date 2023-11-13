import lexer
import re

lineas = lexer.llamarLexer("ExpresionesMat.txt")
#Definicion de atajos para reducir expresiones regulares
TIPO = "char|int|short|long(long|double)?|float|double|bool|string|void|string"
TIPNUM = "(DEC|ENT)"
OPMATS = "(DIVISION|MULTIPLICACION|MENOS|MAS|MODULO|PORCENTAJE)"
EXPMAT = ""
FUNC = "IDIZQPAR(ID(COMAID)*?)?DERPAR(PUNTOCOMA)?"

#Definicion de expresiones regulares para comprobar si una linea es correcta
expRegL = [
    (r'(^ $)'), #Lineas vacias
    (r'(^GATOIDMENORQUE(PR|ID|string)(PUNTOID)?MAYORQUE$)'), #Librerias
    (r'(^usingnamespaceIDPUNTOCOMA$)'), #Using namespace
    (r'(^intmainIZQPARDERPARIZQLLAVE$)'), #Declaracion de main
    (r'(^DERLLAVE$)|(^IZQLLAVE$)'), #Llaves
    (r'(^{}IDIZQPAR({}ID(COMA{}ID)*)?DERPAR(IZQLLAVE)?$)'.format(TIPO, TIPO, TIPO)), #Definicion de funciones
    (r'(^IDIZQPAR(ID(COMAID)*?)?DERPAR(PUNTOCOMA)?$)'),#Llamada a funciones
    (r'(^COMENTARIO$)'), #Comentarios de una linea
    (r'(^(IDDOSPUNTOSDOSPUNTOS)?cout(MENORQUE){2}(ID|(COMILLAS(\w)*COMILLAS))((MENORQUE){2}(ID|(COMILLAS(\w)*COMILLAS)))*(DOSPUNTOSDOSPUNTOSID)?PUNTOCOMA$)'), #cout
    (r'(^cin(MAYORQUE){2}IDPUNTOCOMA$)'), #cin
    (r'(^cout(MENORQUE){2}(CADENA|ID|endl)((MENORQUE){2}(CADENA|ID|endl))*PUNTOCOMA$)'), # COUT
    (r'(^(if|while)IZQPARID((NOT)?(IGUAL)|((MENOR|MAYOR)QUE)(IGUAL)?)ENTDERPAR(IZQLLAVE)?$)'), #Inicio de una estructuras IF, WHILE
    (r'(^(DERLLAVE)?(else|elseif)(IZQLLAVE)?$)'), #Else, else if
    (r'(switchIZQPARIDDERPAR(IZQLLAVE)?)'), #Inicio de un estructura CASE
    (r'(^(caseENT|default)DOSPUNTOS|$)'), #Seleccion de opciones en estructura case
    (r'(^doIZQLLAVE$)'), #Inicio de estructura DO-WHILE
    (r'(^DERLLAVEwhileIZQPARID((NOT)?IGUAL|(MENOR|MAYOR)QUE(IGUAL)?)ENTDERPARPUNTOCOMA$)'), #Fin de estructura DO-WHILE
    (r'(^(DERLLAVE)?whileIZQPARID(((NOT)|(IGUAL))?(IGUAL)|((MENOR|MAYOR)QUE)(IGUAL)?)DIGITODERPARPUNTOCOMA$)'), #Final estructura do-while
    (r'(^breakPUNTOCOMA$)'), #Break
    (r'(^ID(MAS){2}PUNTOCOMA$)'), #Aumento de variables
    (r'(^forIZQPARintID((IGUAL)|((MENOR|MAYOR)QUE)(IGUAL)?)ENTPUNTOCOMAID((IGUAL)|((MENOR|MAYOR)QUE)(IGUAL)?)ENTPUNTOCOMAID(MASMAS|MENOSMENOS)DERPAR(IZQLLAVE)?$)'), #Ciclo for
    (r'(^IDDOSPUNTOS$)'), #Etiquetas,
    (r'(^gotoIDPUNTOCOMA$)'), #Estructura GOTO
    (r'(^returnENTPUNTOCOMA$)'), #Retornos

    #EXPRESIONES REGULARES PARA ASIGNACIONES DE VARIABLES#
    (r'(^(char|wchar_t)ID(IGUALCAR)?(COMAID(IGUALCAR)?)*PUNTOCOMA$)'), #Asignaciones para char y w_char
    
    #EXPRESIONES REGULARES PARA EXPRESIONES MATEMATICAS
    (r'((MENOS)?{})'.format(TIPNUM))
]

#Definicion de la clase compLinea
class enumLinea:
    def __init__(self, numLinea, linea):
        self.numLinea = numLinea
        self.linea = linea
        self.estado = False
        self.comprobarLinea()

    def comprobarLinea(self):
        for exp in expRegL:
            if re.match(exp, self.linea):
                self.estado = True

    def __repr__(self):
        if self.estado:
            s = "correcta"
        else:
            s = "incorrecta"
        return f'{"Linea #" + str(self.numLinea) + " es " + s}'

#Convertir arreglo a linea
def convArLin(arregloLineas):
    linea = ''
    for i in arregloLineas:
        linea = linea + str(i)
    return linea

def numerarLineas(lineasTexto):
    listaLineas = []
    n = 1
    for i in lineasTexto:
        lineaPlana = convArLin(i)
        listaLineas.append((enumLinea(n, lineaPlana)))
        n = n + 1
    return listaLineas

def imprimirLineas(arregloLineas):
    for i in arregloLineas:
        print(i)


llEstado = numerarLineas(lineas)
imprimirLineas(llEstado)