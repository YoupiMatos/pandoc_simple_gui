import PySimpleGUI as psg

file_list_column = [

    [
        psg.Text("Document à convertir"),
        psg.In(size=(25, 1), enable_events=True, key="input_file"),
        psg.FileBrowse(),

    ]

]

outputFolder = [
    [
        psg.Text("Dossier de sortie"),
        psg.In("dossier de sortie...", size=(25, 1), enable_events=True, key="output_folder", ),
        psg.FolderBrowse()
    ]
]

converted_filename = [
    [
        psg.Text("Nom du fichier converti"),
        psg.Input('fichier de sortie', size=(25,1), enable_events=True, key="name")
    ]
]

confirm_button = [
    [
        psg.Button('Convertir', key="convert")
    ]
]

last_result = [
    [
        psg.Text('Dernier résultat : '),
        psg.Text('', key='last_result')
    ]
]

format_list = [
    [
        psg.Text("Formats de sortie :"),
        psg.Listbox([], key='format_list', enable_events=True, size=(25,25))
    ]
]

layout = [
    [psg.Column(file_list_column)],
    [psg.Column(outputFolder)],
    [psg.Column(converted_filename)],
    [psg.Column(format_list)],
    [psg.Column(confirm_button)],
    [psg.Column(last_result)]
]


window = psg.Window("Pandoc Simple GUI", layout, margins=(100, 50), resizable=True, finalize=True)