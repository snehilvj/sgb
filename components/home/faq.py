import dash_mantine_components as dmc

questions = [
    {
        "question": "What is an SGB?",
        "answer": "Sovereign Gold Bonds (SGBs) are government securities denominated in grams of gold. They are "
                  "issued by the Reserve Bank of India (RBI) on behalf of the Government of India. SGBs offer an "
                  "alternative to holding physical gold as an investment.",
    },
    {
        "question": "How do I invest in SGBs?",
        "answer": "Investors can invest in SGBs through brokers, banks, designated post offices, and Stock Holding "
                  "Corporation of India Limited (SHCIL) as well as through various online platforms. The minimum "
                  "investment in SGBs is 1 gram of gold, and the maximum investment limit is 4 kg for individuals and "
                  "Hindu Undivided Families (HUFs) and 20 kg for trusts and similar entities.",
    },
    {
        "question": "What are the benefits of investing in SGBs?",
        "answer": "SGBs offer a range of benefits such as protection against the risk of loss or theft associated "
                  "with physical gold, regular interest income at the rate of 2.50% per annum, exemption from capital "
                  "gains tax on redemption, and liquidity through listing on exchanges.",
    },
    {
        "question": "How are SGB prices determined?",
        "answer": "The prices of SGBs are determined based on the prevailing market price of gold at the time of "
                  "issuance. The RBI sets the issue price of SGBs in consultation with market participants. The "
                  "prices of SGBs are also subject to changes based on fluctuations in the market price of gold.",
    },
    {
        "question": "Can SGBs be traded on the stock exchange?",
        "answer": "Yes, the bonds are tradeable from a date notified by the RBI. It may be noted that only bonds held "
                  "in de-mat form with depositories can be traded in stock exchanges. The bonds can also be sold and "
                  "transferred as per provisions of Government Securities Act, 2006.",
    },
]

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
                        dmc.AccordionControl(q["question"]),
                        dmc.AccordionPanel(q["answer"]),
                    ],
                    value=q["question"],
                )
                for q in questions
            ],
        ),
    ],
)
