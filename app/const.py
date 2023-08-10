import os
from enum import Enum
from typing import (
    Final,
    List,
)

# Open API parameters
OPEN_API_TITLE: Final = "Chat API"
OPEN_API_DESCRIPTION: Final = "API for the chat application"

# Authentication service constants
AUTH_TAGS: Final[List[str | Enum] | None] = ["Authentication"]
AUTH_URL: Final = "auth"

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

BASE_API = "/api/v1"
