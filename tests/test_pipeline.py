import pandas as pd
from pathlib import Path
import pipeline


def test_run_pipeline_creates_features(tmp_path: Path):
    # Create a small sample dataset
    sample = pd.DataFrame({
        'patient': ['P1', 'P1', 'P2', 'P2'],
        'channel': ['FP1', 'FP2', 'FP1', 'FP2'],
        'delta_bp': [1.0, 2.0, 3.0, 4.0],
        'theta_bp': [5.0, 6.0, 7.0, 8.0],
        'alpha_bp': [9.0, 10.0, 11.0, 12.0],
        'beta_bp': [13.0, 14.0, 15.0, 16.0],
        'gamma_bp': [17.0, 18.0, 19.0, 20.0],
    })

    csv_file = tmp_path / 'sample.csv'
    sample.to_csv(csv_file, index=False)

    out_dir = tmp_path / 'out'
    output_file = pipeline.run_pipeline(csv_file, out_dir)

    assert output_file.exists(), 'patient_features.csv was not created'

    df = pd.read_csv(output_file)
    expected_cols = [
        'delta_bp_FP1',
        'delta_bp_FP2',
        'theta_bp_FP1',
        'theta_bp_FP2',
        'alpha_bp_FP1',
        'alpha_bp_FP2',
        'beta_bp_FP1',
        'beta_bp_FP2',
        'gamma_bp_FP1',
        'gamma_bp_FP2',
    ]
    for col in expected_cols:
        assert col in df.columns
