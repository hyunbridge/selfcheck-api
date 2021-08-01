from fastapi import FastAPI, status
from pydantic import BaseModel

import aiohttp
import hcskr

import uvicorn

app = FastAPI()


class SelfCheckUser(BaseModel):
    name: str
    birth: str
    school_area: str
    school_name: str
    school_level: str
    password: str


@app.post("/validate-user/")
async def validate_user(user: SelfCheckUser):
    async with aiohttp.ClientSession() as session:
        result = await hcskr.asyncUserLogin(user.name, user.birth, user.school_area, user.school_name,
                                            user.school_level, user.password, session)
    return result


@app.post("/self-check/")
async def self_check(user: SelfCheckUser):
    result = await hcskr.asyncSelfCheck(user.name, user.birth, user.school_area, user.school_name, user.school_level,
                                        user.password)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
