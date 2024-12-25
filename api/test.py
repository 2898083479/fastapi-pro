from main import app
from test1 import app as app1

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
    uvicorn.run(app1, port=8001)

