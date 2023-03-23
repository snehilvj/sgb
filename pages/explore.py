import dash

from components.home.top import top

dash.register_page(__name__, path="/explore")

layout = [top]
