import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_arealand_by_name():
    processed_path = Path("data/processed/dataset.csv")
    df = pd.read_csv(processed_path)

    plt.figure(figsize=(12, 6))
    plt.bar(df["name"], df["arealand_sqmi"], color="steelblue")
    plt.xticks(rotation=90)
    plt.xlabel("Name")
    plt.ylabel("Area Land (sq mi)")
    plt.title("Area Land (sq mi) by Name")
    plt.tight_layout()

    # Save the figure
    output_path = Path("reports/figures/arealand_by_name.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)

    print(f"Chart saved to {output_path}")

if __name__ == "__main__":
    plot_arealand_by_name()