from pathlib import Path

def open_file(path:str) -> list:
    """Returns file contents as list of dicts."""


    file_to_open = Path(path)
    rows = None

    with open(file_to_open) as f:
        rows = f.readlines()

    if not rows: return None

    rows_list = [r.split(',') for r in rows]
        
    return rows_list


def save_to_db(model, data):
    pass
