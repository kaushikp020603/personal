from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        "question": "Where did our very first interaction happen, the one that started everything?",
        "answer": "pbl"
    },
    {
        "question": "When life felt heavy and placements kept breaking me down, who was the only person I opened up to, again and again?",
        "answer": "ankita"
    },
    {
        "question": "What sweet little thing did you buy even before my placement result came out, because you just *knew* I’d get it?",
        "answer": "chocolate"
    },
    {
        "question": "What major milestone did I hit just before my final exams ended — and who *already knew* I’d get it?",
        "answer": "placement"
    },
    {
        "question": "If you had to describe our entire journey — all of it — in just one word, what would that be?",
        "answer": "*"
    }
]

@app.route('/')
def index():
    return redirect(url_for('question', qid=0))

@app.route('/question/<int:qid>', methods=['GET', 'POST'])
def question(qid):
    if qid >= len(questions):
        return redirect(url_for('success'))

    error = None
    if request.method == 'POST':
        user_answer = request.form['answer'].lower().strip()
        correct_answer = questions[qid]["answer"].lower()

        if correct_answer == "*" or user_answer == correct_answer:
            return redirect(url_for('question', qid=qid + 1))
        else:
            error = "Oops! That's not quite right. Try again."

    return render_template('question.html', qid=qid, question=questions[qid]["question"], error=error)

@app.route('/success')
def success():
    return render_template('success.html')
