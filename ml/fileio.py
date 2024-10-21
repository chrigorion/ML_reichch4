from pathlib import Path

def ensure_dir(path):
    """Create a dir recursively if it doesn't exist. 
    Returns True if the folder exists or was created."""
    path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True, exist_ok=True)
    return path.is_dir()

