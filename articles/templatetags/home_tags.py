from django import template
from articles.models import FooterPage

register = template.Library()


@register.inclusion_tag("home/tags/footer_page_list.html", takes_context=True)
def footer_pages(context):
    pages = []
    request = context["request"]
    site = request._wagtail_site
    if site:
        pages = FooterPage.objects.descendant_of(site.root_page)

    return {
        "request": request,
        "footers": pages,
    }


@register.simple_tag(takes_context=True)
def get_next_article(context, article):
    return (
        article.specific.get_siblings(False)
        .filter(path__gte=article.path, live=True, content_type=8)
        .order_by("path")
        .first()
    )
