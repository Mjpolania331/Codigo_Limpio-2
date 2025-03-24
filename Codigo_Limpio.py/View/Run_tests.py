import unittest

def ejecutar_pruebas():
    loader = unittest.TestLoader()
    tests = loader.discover("../tests") 
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(tests)

if __name__ == '__main__':
    print("Ejecutando todas las pruebas...\n")
    ejecutar_pruebas()