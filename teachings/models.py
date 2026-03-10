
# Modelos de Pages teachings
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Categoria(models.Model):
    nombre = models.CharField("Nombre", max_length=100)

    panels = [
        FieldPanel("nombre"),
    ]

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]


class TeachingPage(Page):
    fecha = models.DateField("Fecha")
    predicador = models.CharField("Predicador", max_length=255, blank=True)
    tema = models.CharField("Tema", max_length=255, blank=True)
    categoria = models.ForeignKey(
        Categoria,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="ensenanzas",
        verbose_name="Categoría",
    )
    imagen_destacada = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Imagen destacada",
    )
    video_url = models.URLField("URL del video", blank=True)
    descripcion = models.TextField("Descripción", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("fecha"),
        FieldPanel("predicador"),
        FieldPanel("tema"),
        FieldPanel("categoria"),
        FieldPanel("imagen_destacada"),
        FieldPanel("video_url"),
        FieldPanel("descripcion"),
    ]

    class Meta:  # type: ignore
        verbose_name = "Enseñanza"
        verbose_name_plural = "Enseñanzas"
        ordering = ["-fecha"]
