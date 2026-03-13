# Modelos de home_page
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    titulo_normal = models.CharField("Título normal", max_length=100, blank=True)
    titulo_destacado = models.CharField("Título destacado", max_length=100, blank=True)
    sede_name = models.CharField("Nombre de sede", max_length=255, blank=True, default="Comunidad Cristiana · Central")
    subtitulo = models.CharField("Subtítulo", max_length=255, blank=True)
    boton_texto = models.CharField("Texto del botón", max_length=100, blank=True)
    boton_url = models.URLField("URL del botón", blank=True)
    imagen_hero = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Imagen hero",
    )

    content_panels = Page.content_panels + [
        FieldPanel("titulo_normal"),
        FieldPanel("titulo_destacado"),
        FieldPanel("sede_name"),
        FieldPanel("imagen_hero"),
        FieldPanel("subtitulo"),
        FieldPanel("boton_texto"),
        FieldPanel("boton_url"),
    ]

    class Meta:  # type: ignore
        verbose_name = "Página de inicio"
