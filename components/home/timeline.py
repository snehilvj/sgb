import dash_mantine_components as dmc

timeline = dmc.Center(
    dmc.Timeline(
        active=-1,
        w=350,
        mt=40,
        bulletSize=40,
        color="indigo",
        lineWidth=2,
        styles={
            "item": {"padding-left": 40},
        },
        children=[
            dmc.TimelineItem(
                title="Apply to an open series",
                bullet="1",
                children=[
                    dmc.Text(
                        "SGBs will be credited to your demat account.",
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Space(h=25),
                ],
            ),
            dmc.TimelineItem(
                title="Earn interest while you hold",
                bullet="2",
                children=[
                    dmc.Text(
                        "Receive 2.5% interest per annum (paid semi-annually)",
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Space(h=25),
                ],
            ),
            dmc.TimelineItem(
                title="Enjoy tax-free maturity",
                bullet="3",
                children=[
                    dmc.Text(
                        "SGBs mature after 8 years. However, you can redeem anytime after 5 years.",
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Space(h=25),
                ],
            ),
        ],
    )
)
