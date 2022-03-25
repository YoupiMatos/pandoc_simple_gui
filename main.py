from window import window
import os.path
import subprocess

def getOutputFormats():
    output_formats = subprocess.check_output(["powershell", "-Command", "pandoc --list-input-formats"])
    output_formats = str(output_formats)
    output_list = []
    final_list = []
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


while True:     #Main event loop
    output_formats = getOutputFormats()
    window['format_list'].update(output_formats)
    event, values = window.read()
    
    if event in (None, 'Exit'):
        break
    if event == "convert":
        input_file = values['input_file']
        output_folder = values['output_folder']
        name = values["name"]

        result = convert(input_file, output_folder, name)
        if result.returncode == 0:
            window.Element(key='last_result')
        print(result)