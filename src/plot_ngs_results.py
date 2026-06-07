import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "reports/ngs_results.csv"
)

mean_support = df[
    "variant_support"
].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    ["Detected Variant"],
    [mean_support]
)

plt.ylabel(
    "Average Variant Support"
)

plt.title(
    "NGS Variant Detection Experiment"
)

plt.tight_layout()

plt.savefig(
    "reports/ngs_experiment.png",
    dpi=300
)

print("Plot saved.")