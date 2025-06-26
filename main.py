from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World from FastAPI on Vercel!"}


# vercel app deployed on- https://fastapi-vercel-test-chq45dns7-mragank-gautams-projects.vercel.app
