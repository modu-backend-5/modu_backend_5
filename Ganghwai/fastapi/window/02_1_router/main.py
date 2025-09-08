from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <h1>Hello FastAPI</h1>
    <a href="/docs">Go to Swagger UI</a><br>
    <a href="/redoc">Go to ReDoc</a>
    """


@app.get("/contact", response_class=HTMLResponse)
def contact():
    return """
    <h1>Contact FastAPI</h1>
    <p>FastAPI 연락 정보</p>
    <a href="/">Go to Home</a>
    """


@app.get("/notice", response_class=HTMLResponse)
def notice():
    return """
    <h1>Notice FastAPI</h1>
    <p>FastAPI 공지 정보</p>
    <a href="/">Go to Home</a>
    <ol>
        <li>첫 번째</li>
        <li>두 번째</li>
        <li>세 번째</li>
    </ol>
    """


from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
