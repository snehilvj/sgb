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
                                            "Developer",
                                            icon=DashIconify(
                                                icon="radix-icons:github-logo", width=16
                                            ),
                                            href="https://www.linkedin.com/in/snehilvj/",
                                            target="_blank",
                                        ),
                                        dmc.MenuDivider(),
                                        dmc.MenuLabel("Inspiration"),
                                        dmc.MenuItem(
                                            "SGB Analyzer",
                                            icon=dmc.Image(
                                                src="/assets/sgb-analyzer.png", width=16
                                            ),
                                            href="https://sgbanalyzer.com/home",
                                            target="_blank",
                                        ),
                                        dmc.MenuItem(
                                            "Wint Wealth",
                                            icon=dmc.Image(
                                                src="/assets/wint.png", width=16
                                            ),
                                            href="https://sgb.wintwealth.com",
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
