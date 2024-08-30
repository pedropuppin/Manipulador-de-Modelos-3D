from PySide6 import QtWidgets
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk

class STLViewer(QtWidgets.QWidget):
    def __init__(self, stl_file):
        super().__init__()
        
        self.setWindowTitle(f"Visualizador - {stl_file}")
        self.resize(800, 600)

        # Configuração do layout
        layout = QtWidgets.QVBoxLayout(self)
        
        # Configuração do renderizador VTK
        self.vtk_widget = QVTKRenderWindowInteractor(self)
        layout.addWidget(self.vtk_widget)

        self.ren = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.ren)

        # Configura o leitor de arquivo STL
        reader = vtk.vtkSTLReader()
        reader.SetFileName(stl_file)

        # Configura o mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        # Configura o ator
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Adiciona o ator ao renderizador
        self.ren.AddActor(actor)

        # Configura a câmera e atualiza a visualização
        self.ren.ResetCamera()
        self.vtk_widget.GetRenderWindow().Render()
        self.vtk_widget.GetRenderWindow().GetInteractor().Start()

    def closeEvent(self, event):
        # Finaliza o interactor corretamente
        interactor = self.vtk_widget.GetRenderWindow().GetInteractor()
        interactor.TerminateApp()

        # Desassocia e deleta o renderizador
        self.vtk_widget.GetRenderWindow().RemoveRenderer(self.ren)
        self.ren = None

        # Finaliza o contexto de renderização e deletar o widget
        self.vtk_widget.GetRenderWindow().Finalize()
        self.vtk_widget.setParent(None)
        self.vtk_widget.deleteLater()

        event.accept()