from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files (CSS, JS, etc.)
app.mount("/content/static/static.css", StaticFiles(directory="static"), name="static")

# Set up HTML templates
templates = Jinja2Templates(directory="templates")

# Home page (frontend)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint to receive data from frontend
@app.post("/submit", response_class=HTMLResponse)
def submit_data(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    result = f"Hello {name}! Your message has been received."
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
print("Directories 'static' and 'templates' created successfully (if they didn't exist).")

