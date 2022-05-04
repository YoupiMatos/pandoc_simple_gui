from window import window
import os.path
import subprocess

def getInputFormats():
    input_formats = subprocess.check_output(["powershell", "-Command", "pandoc --list-input-formats"])
    input_formats = str(input_formats)
    input_list = []
    input_list = input_formats.split(r"\r\n")
    input_list[0] = input_list[0].replace("'b'", "")
    input_list.pop()

    print(input_list)
    print(len(input_list))
    
    return input_list

def getOutputFormats():
    output_formats = subprocess.check_output(["powershell", "-Command", "pandoc --list-output-formats"])
    output_formats = str(output_formats)
    output_list = []
    output_list = output_formats.split(r"\r\n")
    output_list[0] = output_list[0].replace("'b'", "")
    output_list.pop()

    print(output_list)
    print(len(output_list))
    
    return output_list

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def convert(entry_file: str, output_folder: str, name: str):
    entry_file = '"' + entry_file + '"' 
    output_folder = '"' + output_folder + '/' 
    name =  name + '"' 

    print(entry_file)
    print(output_folder)
    print(name) 

    result = run('pandoc ' + entry_file + " -o " + output_folder + name) 
    return result

def getResult(result: subprocess.CompletedProcess):
    if result.returncode == 0:
        pass
input_formats = getInputFormats()
output_formats = getOutputFormats()
while True:     #Main event loop
    window['input_format_list'].update(values=input_formats)
    window['output_format_list'].update(values=output_formats)
    event, values = window.read()
    
    if event in (None, 'Exit'):
        break
    if event == "convert":
        input_file = values['input_file']
        output_folder = values['output_folder']
        name = values["name"]

        result = convert(input_file, output_folder, name)
        if result.returncode == 0:
            window.Element(key='last_result').update("Conversion réussie!")
        elif "pdflatex" in str(result.stderr):
            window.Element(key='last_result').update("Échec de la conversion. Il faut installer pdflatex pour convertir vers le format pdf.")
        else:
            window.Element(key='last_result').update("Échec de la conversion.")
        print(result)