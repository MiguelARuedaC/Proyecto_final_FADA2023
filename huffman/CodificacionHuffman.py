from huffman.arbolbinariohuffman import ArbolBinarioHuffman
from huffman.DecodificacionHuffman import DecodificacionHuffman
import time
class CodificacionHuffman:
    """
    Clase CodificacionHUffman
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
     Autor: <Leider Santiago Cortés Hernandez - 2159879
            Miguel Angel Rueda Colonia - 2159896>
    """

    def __init__(self):
        self.tree = None
        self.table = None
        self.summary = None
        self.text = None

    def encode(self, text):
        """
        Codifica el texto.
        :param text: texto a codificar
        :return: texto codificado
        """
        self.text = text
        # Construir el árbol de Huffman
        frequency = {}
        for char in text:
            frequency[char] = frequency.get(char, 0) + 1
        nodes = []
        for key, value in frequency.items():
            node = ArbolBinarioHuffman()
            node.key = (value, key)
            nodes.append(node)
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.key[0])
            left = nodes[0]
            right = nodes[1]
            parent = ArbolBinarioHuffman()
            parent.key = (left.key[0] + right.key[0], None)
            parent.left = left
            parent.right = right
            nodes = nodes[2:]
            nodes.append(parent)
        self.tree = nodes[0]

        # Generar la tabla de codificación
        self.table = {}
        self.generate_table(self.tree, "")

        # Codificar el texto
        encoded_text = ""
        for char in text:
            encoded_text += self.table[char]
        return encoded_text

    def generate_table(self, node, code):
        """
        Genera la tabla de codificación recursivamente.
        :param node: nodo actual
        :param code: código actual
        """
        if node.key[1] is not None:
            self.table[node.key[1]] = code
        else:
            self.generate_table(node.left, code + "0")
            self.generate_table(node.right, code + "1")

    def getTree(self):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        return self.tree

    def getTable(self):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
        return self.table

    def getSummary(self):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        # Porcentaje de compresión
        total = self.count_characters(self.text)
        total2 = self.count_characters(self.encode(self.text))

        # Numero de nodos
        total_nodos_huffman = self.contar_nodos_huffman(self.tree)

        # Profundidad del arbol
        profundidad_arbol = self.obtener_profundidad_huffman(self.tree)

        # Construcción del resumen:
        summary = f"Total de caracteres: {total}\n"
        summary += f"Total de caracteres binarios: {total2}\n"
        summary += f"Total de nodos del árbol de Huffman: {total_nodos_huffman}\n"
        summary += f"Profundidad del árbol de Huffman: {profundidad_arbol}\n"

        return summary

    def count_characters(self, text):
        """
        Cuenta el número total de caracteres en el texto.
        :param text: texto para contar los caracteres
        :return: número total de caracteres
        """
        contador = {}
        total_caracteres = 0
        for caracter in text:
            if caracter in contador:
                contador[caracter] += 1
            else:
                contador[caracter] = 1
            total_caracteres += 1
        return total_caracteres

    def contar_nodos_huffman(self, nodo):
        if nodo is None:
            return 0

        return 1 + self.contar_nodos_huffman(nodo.left) + self.contar_nodos_huffman(nodo.right)

    def obtener_profundidad_huffman(self, nodo):
        if nodo is None:
            return 0

        profundidad_izquierda = self.obtener_profundidad_huffman(nodo.left)
        profundidad_derecha = self.obtener_profundidad_huffman(nodo.right)

        return max(profundidad_izquierda, profundidad_derecha) + 1


# Crear una instancia de HuffmanCoding:

huffman = CodificacionHuffman()

# Codificar texto 1:
inicio1 =time.time()
texto_original = """nwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjn"""
texto_codificado = huffman.encode(texto_original)

# Imprimir el texto codificado
print("Texto original:", texto_original)
print("Texto codificado:", texto_codificado)

# Obtener el árbol de Huffman, la tabla de codificación y la tabla de resumen
arbol_huffman = huffman.getTree()
tabla_codificacion = huffman.getTable()
tabla_resumen = huffman.getSummary()

# Imprimir el árbol de Huffman
print("\nÁrbol de Huffman:")
arbol_huffman.traverse()

# Imprimir la tabla de codificación
print("\nTabla de Codificación:")
for simbolo, codigo in tabla_codificacion.items():
    print(simbolo, ":", codigo)

# Crear una instancia de HuffmanDecoding
decodificador = DecodificacionHuffman()

# Decodificar el texto
texto_decodificado = decodificador.decode(texto_codificado, arbol_huffman)

# Imprimir el texto decodificado
print("\nTexto decodificado:", texto_decodificado)

# Imprimir resumen
print("\nTabla de resumen:")
print(tabla_resumen)
fin1 = time.time()
tiempoEjecucion1 = (fin1 - inicio1) * 1000
print("\nTiempo de ejecucion prueba de 100:")
print({tiempoEjecucion1})
#--------------------------------------------------------------------------------------
# Codificar texto 2:
inicio2 =time.time()
texto_original = """nwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjn"""
texto_codificado = huffman.encode(texto_original)

# Imprimir el texto codificado
print("Texto original:", texto_original)
print("Texto codificado:", texto_codificado)

# Obtener el árbol de Huffman, la tabla de codificación y la tabla de resumen
arbol_huffman = huffman.getTree()
tabla_codificacion = huffman.getTable()
tabla_resumen = huffman.getSummary()

# Imprimir el árbol de Huffman
print("\nÁrbol de Huffman:")
arbol_huffman.traverse()

# Imprimir la tabla de codificación
print("\nTabla de Codificación:")
for simbolo, codigo in tabla_codificacion.items():
    print(simbolo, ":", codigo)

# Crear una instancia de HuffmanDecoding
decodificador = DecodificacionHuffman()

# Decodificar el texto
texto_decodificado = decodificador.decode(texto_codificado, arbol_huffman)

# Imprimir el texto decodificado
print("\nTexto decodificado:", texto_decodificado)

# Imprimir resumen
print("\nTabla de resumen:")
print(tabla_resumen)
fin2 = time.time()
tiempoEjecucion2 = (fin2 - inicio2) * 1000
print("\nTiempo de ejecucion prueba de 200:")
print({tiempoEjecucion2})
#--------------------------------------------------------------------------------------
#Texto a codificar de emtrada 500:

inicio3 = time.time()

texto_original2 = """nwdfacijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjxyzs"""
texto_codificado2 = huffman.encode(texto_original2)

# Imprimir el texto codificado
print("Texto original:", texto_original2)
print("Texto codificado:", texto_codificado2)

# Obtener el árbol de Huffman, la tabla de codificación y la tabla de resumen
arbol_huffman2 = huffman.getTree()
tabla_codificacion2 = huffman.getTable()
tabla_resumen2 = huffman.getSummary()

# Imprimir el árbol de Huffman
print("\nÁrbol de Huffman:")
arbol_huffman2.traverse()

# Imprimir la tabla de codificación
print("\nTabla de Codificación:")
for simbolo, codigo in tabla_codificacion2.items():
    print(simbolo, ":", codigo)

# Crear una instancia de HuffmanDecoding
decodificador2 = DecodificacionHuffman()

# Decodificar el texto
texto_decodificado2 = decodificador2.decode(texto_codificado2, arbol_huffman2)

# Imprimir el texto decodificado
print("\nTexto decodificado:", texto_decodificado2)

# Imprimir resumen
print("\nTabla de resumen:")
print(tabla_resumen2)

fin3 = time.time()
tiempoEjecucion3 = (fin3 - inicio3) * 1000
print("\nTiempo de ejecucion prueba de 500:")
print({tiempoEjecucion3})
#--------------------------------------------------------------------------------------
#Texto a codificar de emtrada 1000:

inicio4 = time.time()

texto_original2 = """nwdfacijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjxyzsnwdfacijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjxyzs"""
texto_codificado2 = huffman.encode(texto_original2)

# Imprimir el texto codificado
print("Texto original:", texto_original2)
print("Texto codificado:", texto_codificado2)

# Obtener el árbol de Huffman, la tabla de codificación y la tabla de resumen
arbol_huffman2 = huffman.getTree()
tabla_codificacion2 = huffman.getTable()
tabla_resumen2 = huffman.getSummary()

# Imprimir el árbol de Huffman
print("\nÁrbol de Huffman:")
arbol_huffman2.traverse()

# Imprimir la tabla de codificación
print("\nTabla de Codificación:")
for simbolo, codigo in tabla_codificacion2.items():
    print(simbolo, ":", codigo)

# Crear una instancia de HuffmanDecoding
decodificador2 = DecodificacionHuffman()

# Decodificar el texto
texto_decodificado2 = decodificador2.decode(texto_codificado2, arbol_huffman2)

# Imprimir el texto decodificado
print("\nTexto decodificado:", texto_decodificado2)

# Imprimir resumen
print("\nTabla de resumen:")
print(tabla_resumen2)

fin4 = time.time()
tiempoEjecucion4 = (fin4 - inicio4) * 1000
print("\nTiempo de ejecucion prueba de 1000:")
print({tiempoEjecucion4})
#--------------------------------------------------------------------------------------
#Texto a codificar de emtrada 1500:

inicio5 = time.time()

texto_original2 = """nwdfacijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnnwdfacijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjxyzswdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjxyzsnwdfacijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjnwdfcijneiorvbhdsfbevhohfvjfevijndfjinjidfnjivdjfivjdvjidajvjidsfnvjidvijdijndvjidafjivvjdifvjidfvjxyzs"""
texto_codificado2 = huffman.encode(texto_original2)

# Imprimir el texto codificado
print("Texto original:", texto_original2)
print("Texto codificado:", texto_codificado2)

# Obtener el árbol de Huffman, la tabla de codificación y la tabla de resumen
arbol_huffman2 = huffman.getTree()
tabla_codificacion2 = huffman.getTable()
tabla_resumen2 = huffman.getSummary()

# Imprimir el árbol de Huffman
print("\nÁrbol de Huffman:")
arbol_huffman2.traverse()

# Imprimir la tabla de codificación
print("\nTabla de Codificación:")
for simbolo, codigo in tabla_codificacion2.items():
    print(simbolo, ":", codigo)

# Crear una instancia de HuffmanDecoding
decodificador2 = DecodificacionHuffman()

# Decodificar el texto
texto_decodificado2 = decodificador2.decode(texto_codificado2, arbol_huffman2)

# Imprimir el texto decodificado
print("\nTexto decodificado:", texto_decodificado2)

# Imprimir resumen
print("\nTabla de resumen:")
print(tabla_resumen2)

fin5 = time.time()
tiempoEjecucion5 = (fin4 - inicio4) * 1000
print("\nTiempo de ejecucion prueba de 1000:")
print({tiempoEjecucion5})


