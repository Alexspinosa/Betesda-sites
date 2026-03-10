
# Modelos de Pages resources
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class ResourcePage(Page):
    descripcion = models.TextField("Descripción", blank=True)
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
    url_externa = models.URLField("URL externa", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("descripcion"),
        FieldPanel("imagen_destacada"),
        FieldPanel("documento"),
        FieldPanel("url_externa"),
    ]

    class Meta:  # type: ignore[reportIncompatibleVariableOverride]
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"
