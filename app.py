from pathlib import Path

from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

MODEL_PATH = Path(__file__).resolve().parent / "ner_model"
nlp = None

if MODEL_PATH.exists():
    try:
        nlp = spacy.load(MODEL_PATH)
    except Exception:
        nlp = None


def extract_entities(text):
    if nlp is None:
        return [], "Model not found. Run the training notebook first."

    doc = nlp(text)
    entities = [
        {
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start_char,
            "end": ent.end_char,
        }
        for ent in doc.ents
    ]
    return entities, None


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    entities = []
    error = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            entities, error = extract_entities(text)
        else:
            error = "Please enter some text."

    return render_template(
        "index.html",
        text=text,
        entities=entities,
        error=error,
        model_ready=nlp is not None,
    )


if __name__ == "__main__":
    app.run(debug=True)
