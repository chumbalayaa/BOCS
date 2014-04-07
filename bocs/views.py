from bocs import app

@app.route('/')
def index():
  return "Hello Bocs"
