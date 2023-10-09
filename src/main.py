from fastapi import FastAPI

from routers import recipe

app = FastAPI()
app.include_router(recipe.router)
