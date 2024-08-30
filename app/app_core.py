import sys
from PySide6 import QtCore, QtWidgets, QtGui
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
                
        # Botão para abrir o diálogo de upload de arquivos
        self.upload_button = QtWidgets.QPushButton("Carregue os arquivos .stl")
        
        # Área de texto para mostrar os arquivos selecionados
        self.file_list = QtWidgets.QTextEdit()
        self.file_list.setReadOnly(True)
        
        # Botão para visualizar o arquivo selecionado
        self.view_button = QtWidgets.QPushButton("View Selected STL")
        self.view_button.setEnabled(False)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.upload_button)
        self.layout.addWidget(self.file_list)
        self.layout.addWidget(self.view_button)
        
        # Conecta os sinais aos slots
        self.upload_button.clicked.connect(self.open_file_dialog)
        self.view_button.clicked.connect(self.view_stl_file)
        
        # Configuração do renderizador VTK
        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.layout.addWidget(self.vtk_widget)
        self.vtk_widget.setVisible(False)

        self.ren = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.ren)

    @QtCore.Slot()
    def open_file_dialog(self):
        # Abrir o diálogo de seleção de arquivos
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            "Select STL Files",
            "",
            "STL Files (*.stl)"
        )

        if files:
            # Exibir os arquivos selecionados na área de texto
            self.file_list.clear()
            for file in files:
                self.file_list.append(file)
            self.view_button.setEnabled(True)
                
    @QtCore.Slot()
    def view_stl_file(self):
        # Pegar o primeiro arquivo da lista para visualização
        stl_file = self.file_list.toPlainText().splitlines()[0]

        # Configurar o leitor de arquivo STL
        reader = vtk.vtkSTLReader()
        reader.SetFileName(stl_file)

        # Configurar o mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        # Configurar o ator
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Limpar o renderizador atual e adicionar o novo ator
        self.ren.RemoveAllViewProps()
        self.ren.AddActor(actor)

        # Configurar a câmera e atualizar a visualização
        self.ren.ResetCamera()
        self.vtk_widget.setVisible(True)
        self.vtk_widget.GetRenderWindow().Render()
        self.vtk_widget.GetRenderWindow().GetInteractor().Start()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.setWindowTitle("3D auto model")
    widget.show()

    sys.exit(app.exec())