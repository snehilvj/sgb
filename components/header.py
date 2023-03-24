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
                                            "FAQs on NSE Website",
                                            href="https://m.rbi.org.in/scripts/FAQView.aspx?Id=109",
                                            target="_blank",
                                        ),
                                        dmc.MenuItem(
                                            "Developer",
                                            href="https://www.linkedin.com/in/snehilvj/",
                                            target="_blank",
                                        ),
                                    ]
                                ),
                            ],
                        ),
                        dmc.NavLink(label="Explore", w="auto", href="/explore"),
                    ],
                ),
            ],
        )
    ],
)
