from typing import Sequence

import pandas as pd
from interfaces.extractor import DataExtractorBase
from interfaces.transform import DataTransformBase


class DataIngestor:
    """ETL pipeline to ingest, transform and load extracted data into parquet files"""

    def __init__(
        self,
        append_mode: str,
        data_extractors: Sequence[DataExtractorBase],
        dataclass: type,
        save_path: str,
        data_transforms: Sequence[DataTransformBase] = [],
    ):
        pass

    def _extract(self) -> pd.DataFrame:
        pass

    def _transform(self, data: pd.DataFrame):
        pass

    def _load(self, data: pd.DataFrame):
        pass

    def ingest(self):
        """ETL to parquet"""
        extracted_data = self._extract()
        transformed_data = self._transform(extracted_data)
        self._load(transformed_data)
