from fastapi import FastAPI # pyright: ignore
from .core.configs import DEBUG_MODE


app = FastAPI(DEBUG_MODE)
