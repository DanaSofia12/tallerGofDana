"""Única clase de dominio: Documento."""

from __future__ import annotations

from typing import Any

from documento.entidad.constantes import CARGA_DIRECTO, DOC_MBL, ESTADO_RECIBIDO
from documento.entidad.nucleo import ciclo_vida, consulta, novedades
from documento.entidad.nucleo import datos as operacion_datos


class Documento:
    """
    Entidad única del proceso logístico (MBL/HBL).
    La lógica está en entidad/nucleo/; aquí solo se delega.
    """

    def __init__(
        self,
        id_documento: str,
        naviera: str,
        tipo_carga: str = CARGA_DIRECTO,
        tipo_documento: str = DOC_MBL,
        numero_bl: str = "",
        shipper: str = "",
        consignee: str = "",
        puerto_origen: str = "",
        puerto_destino: str = "",
        fecha_salida: str = "",
        fecha_llegada: str = "",
        nombre_barco: str = "",
        viaje: str = "",
        ruta_carpeta: str = "",
        ruta_pdf: str = "",
        estado: str = ESTADO_RECIBIDO,
        datos_digitados: dict[str, Any] | None = None,
        datos_pdf: dict[str, Any] | None = None,
        errores_validacion: list[str] | None = None,
        observaciones: str = "",
    ) -> None:
        self.id_documento = id_documento
        self.naviera = naviera
        self.tipo_carga = tipo_carga
        self.tipo_documento = tipo_documento
        self.numero_bl = numero_bl
        self.shipper = shipper
        self.consignee = consignee
        self.puerto_origen = puerto_origen
        self.puerto_destino = puerto_destino
        self.fecha_salida = fecha_salida
        self.fecha_llegada = fecha_llegada
        self.nombre_barco = nombre_barco
        self.viaje = viaje
        self.ruta_carpeta = ruta_carpeta
        self.ruta_pdf = ruta_pdf
        self.estado = estado
        self.datos_digitados = datos_digitados if datos_digitados is not None else {}
        self.datos_pdf = datos_pdf if datos_pdf is not None else {}
        self.errores_validacion = (
            errores_validacion if errores_validacion is not None else []
        )
        self.observaciones = observaciones

    def registrar_datos_digitados(self, datos_digitados: dict[str, Any]) -> None:
        operacion_datos.registrar_digitados(self, datos_digitados)

    def registrar_datos_pdf(self, datos_pdf: dict[str, Any]) -> None:
        operacion_datos.registrar_pdf(self, datos_pdf)

    def marcar_en_validacion(self) -> None:
        ciclo_vida.marcar_validacion(self)

    def marcar_errores(self, errores: list[str]) -> None:
        ciclo_vida.marcar_errores(self, errores)

    def aprobar_ejecutivo(self) -> None:
        ciclo_vida.aprobar_ejecutivo(self)

    def marcar_preaviso(self) -> None:
        ciclo_vida.marcar_preaviso(self)

    def marcar_borrador_cliente(self) -> None:
        ciclo_vida.marcar_borrador_cliente(self)

    def aprobar_cliente(self) -> None:
        ciclo_vida.aprobar_cliente(self)

    def registrar_novedad(self, cambios: dict[str, Any]) -> None:
        novedades.aplicar_cambios(self, cambios)

    def notificar_cliente(self) -> None:
        ciclo_vida.notificar_cliente(self)

    def campos_comparables(self) -> list[str]:
        return consulta.campos_comparables(self)

    def vista_validacion(self) -> dict[str, Any]:
        return consulta.vista_para_validacion(self)
