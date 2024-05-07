from abc import ABC, abstractmethod

import pandas as pd


class DataExtractorBase(ABC):
    """Base class to extract data from a source"""

    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        raise NotImplementedError

    @abstractmethod
    def get_mapper(self) -> dict:
        """Gets dict to map source data columns to target"""
        raise NotImplementedError

    @abstractmethod
    def id_string(self) -> str:
        """Returns string identifier for dataset source"""
        raise NotImplementedError
