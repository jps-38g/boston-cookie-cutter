import pandas as pd
from pathlib import Path
from loguru import logger
from tqdm import tqdm
import typer

from boston_cookie_cutter.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()

@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
):
    logger.info(f"Reading data from {input_path}...")
    df = pd.read_csv(input_path)

    logger.info("Cleaning data: Selecting columns...")
    df_clean = df[["name", "year", "arealand_sqmi"]]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(output_path, index=False)

    logger.success(f"Processing complete. Saved to {output_path}")


def run():
    app()


if __name__ == "__main__":
    run()