import dash_mantine_components as dmc

faqs = dmc.Container(
    size="md",
    mt=65,
    children=[
        dmc.Text("Frequently asked questions on SGBs", size=30, mb=20, align="center"),
        dmc.AccordionMultiple(
            variant="separated",
            children=[
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("Customization"),
                        dmc.AccordionPanel(
                            "Colors, fonts, shadows and many other parts are customizable to fit your design needs"
                        ),
                    ],
                    value="customization",
                ),
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("Flexibility"),
                        dmc.AccordionPanel(
                            "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
                            "component styles "
                        ),
                    ],
                    value="flexibility",
                ),
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("No annoying focus ring"),
                        dmc.AccordionPanel(
                            "With new :focus-visible pseudo-class focus ring appears only when user navigates with keyboard"
                        ),
                    ],
                    value="focus",
                ),
            ],
        ),
    ],
)
