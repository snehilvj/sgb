import pandas as pd


def get_bond_with_top_yield():
    data = pd.read_csv("./data/sgb_2023-03-23.csv")
    top = data.sort_values(by="Total Yield to Maturity", ascending=False).iloc[0]
    symbol = top["Symbol"]
    ytm = (top["Total Yield to Maturity"] * 100).round(2)
    fv = top["Fair Value"].round(2)
    discount = (top["Discount to Fair Value"] * 100).round(2)
    ask = "4243.00"
    gold = "2221.00"
    units = 10
    maturity = "Jul 2019"
    return symbol, ytm, fv, discount, ask, gold, units, maturity
