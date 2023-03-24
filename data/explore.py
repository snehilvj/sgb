import pandas as pd


def get_data_for_explore_section():
    data = pd.read_csv("./data/sgb_2023-03-23.csv")
    cols = [
        "Symbol",
        "Issue Price",
        "Maturity Date",
        "Years To Maturity",
        "Interest Value",
        "Present Value of Future Interest Payments",
        "Fair Value",
        "Ask Price",
        "Average Trading Volume",
        "Discount to Fair Value",
        "Discount to Gold Price",
        "Total Yield to Maturity",
    ]
    data = data[cols]
    data['Discount to Gold Price'] *= 100
    data['Discount to Fair Value'] *= 100
    data['Total Yield to Maturity'] *= 100
    data = data.round(2)

    return data
# dark = #1a1b1e
# light = #25262b;