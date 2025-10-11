from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import service


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @=== Pydantic Model ===@
class PredictResponse(BaseModel):
    winRate: float
    drawRate: float
    loseRate: float


class PredictRequest(BaseModel):
    home: str
    away: str
    ref_name: str


class Team(BaseModel):
    team_name: str


class Ref(BaseModel):
    ref_name: str


unpack_dict = lambda d, key: round(list(d.get(key).values())[0], 2)


@app.get("/ref")
async def get_ref():
    return service.getRef()


@app.post("/predict")
async def predict(item: PredictRequest):
    home_xg = service.get_xg(item.home)
    away_xg = service.get_xg(item.away)
    pred = service.predict(home_xg, away_xg, item.ref_name)

    prob = {
        "winRate": unpack_dict(pred, "W"),
        "drawRate": unpack_dict(pred, "D"),
        "loseRate": unpack_dict(pred, "L"),
    }

    return prob


@app.get("/teams")
async def get_teams():
    teams = service.get_teams()
    return teams


# @app.get("/teams/xg/{name}")
# async def team_xg(name: str):
#     return service.get_xg(name)
