from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This is the "Magic" part that fixes the white screen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This allows any website to talk to your backend
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Brain Initialized & Ready for Queries"}
