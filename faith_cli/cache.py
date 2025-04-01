import json
from pathlib import Path

cache_file = Path(__file__).parent.parent /data/cache.json

def load_cache():
    if cache_file.exists():
        
        with open(cache_file, "r") as f:
            return json.load(f)
    return {}
        