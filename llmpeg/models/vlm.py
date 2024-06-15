from dataclasses import dataclass
from pathlib import Path

from llmpeg.capabilities.filesystem import ImgVec

# TODO: https://huggingface.co/blog/vlms
@dataclass
class VLM:
    cache_dir: Path
    model_name: str = 'vlm'

    def __post_init__(self):
        self.cache_dir = self.cache_dir / 'models'
        self.cache_dir.mkdir(exist_ok=True, parents=True)
        self._setup()

    def _setup(self):
        return

    def generate(self, query: str, image: ImgVec) -> str:
        return ""
