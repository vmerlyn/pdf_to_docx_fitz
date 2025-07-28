from pathlib import Path
import time


def delete_expired_files(upload_dir: Path, max_age_minutes: int = 10):
    now = time.time()
    expiration_time = max_age_minutes * 60  # seconds

    for file in upload_dir.glob("*"):
        if file.is_file():
            age = now - file.stat().st_mtime
            if age > expiration_time:
                try:
                    file.unlink()
                except Exception as e:
                    print(f"Failed to delete {file}: {e}")
