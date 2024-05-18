

#! /usr/bin/env python
###################################################################################################
#
#   1 Lee un archivo input (txt) que contiene en cada línea la ruta absoluta de los archivos a ser
#     transformados
#   2 Itera por cada archivo en el input file para transformarlo a ansi y luego salvar la versión
#     recién transformada (contiene una extensión adicional ".txt" al nombre exacto del fuente)
#   3 Los archivos de salida son ubicados en la misma ruta que el archivo origen, para conveniencia
#     del usuario
#
#   Cómo ejecutar?
#   > python* <this.py> -i "<ruta sources>"
#   * usar python3 en linux, python en windows
#
#   Nota: esta version sólo convierte de ebcdic a ansi.
###################################################################################################
#
import codecs, os, getopt, sys, time
input_file = converted_contents = file_ = out_file_name = ""
argv = sys.argv[1:]
# Use the following lines to use interactive getOps in CMD
try:
    opts, args = getopt.getopt(argv, ":i:o:h")
except:
    print("--Error: opcion invalida! Usar solamente -i=\"input list\" ; -h=help")

for opt, arg in opts:
    if opt in ['-i']:
        input_file = arg
    else:
        print(f"Help:\nSintaxis:\n  > python* {sys.argv[0]} -i \"X\" \n    Parametros validos: -i=\"input list\" ; -h=help ")
        print("  Input list = archivo.txt que contiene las rutas absolutas de los archivos que se desean transformar.")
        print('''Ej. para ejecutar:
      $> python3 <programa.py> -i "c:/tmp/input.txt"
    C:\> python  <programa.py> -i "c:\\tmp\\input.txt" ''')
        exit(1)

print(f"\n **Convertidor de archivos Ebcdic a formato legible (ansi)\n      Este proceso produce un archivo de salida convertido en la misma ruta que el archivo input\n")
print(f"    input file:    {input_file} (lista con rutas absolutas de los archivos a convertir)")
print(f"    output file:   Si: Input = c:/tmp/x.DAT --> Output = c:/tmp/x.DAT.txt (misma ruta/nombre de archivo + ext='.txt')\n")

# Format converter
def ebcdic_to_ansi_file_converter(input_file):
    input_file_ = os.path.join(input_file)
    with codecs.open(input_file_, "r", encoding='cp500', errors='ignore') as f: # this only converts the input format from ebcdic
        return f.read()

# Input file's list's reading
with open(input_file, 'r') as input_file:
    files_to_process = input_file.readlines()

#files_to_process = ["C:\\Users\\avassallomal\\OneDrive - DXC Production\\Desktop\\FILE001.DAT"]
# Iterates file per file in order to pass each file to the file converter and creates an output converted-output-file in the same path as the input file
print(f"   * Conversion de archivo(s): ")
try:
    for file in files_to_process:
        file_ = file.replace('\n','').strip('"').strip("'")
        print(f"     * {file_}", end="")
        converted_contents = ebcdic_to_ansi_file_converter(file_)
        out_file_name = os.path.join(file_) + ".txt"
        with open(out_file_name, "w") as output_file: # this reads from the function's retuned converted content and writes it out in the desired encoding or format
            output_file.write(converted_contents)
        time.sleep(.25) # allows the HD to settle before opening a new file to write
        print(f" == > finalizado. --> [{out_file_name}]")
        converted_contents = out_file_name = ""
        time.sleep(.25) # allows the HD to settle before opening a new file to write
except Exception as e:
    print(f" Exception {e}")
    pass