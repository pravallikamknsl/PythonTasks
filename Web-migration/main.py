import concurrent.futures
import subprocess
from streamlit import main as st_main
from flask import Flask,redirect,url_for,render_template

app =Flask(__name__)

def run_streamlit():
    subprocess.run(["streamlit", "run", "streamlit.py"])

@app.route('/')
def welcome():
    return render_template('direct.html')

@app.route('/indirect.html')
def welcome1():
    return render_template('indirect.html')

@app.route('/streamlit')
def streamlit_route():
    with concurrent.futures.ThreadPoolExecutor() as executor:
         executor.submit(run_streamlit)
    return redirect(url_for('direct')) # Redirect back to the index page
if __name__ =='__main__':
    app.run(debug=True)
