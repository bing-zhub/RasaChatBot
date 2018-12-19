## nlu_train
` python -m rasa_nlu.train --config config/config.yml --data data/data.json --path ./models --project CriminalMiner --fixed_model_name nlu`

## nlu_run
`python -m rasa_nlu.server --path ./models/`

## core_train
` python -m rasa_core.train -s data/stories.md -d data/criminal_domain.yml -o models/dialogue`

## core_run
`python -m rasa_core.run -d models/dialogue -u CriminalMiner/nlu --port 5002 --credentials credentials.yml --cors * --endpoints endpoints.yml`

## action_run
` python -m rasa_core_sdk.endpoint --actions actions`

## interactive_train
` python -m rasa_core.train interactive -s data/stories.md -d data/criminal_domain.yml --nlu CriminalMiner/nlu -o models/dialogue --endpoints endpoints.yml`

## nlu_test
` curl -XPOST localhost:5000/parse -d '{"q":"你好", "project":"CriminalMiner","model":"nlu"}'`
