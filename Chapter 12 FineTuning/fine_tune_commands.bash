pip install --upgrade openai

export OPENAI_API_KEY="<OPENAI_API_KEY>"

openai tools fine_tunes.prepare_data -f train_data.json

openai api fine_tunes.create -t train_data_prepared.jsonl  -m davinci

openai api fine_tunes.follow -i <YOUR_MODEL_ID>

openai api fine_tunes.list

openai api fine_tunes.get -i <YOUR_MODEL_ID>

openai api fine_tunes.cancel -i <YOUR_MODEL_ID>

curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "prompt": "Secrets Unveiled ->",
    "max_tokens": 30,
    "model": "<YOUR_MODEL_NAME>"}'

openai api models.delete -i <YOUR_MODEL_NAME>
