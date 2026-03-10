
# Modelos de  Pages donations
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class MetodoPago(models.Model):
    METODOS = [
        ("transferencia", "Transferencia Bancaria"),
        ("nequi", "Nequi"),
        ("daviplata", "Daviplata"),
        ("pse", "PSE"),
        ("efectivo", "Efectivo"),
    ]

    nombre = models.CharField(
        "Método de pago",
        max_length=50,
        choices=METODOS,
    )
    numero_cuenta = models.CharField("Número de cuenta", max_length=255, blank=True)
    titular = models.CharField("Titular", max_length=255, blank=True)
    descripcion = models.TextField("Descripción", blank=True)
    imagen = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Imagen o logo",
    )

    panels = [
        FieldPanel("nombre"),
        FieldPanel("numero_cuenta"),
        FieldPanel("titular"),
        FieldPanel("descripcion"),
        FieldPanel("imagen"),
    ]

    def __str__(self):
        return self.get_nombre_display()

    class Meta:
        verbose_name = "Método de pago"
        verbose_name_plural = "Métodos de pago"


class DonationPage(Page):
    introduccion = models.TextField("Introducción", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduccion"),
    ]

    class Meta:  # type: ignore
        verbose_name = "Donaciones"
