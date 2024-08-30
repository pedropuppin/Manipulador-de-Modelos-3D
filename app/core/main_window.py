from PySide6 import QtCore, QtWidgets
from .stl_viewer import STLViewer


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Armazena as instâncias de STLViewer para evitar que sejam coletadas pelo Garbage Collector
        self.viewers = []

        # Botão para abrir o diálogo de upload de arquivos
        self.upload_button = QtWidgets.QPushButton("Carregue os arquivos .stl")
        
        # Área de texto para mostrar os arquivos selecionados
        self.file_list = QtWidgets.QTextEdit()
        self.file_list.setReadOnly(True)
        
        # Botão para visualizar os arquivos selecionados
        self.view_button = QtWidgets.QPushButton("Visualizar o(s) arquivo(s)")
        self.view_button.setEnabled(False)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.upload_button)
        self.layout.addWidget(self.file_list)
        self.layout.addWidget(self.view_button)
        
        # Conecta os sinais aos slots
        self.upload_button.clicked.connect(self.open_file_dialog)
        self.view_button.clicked.connect(self.view_stl_files)
        
    @QtCore.Slot()
    def open_file_dialog(self):
        # Abre o diálogo de seleção de arquivos
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            "Select STL Files",
            "",
            "STL Files (*.stl)"
        )

        if files:
            # Exibe os arquivos selecionados na área de texto
            self.file_list.clear()
            for file in files:
                self.file_list.append(file)
            self.view_button.setEnabled(True)
                
    @QtCore.Slot()
    def view_stl_files(self):
        # Pega todos os arquivos da lista para visualização
        stl_files = self.file_list.toPlainText().splitlines()

        for stl_file in stl_files:
            self.open_stl_viewer(stl_file)

    def open_stl_viewer(self, stl_file):
        viewer = STLViewer(stl_file)
        viewer.show()
        self.viewers.append(viewer) # Armazena a referência


