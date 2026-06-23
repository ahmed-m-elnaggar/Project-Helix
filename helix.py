import matplotlib.pyplot as plt
import pandas as pd

data = {
    "gene": ["APOE", "APP", "PSEN1", "PSEN2", "BDNF", "SOX2", "PAX6", "NEUROG2", "MAP2"],
    "healthy": [2.1, 3.4, 1.8, 2.5, 4.2, 5.1, 4.8, 3.9, 4.5],
    "alzheimers": [5.6, 7.2, 6.1, 5.9, 1.3, 1.8, 2.1, 1.5, 1.9]
}

df = pd.DataFrame(data)
df["difference"] = df["alzheimers"] - df["healthy"]

df["difference"] = df["alzheimers"] - df["healthy"]
most_disrupted = df.sort_values("difference", ascending=False)

threshold = 2.0
significant = df[df["difference"].abs() > threshold]
x = df["gene"]
y_healthy = df["healthy"]
y_alzheimers = df["alzheimers"]

plt.figure(figsize=(10, 6))
plt.plot(x, y_healthy, marker="o", label="Healthy", color="blue")
plt.plot(x, y_alzheimers, marker="o", label="Alzheimer's", color="red")
plt.title("Gene Expression: Healthy vs Alzheimer's")
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.legend()

x = range(len(df["gene"]))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x, df["healthy"], width, label="Healthy", color="blue")
bars2 = ax.bar([i + width for i in x], df["alzheimers"], width, label="Alzheimer's", color="red")

ax.set_title("Gene Expression: Healthy vs Alzheimer's")
ax.set_xlabel("Gene")
ax.set_ylabel("Expression Level")
ax.set_xticks([i + width/2 for i in x])
ax.set_xticklabels(df["gene"])
ax.legend()

plt.tight_layout()
plt.savefig("gene_expression_chart.png", dpi=300, bbox_inches="tight")
plt.show()