# Named Entity Recognition (NER)

A practical Natural Language Processing project that extracts **PERSON**, **LOCATION**, and **ORGANIZATION** entities from raw text.

The project uses **spaCy**, **sequence labeling**, and **IOB tagging**. It includes Jupyter notebooks for dataset exploration, model training, and evaluation, plus a small Flask web app so the trained model can be demonstrated in interviews.

## Project Highlights

- Open-source **CoNLL-2003** dataset
- IOB/IOB2 entity-tagging concepts
- spaCy `EntityRecognizer`
- Custom NER model trained from scratch
- Precision, recall and F1 evaluation
- Confusion-style entity-level analysis
- Flask web application for live predictions
- Simple repository structure with no `src/` folder
- GitHub and LinkedIn profile links in the web app

## Dataset

The notebooks use the open-source **CoNLL-2003** NER dataset through the Hugging Face `datasets` library.

Main entity classes used in this project:

- `PER` → PERSON
- `LOC` → LOCATION
- `ORG` → ORGANIZATION

The dataset also contains `MISC`; this project intentionally focuses on the three entity categories most useful for the demonstration.

## Repository Structure

```text
Named-Entity-Recognition-NER/
│
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_train_ner_model.ipynb
│   └── 03_evaluate_ner_model.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
├── app.py
├── requirements.txt
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

## How to Run

### 1. Create an environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the notebooks in order

1. `01_dataset_exploration.ipynb`
2. `02_train_ner_model.ipynb`
3. `03_evaluate_ner_model.ipynb`

The training notebook saves the trained spaCy pipeline into:

```text
ner_model/
```

That folder is generated locally and is intentionally ignored by Git because trained model artifacts can be large.

### 4. Start the Flask app

```bash
python app.py
```

Then open the local address shown by Flask.

## Example

Input:

```text
Apple CEO Tim Cook visited London to meet government officials.
```

The application can identify entities such as:

```text
Apple      → ORGANIZATION
Tim Cook   → PERSON
London     → LOCATION
```

## Interview Talking Points

This project demonstrates:

- What Named Entity Recognition is
- Sequence labeling at token level
- IOB tagging (`B-`, `I-`, `O`)
- How raw annotations are converted into spaCy training examples
- Why entity boundaries matter
- Training a statistical NLP model
- Evaluating NER using precision, recall and F1
- Serving an NLP model through Flask
- Separating experimentation in notebooks from the user-facing application

## Profiles

**GitHub:** https://github.com/InfinitePraveen

**LinkedIn:** https://www.linkedin.com/in/infinitepraveen/

## License

This project is intended for learning, portfolio and interview demonstration purposes. Dataset licensing and terms remain with the original dataset providers.
