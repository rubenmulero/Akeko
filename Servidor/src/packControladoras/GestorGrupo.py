# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from Servidor.src.packGestorBD import MySQLConnector

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class GestorGrupo(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_grupos(self, p_id_usuario):
        """
        Obtenemos los grupos que tiene un usuario logueado

        :param p_id_usuario: El identificador del uusairo
        :return: La lista de los grupos que contiene el usuario
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdGrupo,NombreGrupo FROM Grupo WHERE IdUsuario=%s", p_id_usuario
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def borrar_grupo(self, p_id_grupo):
        """
        Borra un grupo del sistema dado su identificador
        :param p_id_grupo:
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Grupo WHERE IdGrupo=%s", p_id_grupo
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd
