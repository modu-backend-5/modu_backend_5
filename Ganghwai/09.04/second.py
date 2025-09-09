from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/",response_class=HTMLResponse)
def index():
    return "<h1> 오늘은 비가오니까 꿉꿉하다 </h1>" 


"""
get /about -> h2 태그활용
get /notice -> h3 태그활용
get /contact -> h4 태그활용

"""


@app.get("/about",response_class=HTMLResponse)
def about():
    return "<h2> 오늘은 비가오니까 꿉꿉하다 </h2>"

@app.get("/notice",response_class=HTMLResponse)
def notice():
    return "<h3> 안녕하세요 백엔드 개발자입니다. </h3>"

@app.get("/contact",response_class=HTMLResponse)
def contact():
    return "<h4> 이메일은 gyeonghwan02@gmail.com 입니다. </h4>"

@app.get("/index", response_class=HTMLResponse)
def index2():
    return """
    <h1>hello world 1</h1>
    <p>안녕</p>
    <ol>
        <li>첫 번째</li>
        <li>두 번째</li>
        <li>세 번째</li>
    </ol>
    """
from fastapi import Request
from fastapi.templating import Jinja2Templates # 템플릿 연동

templates = Jinja2Templates("templates") # 템플릿 위치 설정


@app.get("/home")
def home(request:Request,): # 첫번째 인자에는 반드시 넣어야함.
    return templates.TemplateResponse(request, "index.html", {"name":"max","good": "okay"})



@app.get("/me")
def home(request:Request,): # 첫번째 인자에는 반드시 넣어야함.
    return templates.TemplateResponse(request, "home.html", {"안녕하세요":"웅이입니다","하이": "너무더워"})