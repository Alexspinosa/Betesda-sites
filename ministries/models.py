
# Modelos de Pages Ministerios
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class MinistriesPage(Page):
    descripcion = models.TextField("Descripción corta", blank=True)
    imagen_destacada = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Imagen destacada",
    )
    lider = models.CharField("Líder", max_length=255, blank=True)
    horario = models.CharField("Horario de reunión", max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("descripcion"),
        FieldPanel("imagen_destacada"),
        FieldPanel("lider"),
        FieldPanel("horario"),
    ]

    class Meta:  # type: ignore[reportIncompatibleVariableOverride]
        verbose_name = "Ministerio"
        verbose_name_plural = "Ministerios"
        ordering = ["title"]
