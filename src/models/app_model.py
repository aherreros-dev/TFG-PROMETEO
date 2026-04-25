from dataclasses import dataclass, field
import pandas as pd


@dataclass
class AppModel:
    """Central application state. Passed to controllers; never touched directly by views."""
    dataset: pd.DataFrame = field(default_factory=pd.DataFrame)
    model_name: str = ""
    hyperparams: dict = field(default_factory=dict)
    trained_model: object = None
    metrics: dict = field(default_factory=dict)
