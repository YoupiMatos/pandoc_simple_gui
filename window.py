from json import tool
import PySimpleGUI as psg

file_list_column = [
        psg.Text("Document à convertir"),
        psg.In("Document...",size=(25, 1), enable_events=True, key="input_file"),
        psg.FileBrowse(),

]

outputFolder = [
        psg.Text("Dossier de sortie"),
        psg.In("Dossier de sortie...", size=(25, 1), enable_events=True, key="output_folder", ),
        psg.FolderBrowse()
]

converted_filename = [
        psg.Text("Nom du fichier converti"),
        psg.Text("ℹ️", tooltip='Renseignez le nom du fichier de sortie, avec son extension. Pandoc convertira directement vers cette extension. Exemple: "monfichier.pdf"'),
        psg.Input('exemple.doc', size=(25,1), enable_events=True, key="name")
]

confirm_button = [
        psg.Button('Convertir', key="convert")
]

last_result = [
        psg.Text('Dernier résultat : '),
        psg.Text('', key='last_result')
]

output_format_list = [
        psg.Text("Formats de sortie :"),
        psg.Combo([], key='output_format_list', enable_events=True, size=(25,25))
]

input_format_list = [
        psg.Text("Formats d'entrée :"),
        psg.Combo([], key='input_format_list', enable_events=True, size=(25,25))
]

format_col = [input_format_list, output_format_list]

layout = [[ 
        psg.Column([
            file_list_column,
            outputFolder,
            converted_filename,
            confirm_button,
            last_result,
        ]),
        psg.Column(format_col)
]]

window = psg.Window("Pandoc Simple GUI", layout, margins=(100, 50), resizable=True, finalize=True)