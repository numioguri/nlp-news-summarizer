from flask import Flask, render_template, request
from translate import translate_text
from summarize import summarize_text
from evaluate import evaluate_summary

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    summary = ""
    rouge_score = ""
    bleu_score = ""

    if request.method == 'POST':
        original_text = request.form['news']
        translated_text = translate_text(original_text)
        summary = summarize_text(translated_text)
        rouge_score, bleu_score = evaluate_summary(translated_text, summary)

    return render_template('index.html',
                           translated_text=translated_text,
                           summary=summary,
                           rouge=rouge_score,
                           bleu=bleu_score)

if __name__ == '__main__':
    app.run(debug=True)
