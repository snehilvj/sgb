import dash_mantine_components as dmc
from dash_iconify import DashIconify

header = dmc.Header(
    height=70,
    withBorder=False,
    pt=17,
    px=20,
    fixed=True,
    children=[
        dmc.Group(
            position="apart",
            children=[
                dmc.NavLink(label="Home", w="auto", href="/"),
                dmc.Group(
                    position="right",
                    children=[
                        dmc.Menu(
                            trigger="hover",
                            children=[
                                dmc.MenuTarget(
                                    dmc.NavLink(
                                        label="Links",
                                        w="auto",
                                        rightSection=DashIconify(
                                            icon="tabler-chevron-down"
                                        ),
                                    )
                                ),
                                dmc.MenuDropdown(
                                    [
                                        dmc.MenuItem(
                                            "External Link",
                                            href="https://www.github.com/snehilvj",
                                            target="_blank",
                                        ),
                                        dmc.MenuItem(
                                            "NSE Website",
                                            href="https://www.github.com/snehilvj",
                                            target="_blank",
                                        ),
                                    ]
                                ),
                            ],
                        ),
                        dmc.NavLink(label="Explore", w="auto", href="/explore"),
                        dmc.NavLink(label="Resources", w="auto", href="/resources"),
                    ],
                ),
            ],
        )
    ],
)
