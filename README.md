# RasaChatBot
Using rasa..
## Step
### Step 1 - spacy
go to `https://github.com/howl-anderson/Chinese_models_for_SpaCy/releases`
download Chinese model.
`pip install zh_core_web_sm-2.0.5.tar.gz`
inorder to use this model in rasa, we have to link it.
`python -m spacy link zh_core_web_sm zh`
Industrial-Strength Natural Language Processing
### Step 2 - rasa-nlu-trainer
`npm install -g rasa-nlu-trainer`
make it easier to generate examokes and data annotations.
