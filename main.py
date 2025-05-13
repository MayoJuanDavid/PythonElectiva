import unittest
import math

# Aquí deberías importar o definir las funciones y clases de los ejercicios

class TestEjerciciosIntermedios(unittest.TestCase):

    # 1. Rectángulo
    def test_area_rectangulo(self):
        r = Rectangulo(5, 3)
        self.assertEqual(r.area(), 15)

    # 2. Circulo
    def test_grados_a_radianes(self):
        self.assertAlmostEqual(Circulo.grados_a_radianes(180), math.pi)

    # 3. Generador de pares
    def test_generador_pares(self):
        self.assertEqual(list(pares(4)), [0, 2, 4, 6])

    # 4. Generador de palabras
    def test_generador_palabras(self):
        self.assertEqual(list(palabras('Hola mundo cruel')), ['Hola', 'mundo', 'cruel'])

    # 5. Decorador medir tiempo – no se testea, solo se ejecuta

    # 6. Decorador verificar_enteros
    def test_verificar_enteros_ok(self):
        @verificar_enteros
        def suma(a, b): return a + b
        self.assertEqual(suma(1, 2), 3)

        with self.assertRaises(TypeError):
            suma(1, '2')

    # 9. Contar vocales
    def test_contar_vocales(self):
        self.assertEqual(contar_vocales('Hola mundo'), 4)

    # 10. Invertir palabras
    def test_invertir_palabras(self):
        self.assertEqual(invertir_palabras('Hola mundo cruel'), 'cruel mundo Hola')

    # 11. Fusionar diccionarios
    def test_fusionar_diccionarios(self):
        self.assertEqual(fusionar_diccionarios({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})

    # 12. Contar palabras
    def test_contar_palabras(self):
        self.assertEqual(contar_palabras('hola mundo hola'), {'hola': 2, 'mundo': 1})

    # 13. Intercambiar tupla
    def test_intercambiar(self):
        self.assertEqual(intercambiar((1, 2)), (2, 1))

    # 14. Filtrar impares
    def test_filtrar_impares(self):
        self.assertEqual(filtrar_impares((1, 2, 3, 4)), (1, 3))

    # 15. Set operaciones ya testeadas con operadores directamente

    # 16. Eliminar duplicados
    def test_eliminar_duplicados(self):
        self.assertEqual(sorted(eliminar_duplicados([1, 2, 2, 3])), [1, 2, 3])

    # 17. __str__ en Persona
    def test_persona_str(self):
        p = Persona("Ana", 30)
        self.assertEqual(str(p), "Ana (30 años)")

    # 18. Generador de primos
    def test_primos(self):
        self.assertEqual(list(primos(5)), [2, 3, 5, 7, 11])

    # 19. Decorador para registrar – solo verificar ejecución
    def test_loggear(self):
        @loggear
        def dummy(): return "ok"
        self.assertEqual(dummy(), "ok")

    # 21. Revertir string sin slicing
    def test_revertir(self):
        self.assertEqual(revertir("python"), "nohtyp")

    # 22. Claves comunes
    def test_claves_comunes(self):
        self.assertEqual(claves_comunes({'a':1, 'b':2}, {'b':3, 'c':4}), {'b'})

    # 23. Sub-tupla contenida
    def test_esta_contenida(self):
        self.assertTrue(esta_contenida((1,2,3,4), (2,3)))
        self.assertFalse(esta_contenida((1,2,3), (3,2)))

    # 24. Subset test (ya cubierto con operador <=)

    # 25. Contador de instancias
    def test_instancia_contador(self):
        Instancia.contador = 0  # reset
        a = Instancia()
        b = Instancia()
        self.assertEqual(Instancia.contador, 2)

    # 26. Fibonacci
    def test_fibonacci(self):
        self.assertEqual(list(fibonacci(6)), [0, 1, 1, 2, 3, 5])

    # 27. Decorador repetir
    def test_repetir(self):
        llamadas = []
        @repetir(3)
        def hola():
            llamadas.append("Hola")
        hola()
        self.assertEqual(len(llamadas), 3)

    # 29. Reemplazar palabras
    def test_reemplazar(self):
        self.assertEqual(reemplazar('Hola mundo', {'Hola': 'Adiós'}), 'Adiós mundo')

    # 30. Diccionario con listas
    def test_agregar_valor(self):
        d = {}
        agregar_valor(d, 'clave', 1)
        agregar_valor(d, 'clave', 2)
        self.assertEqual(d, {'clave': [1, 2]})

if __name__ == "__main__":
    unittest.main()
