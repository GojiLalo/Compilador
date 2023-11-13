import re

operadores = ['+', '-', '*', '/', '%', '>', '<', '!', '&', '|', '^', '~', '(', ')', '{', '}', '[', ']', ';', ',', '.', ':', '#', '"', '=']
reservadas = [
    "alignas", "alignof", "and", "and_eq", "asm", "atomic_cancel",
    "atomic_commit", "atomic_noexcept", "auto", "bitand", "bitor",
    "bool", "break", "case", "catch", "char", "char8_t", "char16_t",
    "char32_t", "class", "compl", "concept", "const", "consteval",
    "constexpr", "constinit", "const_cast", "continue", "co_await",
    "co_return", "co_yield", "decltype", "default", "delete", "do",
    "double", "dynamic_cast", "else", "enum", "explicit", "export",
    "extern", "false", "float", "for", "friend", "goto", "if", "import",
    "inline", "int", "long", "module", "mutable", "namespace", "new",
    "noexcept", "not", "not_eq", "nullptr", "operator", "or", "or_eq",
    "private", "protected", "public", "register", "reinterpret_cast",
    "requires", "return", "short", "signed", "sizeof", "static",
    "static_assert", "static_cast", "struct", "switch", "synchronized",
    "template", "this", "thread_local", "throw", "true", "try", "typedef",
    "typeid", "typename", "union", "unsigned", "using", "virtual", "void",
    "volatile", "wchar_t", "while", "xor", "xor_eq", "cout", "cin", "COMENTARIO", "CADENA", "DEC", "CAR",
    "ENT", "main", "endl", "string"
]



expRegS = [
    (r'([a-zA-Z][a-zA-Z0-9]*)', 'ID'),
    (r'(\#)', 'GATO'),
    (r'(=)', 'IGUAL'),
    (r'(\+)', 'MAS'),
    (r'(\-)', 'MENOS'),
    (r'(\*)', 'MULTIPLICACION'),
    (r'(/)', 'DIVISION'),
    (r'(%)', 'MODULO'),
    (r'(>)', 'MAYORQUE'),
    (r'(<)', 'MENORQUE'),
    (r'(\()', 'IZQPAR'),
    (r'(\))', 'DERPAR'),
    (r'(\[)', 'DERCOR'),
    (r'(\])', 'IZQCOR'),
    (r'(;)', 'PUNTOCOMA'),
    (r'(,)', 'COMA'),
    (r'(\.)', 'PUNTO'),
    (r'({)', 'IZQLLAVE'),
    (r'(})', 'DERLLAVE'),
    (r'(")', 'COMILLAS'),
    (r'(%)', 'PORCENTAJE'),
    (r'(!)', 'NOT'),
    (r'(&)', 'AND'),
    (r'(\|)', 'OR'),
    (r'(\^)', 'POTENCIA'),
    (r'(:)', 'DOSPUNTOS'),
    (r'(\~)', 'VIRGU'),
]

class Token:
    def __init__(self, token, tipoToken):
        self.token = token
        self.tipoToken = tipoToken

    def __repr__(self):
        return f'{self.tipoToken}'


def imprimirTokens(listaTokens):
    tokenTxt = open("Tokens.txt", "w")
    s = ''
    c = 1
    for t in listaTokens:
        for i in t:
            s = s + str(i) + ' '
        print(str(c) + '# ' + s)
        tokenTxt.write(str(c) + '# ' + s + '\n')
        c += 1
        s = ''


def procesarCodigo(nombreArchivo):
    codRep = open('codigoRemplazado.txt', 'w')
    
    with open(nombreArchivo) as archivo:
        for linea in archivo:
            caracter = re.search(r'\".\"', linea)
            cadena = re.search(r'\"(.{2,})\"', linea)
            comentarioU = re.search(r'(//.*)|(/\*.*\*/)', linea)
            numDec = re.search(r'(\d*\.\d+(?:[eE][-+]?\d+)?)', linea)
            numEnt = re.search(r'(\d+(?:[eE][-+]?\d+)?)', linea)
            if caracter:
                res_str = re.sub(r'\".\"', 'CAR', linea)
            elif cadena:
                res_str = re.sub(r'\"(.{2,})\"', 'CADENA', linea)
            elif comentarioU:
                res_str = re.sub(r'(//.*)|(/\*.*\*/)', 'COMENTARIO', linea)
            elif numDec:
                res_str = re.sub(r'(\d*\.\d+(?:[eE][-+]?\d+)?)', 'DEC',  linea)
            elif numEnt:
                res_str = re.sub(r'(\d+(?:[eE][-+]?\d+)?)', 'ENT',  linea)
            else:
                res_str = linea
            codRep.write(res_str)
    codRep.close
     
 
def separarCodigo(nombreArchivo):
    procesarCodigo(nombreArchivo)
    listaLineas = []
    codEsp = open('codigoSeparado.txt', 'w')       
    with open("codigoRemplazado.txt") as archivo:
        for linea in archivo:
            for o in operadores:
                linea = linea.replace(o, '  ' + o + '  ')
            listaLineas.append(linea)
            codEsp.write(linea)   
    return listaLineas


def obtenerTokens(linea):
    listaTokens = []
    listaPalabras = linea.split()
    for t in listaPalabras:
        if t in reservadas:
            listaTokens.append(Token(t, t))
        else:
            for expresion, tipoToken in expRegS:
                if re.match(expresion, t):
                    listaTokens.append(Token(t, tipoToken))
    return listaTokens

def obtenerListaTokens(listaLineas):
    lt = []
    for l in listaLineas:
        lt.append(obtenerTokens(l))
    return lt


def llamarLexer(nombreArchivo):
    lt = obtenerListaTokens(separarCodigo(nombreArchivo))
    imprimirTokens(lt)
    return lt;