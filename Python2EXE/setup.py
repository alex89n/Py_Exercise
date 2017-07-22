from cx_Freeze import setup, Executable

setup(name='urlParse',
      version='1.0',
      description='Parse stuff',
      executables = [Executable("printAditionaLabels.py")])

      
# python setup.py build