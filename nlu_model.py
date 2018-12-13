from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
import json

def train_nlu(data, configs, model_dir):
  training_data = load_data(data)
  trainer = Trainer(config.load(configs))
  trainer.train(training_data)
  model_directory = trainer.persist(model_dir, fixed_model_name = 'criminalnlu')

def run_nlu():
  interpreter = Interpreter.load('./models/nlu/default/criminalnlu/')
  print(interpreter.parse("张青红何时出生"))

if __name__ == '__main__':
  # train_nlu('./data/data.json', './config/config.yml', './models/nlu')
  run_nlu()
