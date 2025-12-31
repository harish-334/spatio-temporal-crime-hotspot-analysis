from pathlib import Path
import sys

def load_paths(current_notebook_path: Path):
    """
    Determines project paths based on the location of the current notebook.
    Adds utils/ to system path.
    Returns all directory paths.
    """

    project_root = current_notebook_path.parent.parent

    raw_dir = project_root / "data"
    parquet_dir = project_root / "data_parquet"
    processed_dir = project_root / "data_processed"
    models_dir = project_root / "models"
    logs_dir = project_root / "logs"
    utils_dir = project_root / "utils"

    # Add utils/ for imports
    if str(utils_dir) not in sys.path:
        sys.path.append(str(utils_dir))

    # Return all paths in a dictionary
    return {
        "PROJECT_ROOT": PROJECT_ROOT,
        "raw_dir": raw_dir,
        "parquet_dir": parquet_dir,
        "processed_dir": processed_dir,
        "models_dir": models_dir,
        "logs_dir": logs_dir,
        "utils_dir": utils_dir,
    }
