from fastapi import FastAPI
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated


import pandas as pd
import pickle


# importing ml model
with open("model/model.pkl") as f:
    model = pickle.load(f)
