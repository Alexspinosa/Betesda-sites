
# Modelos del Menu Principal
from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


@register_snippet
class Menu(ClusterableModel):
    titulo = models.CharField("Título", max_length=255)
    slug = models.SlugField(unique=True)

    panels = [
        FieldPanel("titulo"),
        FieldPanel("slug"),
        InlinePanel("menu_items", label="Items del menú"),
    ]

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Menú"
        verbose_name_plural = "Menús"


class MenuItem(Orderable):
    menu = ParentalKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="menu_items",
    )
    titulo = models.CharField("Título", max_length=255)
    link_page = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Página interna",
    )
    link_url = models.URLField("URL externa", blank=True)
    abrir_en_nueva_pestana = models.BooleanField(
        "Abrir en nueva pestaña", default=False
    )

    panels = [
        FieldPanel("titulo"),
        FieldPanel("link_page"),
        FieldPanel("link_url"),
        FieldPanel("abrir_en_nueva_pestana"),
    ]

    def __str__(self):
        return self.titulo

    def get_url(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url or "#"
