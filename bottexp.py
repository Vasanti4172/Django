from bottle import Bottle, run 
app = Bottle()

@app.route('/')
def home_page(): 
    return 'Experience this bottle webpage.'

if __name__ == '__main__': 
    run(app, host='localhost', port=8082)