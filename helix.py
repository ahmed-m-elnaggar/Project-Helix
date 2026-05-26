import matplotlib.pyplot as plt
import pandas as pd

data = {
    "gene": ["APOE", "APP", "PSEN1", "PSEN2", "BDNF"],
    "healthy": [2.1, 3.4, 1.8, 2.5, 4.2],
    "alzheimers": [5.6, 7.2, 6.1, 5.9, 1.3]
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
plt.show()