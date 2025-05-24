from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="../templates")

questions = [
    {"question": "The beginning of everything we had, which college subject was it?", "answer": "pbl"},
    {"question": "Where did we first have a deep conversation late at night?", "answer": "instagram"},
    {"question": "What was the name of the album I made with all your saved posts?", "answer": "ankita special"},
    {"question": "What subject did you help me survive without knowing a thing?", "answer": "cn"},
    {"question": "Where did you first say I am your 'important person'?", "answer": "linkedin"},
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/question/<int:qid>', methods=['GET', 'POST'])
def question(qid):
    if qid >= len(questions):
        return redirect(url_for('success'))

    question = questions[qid]["question"]
    answer = questions[qid]["answer"]

    if request.method == 'POST':
        user_answer = request.form["answer"].strip().lower()
        if user_answer == answer:
            return redirect(url_for('question', qid=qid + 1))
        else:
            return render_template("question.html", question=question, qid=qid, error="Try again!")

    return render_template("question.html", question=question, qid=qid)

@app.route('/success')
def success():
    return render_template("success.html")
