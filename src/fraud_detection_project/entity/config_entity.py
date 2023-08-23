from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    s3_bucket: str
    s3_object_key: Path
    local_data_file: Path