# -*- coding: utf-8 -*-
__author__ = "Rubén Mulero"

# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from src.packControladoras import CCrearGrupo
import re

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(556, 330)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lNombreGrupo = QtWidgets.QLineEdit(Dialog)
        self.lNombreGrupo.setMaxLength(25)
        self.lNombreGrupo.setAlignment(QtCore.Qt.AlignCenter)
        self.lNombreGrupo.setObjectName("lNombreGrupo")
        self.horizontalLayout_2.addWidget(self.lNombreGrupo)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.bCrearGrupo = QtWidgets.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/dialog-ok.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCrearGrupo.setIcon(icon)
        self.bCrearGrupo.setObjectName("bCrearGrupo")
        self.horizontalLayout.addWidget(self.bCrearGrupo)
        spacerItem6 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.bCancelar = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/edit-delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCancelar.setIcon(icon1)
        self.bCancelar.setObjectName("bCancelar")
        self.horizontalLayout.addWidget(self.bCancelar)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.lNombreGrupo)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Nombre Grupo"))
        self.label.setText(_translate("Dialog", "Por favor, define un nombre válido para crear el &grupo:"))
        self.bCrearGrupo.setText(_translate("Dialog", "Crear Grupo"))
        self.bCancelar.setText(_translate("Dialog", "Cancelar"))

class CrearGrupoNombre(QtWidgets.QDialog):
    # Definimos el constructor de la clase principal
    def __init__(self, p_iu_crear_grupo, p_iu_main, p_id_usuario, p_lista_alumnos, p_lista_grupos, parent=None):
        # Llamamos al constructor de la clase padre
        super(CrearGrupoNombre, self).__init__(parent)
        self.el_parent = parent
        # Instancio la Interfaz
        self.ventana = Ui_Dialog()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        self.iu_crear_grupo = p_iu_crear_grupo # El objeto de Crear_Grupo para poder cerrar la interfaz anterior.
        self.iu_main = p_iu_main # El objeto del main para poder recargar el combobox del main
        self.id_usuario = p_id_usuario
        self.lista_alumnos = p_lista_alumnos
        self.lista_grupos = p_lista_grupos

        # Conectamos los botones
        self.ventana.bCancelar.clicked.connect(self.close)
        self.ventana.bCrearGrupo.clicked.connect(self.crear_grupo)

    def crear_grupo(self):
        # Obtenemos le nombre del grupoo y lo validamos
        nombre_grupo = self.ventana.lNombreGrupo.text()
        if self.__mascara_filtrado(nombre_grupo):
            # El nombre del grupo no existe por lo que podemos insertar los datos en la BD
            controladora_grupo = CCrearGrupo.CCrearGrupo()
            resultado = controladora_grupo.crear_grupo(self.id_usuario, nombre_grupo,
                                                       self.lista_alumnos, self.lista_grupos)
            # Si el resultado es correcto, mostramos una pantalla de confirmación. y cerramoas la interfaz anterior.
            print "Resultado de la operación es %s" % resultado
            if resultado is True:
                self.iu_main.generar_combo_box()
                self.iu_main.seleccionar_item()
                # Creamos ventana de aviso
                msg_box = QMessageBox()
                msg_box.setIcon(1)
                msg_box.setWindowTitle("Creación de un grupo")
                msg_box.setText("CORRECTO")
                msg_box.setInformativeText("El grupo se ha creado corretamente")
                msg_box.exec_()
                # Cerramos y volvemos al main
                self.iu_crear_grupo.close()
                self.close()
            elif resultado is None:
                print "El grupo ya existe en el sistema"
                msg_box = QMessageBox()
                msg_box.setIcon(2)
                msg_box.setWindowTitle("Creación de un grupo")
                msg_box.setText("ADVERTENCIA")
                msg_box.setInformativeText("El nombre del grupo ya existe en el sistema. Por favor elige otro.")
                msg_box.exec_()
            else:
                print "El grupo no se ha creado correctamente por alguna razón."
                error_box_2 = QMessageBox()
                error_box_2.setIcon(3)
                error_box_2.setWindowTitle("Creación de un grupo")
                error_box_2.setText("Error")
                error_box_2.setInformativeText("El grupo no se ha podido crear debido a un error interno.")
                error_box_2.exec_()
        else:
            print "Los caracteres del grupo introducidos son inválidos"
            error_box = QMessageBox()
            error_box.setIcon(3)
            error_box.setWindowTitle("Creación de un grupo")
            error_box.setText("Error")
            error_box.setInformativeText("El nombre del grupo introducido contiene caracteres extraños. Introduce"
                                         "un nombre de grupo correcto.")
            error_box.exec_()

    def __mascara_filtrado(self, p_texto):
        """
        Filtra los valores de entrada para permitir sólo letras y números

        :param p_texto: El texto a comprobar
        :return: True si la cadeno de texto contiene a-z, A-Z, 0-9
                False si la cadena de texto contiene espacios o caracteres extraños
        """
        patron = re.compile("[a-zA-Z\d]*$")
        return patron.match(p_texto)
