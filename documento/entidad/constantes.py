"""Valores del dominio Documento (sin clases adicionales)."""

# Tipos de carga
CARGA_DIRECTO = "directo"
CARGA_CONSOLIDADO = "consolidado"

# Tipos de conocimiento de embarque
DOC_MBL = "mbl"
DOC_HBL_MASTER = "hbl_master"
DOC_HBL_HIJO = "hbl_hijo"

# Estados del ciclo de vida
ESTADO_RECIBIDO = "recibido"
ESTADO_EN_COTIZACION = "en_cotizacion"
ESTADO_COTIZADO = "cotizado"
ESTADO_PENDIENTE_CONFIRMACION = "pendiente_confirmacion_cliente"
ESTADO_CONFIRMADO_CLIENTE = "confirmado_cliente"
ESTADO_EN_NEGOCIO_NAVIERA = "en_negocio_naviera"
ESTADO_PDF_RECIBIDO = "pdf_recibido"
ESTADO_DIGITADO = "digitado"
ESTADO_EN_VALIDACION = "en_validacion"
ESTADO_CON_ERRORES = "con_errores"
ESTADO_APROBADO_EJECUTIVO = "aprobado_ejecutivo"
ESTADO_PREAVISO_ENVIADO = "preaviso_enviado"
ESTADO_BORRADOR_CLIENTE = "borrador_enviado_cliente"
ESTADO_APROBADO_CLIENTE = "aprobado_cliente"
ESTADO_NOVEDAD = "novedad_detectada"
ESTADO_NOTIFICADO_CLIENTE = "notificado_cliente"

CAMPOS_COMPARABLES = (
    "numero_bl",
    "shipper",
    "consignee",
    "puerto_origen",
    "puerto_destino",
    "fecha_salida",
    "fecha_llegada",
    "nombre_barco",
    "viaje",
)
