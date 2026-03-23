# Modelos de Pages resources
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class ResourceIndexPage(Page):
    """Página índice que lista todos los recursos"""

    sede_nombre = models.CharField(
        "Nombre de la sede",
        max_length=255,
        blank=True,
        default="Comunidad Cristiana · Central"
    )

    imagen_hero = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Imagen hero",
    )

    content_panels = Page.content_panels + [
        FieldPanel("sede_nombre"),
        FieldPanel("imagen_hero"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        categoria = request.GET.get("categoria", "")
        recursos = ResourcePage.objects.live().child_of(self).order_by("-first_published_at")
        if categoria:
            recursos = recursos.filter(categoria=categoria)
        context["recursos"] = recursos
        context["categoria_activa"] = categoria
        return context

    class Meta:  # type: ignore[reportIncompatibleVariableOverride]
        verbose_name = "Índice de recursos"


class ResourcePage(Page):
    """Página de cada recurso individual"""

    CATEGORIAS = [
        ("sermon", "Sermón en video"),
        ("devocional", "Devocional"),
        ("libro", "Libro y PDF"),
    ]

    sede_nombre = models.CharField(
        "Nombre de la sede",
        max_length=255,
        blank=True,
        default="Comunidad Cristiana · Central"
    )

    etiqueta = models.CharField(
        "Etiqueta",
        max_length=100,
        blank=True,
        default="Recurso destacado"
    )

    categoria = models.CharField(
        "Categoría",
        max_length=50,
        choices=CATEGORIAS,
        blank=True
    )

    tiempo_lectura = models.CharField(
        "Tiempo de lectura",
        max_length=50,
        blank=True,
        help_text="Ejemplo: 5 min, 30 min, 1 hora"
    )

    titulo_contenido = models.CharField(
        "Título del contenido",
        max_length=255,
        blank=True
    )

    titulo_acento = models.CharField(
        "Título con acento de color",
        max_length=100,
        blank=True
    )

    descripcion = models.TextField(
        "Descripción",
        blank=True
    )

    imagen_destacada = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Imagen destacada",
    )

    documento = models.ForeignKey(
        "wagtaildocs.Document",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Archivo descargable",
    )

    texto_boton_descarga = models.CharField(
        "Texto botón descarga",
        max_length=50,
        blank=True,
        default="Descargar documento"
    )

    url_externa = models.URLField(
        "URL externa",
        blank=True
    )

    texto_boton_externo = models.CharField(
        "Texto botón externo",
        max_length=50,
        blank=True,
        default="Ver recurso externo"
    )

    content_panels = Page.content_panels + [
        FieldPanel("sede_nombre"),
        FieldPanel("etiqueta"),
        FieldPanel("categoria"),
        FieldPanel("tiempo_lectura"),
        FieldPanel("titulo_contenido"),
        FieldPanel("titulo_acento"),
        FieldPanel("descripcion"),
        FieldPanel("imagen_destacada"),
        FieldPanel("documento"),
        FieldPanel("texto_boton_descarga"),
        FieldPanel("url_externa"),
        FieldPanel("texto_boton_externo"),
    ]

    class Meta:  # type: ignore[reportIncompatibleVariableOverride]
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"
