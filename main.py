from fastapi import FastAPI

app = FastAPI()
x = 6
y = 10
print(x + y)

@app.get("/")
def home():
    return {
        "message":"Hello from FastAPI"
    }

print(app)

