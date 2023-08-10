from fastapi import FastAPI
from app import models
from app.backend.session import engine

from app.const import (
    OPEN_API_DESCRIPTION,
    OPEN_API_TITLE,
    BASE_API,
)
from app.routers import (
    _healthcheck,
    auth,
    users,
)
from app.version import __version__

app = FastAPI(
    title=OPEN_API_TITLE,
    description=OPEN_API_DESCRIPTION,
    version=__version__,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

models._base.Base.metadata.create_all(bind=engine)

app.mount(BASE_API, app)

app.include_router(_healthcheck.router)
app.include_router(auth.router)
app.include_router(users.router)
