import pandas as pd
from pathlib import Path


def run_pipeline(csv_path: Path | str, output_dir: Path | str) -> Path:
    """Process `csv_path` and write patient features to `output_dir`.

    The input CSV must contain columns:
    `patient`, `channel`, `delta_bp`, `theta_bp`, `alpha_bp`, `beta_bp`, `gamma_bp`.
    The output CSV `patient_features.csv` will contain one row per patient and
    band-power features pivoted by channel.
    """
    csv_path = Path(csv_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_path)
    required_cols = {
        "patient",
        "channel",
        "delta_bp",
        "theta_bp",
        "alpha_bp",
        "beta_bp",
        "gamma_bp",
    }
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in input CSV: {missing}")

    pivot = df.pivot_table(
        index="patient",
        columns="channel",
        values=["delta_bp", "theta_bp", "alpha_bp", "beta_bp", "gamma_bp"],
    )
    pivot.columns = [f"{band}_{ch}" for band, ch in pivot.columns]
    pivot.reset_index(inplace=True)

    out_file = output_dir / "patient_features.csv"
    pivot.to_csv(out_file, index=False)
    return out_file


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run EEG processing pipeline")
    parser.add_argument("csv_path", help="Path to input sample EEG CSV")
    parser.add_argument("output_dir", help="Directory to write outputs")
    args = parser.parse_args()
    run_pipeline(args.csv_path, args.output_dir)
