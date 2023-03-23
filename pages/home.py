import dash

from components.home.faq import faqs
from components.home.hero import hero
from components.home.top import top
from components.love import love

dash.register_page(__name__, path="/")

layout = [hero, top, faqs, love]
