import pandas as pd

scheme_df = pd.read_csv("../data/processed/scheme_performance_clean.csv")
sharpe_df = pd.read_csv("../reports/sharpe_ratio.csv")

recommend_df = scheme_df.merge(
    sharpe_df,
    on="amfi_code"
)

def recommend_funds(risk):

    result = (
        recommend_df[
            recommend_df["risk_grade"] == risk
        ]
        .sort_values(
            "Sharpe_Ratio",
            ascending=False
        )
        [
            [
                "scheme_name",
                "fund_house",
                "Sharpe_Ratio",
                "return_3yr_pct"
            ]
        ]
        .head(3)
    )

    return result


print(recommend_funds("Moderate"))