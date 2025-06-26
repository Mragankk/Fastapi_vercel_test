from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World from FastAPI on Vercel!"}


# vercel app deployed on- https://fastapivercel-3flnuny2j-mragank-s-projects.vercel.app/
