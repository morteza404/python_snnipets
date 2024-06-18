import json
import os

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import requests

# Set the URL of your SonarQube instance
sonarqube_url = "http://172.19.0.1:9000"

# Set the username and password
username = "admin"

password = "123"

# Define the API endpoints
api_measures_component = "/api/measures/component_tree"


# Retrieve the measures for the component
params = {
    "asc": "false",
    "component": "smartlab_monster-saghi_AYpaDljB2WLPeXyeNYDj",
    "metricKeys": "complexity,sqale_index,sqale_debt_ratio,ncloc,reliability_remediation_effort",
    "metricSort": "sqale_debt_ratio",
    "metricSortFilter": "withMeasuresOnly",
    "ps": 500,
    "s": "metric",
    "strategy": "leaves",
}

response = requests.get(
    sonarqube_url + api_measures_component, auth=(username, password), params=params
)

if response.status_code != 200:
    print("Failed to retrieve measures for component:", response.content)
    exit()

measures = json.loads(response.content)

print(measures)

cmap = matplotlib.colormaps["RdYlGn"].reversed()
matplotlib.rcParams.update({"font.size": 20})


measures_df = pd.json_normalize(
    measures["components"], record_path=["measures"], meta=["path"]
)

# Use pivot to create a new column for each metric
measures_df = measures_df.pivot(index=["path"], columns="metric", values="value")

# Reset the index to make the key columns regular columns
measures_df = measures_df.reset_index()
measures_df.dropna(subset=["complexity"], inplace=True)

measures_df["complexity"] = pd.to_numeric(measures_df["complexity"])
measures_df["sqale_debt_ratio"] = pd.to_numeric(measures_df["sqale_debt_ratio"])
measures_df["sqale_index"] = pd.to_numeric(measures_df["sqale_index"])
measures_df["reliability_remediation_effort"] = pd.to_numeric(
    measures_df["reliability_remediation_effort"]
)
measures_df["ncloc"] = pd.to_numeric(measures_df["ncloc"])


mask = (
    (measures_df["complexity"] >= 10)
    & (measures_df["sqale_debt_ratio"] >= 0.1)
    & (measures_df["path"].str.startswith("swift/"))
)


measures_df = measures_df.loc[mask]


def create_scatter_plot(x_param, y_param, size_param, color_param, fname):
    x_param_metric, x_param_name = x_param
    y_param_metric, y_param_name = y_param
    size_param_metric, size_param_name = size_param
    color_param_metric, color_param_name = color_param

    data = measures_df.nlargest(15, color_param_metric)

    # Create the scatter plot
    fig, ax = plt.subplots(figsize=(40, 20))
    sc = ax.scatter(
        data[x_param_metric],
        data[y_param_metric],
        s=20000 * data[size_param_metric],
        alpha=0.5,
        c=data[color_param_metric],
        cmap=cmap,
    )

    cbar = plt.colorbar(sc)

    for i, row in data.iterrows():
        font_size = (
            12 * row[size_param_metric]
        )  # Set the font size based on the circle ratio
        bbox = dict(
            facecolor="white", alpha=0.5, edgecolor="none"
        )  # Add a background rectangle behind the text
        x, y = row[x_param_metric], row[y_param_metric]
        ann = ax.annotate(
            row["path"],
            xy=(x, y),
            ha="center",
            va="center",
            fontsize=font_size,
            bbox=bbox,
        )

    # Set the axis labels and title
    ax.set_xlabel(x_param_name)
    ax.set_ylabel(y_param_name)
    ax.set_title("Code with High Interest Rates")

    fig.savefig(f"{fname}.pdf", dpi=300)


# Call the function with the desired parameter names and data
create_scatter_plot(
    ("complexity", "Cyclomatic Complexity"),
    ("sqale_index", "Technical Debt"),
    ("sqale_debt_ratio", "Technical debt ratio"),
    ("sqale_debt_ratio", "Technical debt ratio"),
    "maintainability",
)
create_scatter_plot(
    ("ncloc", "Lines of Code"),
    ("reliability_remediation_effort", "Reliability remediation effort"),
    ("sqale_debt_ratio", "Technical debt ratio"),
    ("reliability_remediation_effort", "Reliability remediation effort"),
    "reliability",
)


print("hello")
