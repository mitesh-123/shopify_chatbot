from flask import Flask, request, render_template, redirect, url_for, send_file,make_response
from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
import os
import pymysql
from langchain.sql_database import SQLDatabase
import openai

project_root = os.path.dirname(os.path.realpath('__file__'))
static_path = os.path.join(project_root, 'app/static')
app = Flask(__name__, template_folder= 'templates')
context_set = ""

OPENAI_API_KEY=""
openai.api_key = OPENAI_API_KEY

db = SQLDatabase.from_uri("mysql+pymysql://root:shashikant420@localhost/hospital")
# db = SQLDatabase.from_uri("mysql+pymysql://avnadmin:AVNS_CZrlqhxcMzaiKVVTWwp@mysql-12c605c0-bhawna-aeb3.a.aivencloud.com/defaultdb")
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0, verbose=True)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

class ProductNotFoundError(Exception):
    pass

@app.route('/')
def hello_world():
    return render_template('index.html') 

@app.route('/general')
def general():
    return render_template('general.html')

@app.route('/answers',methods=['GET', 'POST'])
def answers():
    question = request.form.get("question")
    try:
        result = db_chain.run(question)
        if not result:
            raise ProductNotFoundError("Product not found in the database.")
    except ProductNotFoundError as pnf_error:
        result = str(pnf_error)
    except Exception as e:
        result = "An error occurred. Please try again later."
    return result

@app.route('/general_answer', methods=['GET', 'POST'])
def generate_response():
    if request.method == 'POST':
        model = "text-davinci-003"
        user = request.form['general_question']

        if "exit" in user:
            return "Goodbye!"

        completion = openai.Completion.create(
            model=model,
            prompt=user,
            max_tokens=1024,
            temperature=0.5,
            n=1,
            stop=None
        )
        
        response = completion.choices[0].text
        return response

# data = answers()
# print(data)

if __name__ == '__main__':
    app.run(debug=True)