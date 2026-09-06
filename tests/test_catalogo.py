import unittest

from servicios.catalogo import Catalogo


class TestCatalogo(unittest.TestCase):

    def setUp(self):
        self.catalogo = Catalogo()
        self.catalogo.cargar_desde_json("datos/juegos.json")

    def test_buscar_por_titulo(self):
        resultado = self.catalogo.buscar("Minecraft")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.titulo, "Minecraft")

    def test_buscar_no_existente(self):
        resultado = self.catalogo.buscar("NoExiste")

        self.assertIsNone(resultado)

    def test_listar(self):
        resultados = self.catalogo.listar()

        self.assertTrue(len(resultados) > 0)

    def test_filtrar_por_genero(self):
        resultados = self.catalogo.filtrar("aventura")

        for videojuego in resultados:
            self.assertEqual(videojuego.genero.lower(), "aventura")

    def test_top_10(self):
        resultados = self.catalogo.top_10()

        self.assertLessEqual(len(resultados), 10)

        for i in range(len(resultados) - 1):
            self.assertGreaterEqual(
                resultados[i].rating,
                resultados[i + 1].rating
            )

    def test_relacionados(self):
        resultados = self.catalogo.relacionados("Minecraft")

        self.assertIsInstance(resultados, list)

    def test_alternativas_desarrollador(self):
        resultados = self.catalogo.alternativas_desarrollador("Minecraft")

        self.assertIsInstance(resultados, list)