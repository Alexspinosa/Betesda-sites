# Modelos de Events pages
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class EventPage(Page):
    fecha = models.DateField("Fecha del evento")
    lugar = models.CharField("Lugar", max_length=255, blank=True)
    descripcion = models.TextField("Descripción", blank=True)
    imagen_destacada = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Imagen destacada",
    )

    content_panels = Page.content_panels + [
        FieldPanel("fecha"),
        FieldPanel("lugar"),
        FieldPanel("descripcion"),
        FieldPanel("imagen_destacada"),
    ]

    class Meta:  # type: ignore[reportIncompatibleVariableOverride]
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["-fecha", "lugar"]  # Ordenar por varios campos
        # Primero ordena por fecha descendente
        # Si dos eventos tienen la misma fecha, ordena por lugar alfabéticamente
