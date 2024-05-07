from abc import ABC, abstractmethod

import pandas as pd


class DataTransformBase(ABC):
    """Base class for data transforms applied as a part of the ETL pipeline."""

    @abstractmethod
    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
        """Logic for transform to apply to dataset"""
        raise NotImplementedError
