
# Modelos de Pages contact
from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey


class RedSocial(Orderable):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="redes_sociales",
    )

    REDES = [
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("youtube", "YouTube"),
        ("twitter", "Twitter"),
        ("tiktok", "TikTok"),
        ("whatsapp", "WhatsApp"),
    ]

    red = models.CharField("Red social", max_length=50, choices=REDES)
    url = models.URLField("URL")

    panels = [
        FieldPanel("red"),
        FieldPanel("url"),
    ]

    def __str__(self):
        return self.get_red_display()


class ContactPage(Page):
    telefono = models.CharField("Teléfono", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)
    direccion = models.CharField("Dirección", max_length=255, blank=True)
    mapa_url = models.URLField("URL de Google Maps", blank=True)
    mensaje = models.TextField("Mensaje adicional", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("telefono"),
        FieldPanel("email"),
        FieldPanel("direccion"),
        FieldPanel("mapa_url"),
        FieldPanel("mensaje"),
        InlinePanel("redes_sociales", label="Redes sociales"),
    ]

    class Meta:  # type: ignore
        verbose_name = "Contacto"
