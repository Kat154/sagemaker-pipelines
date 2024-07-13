from fastapi import FastAPI
from enum import Enum

app = FastAPI()
@app.get("/")
def root():
    return {"message":"Hello from Fast api"}

print(f'read the file')
if __name__=="__main__":
    app.run()
