import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


DATABASE_URL = os.getenv("DATABASE_URL")

ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS").split(",")


if not DATABASE_URL:
    raise ValueError(
        f"DATABASE_URL is not set. Checked: {BASE_DIR / '.env'}"
    )