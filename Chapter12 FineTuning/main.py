import time
from openai import OpenAI
client = OpenAI(api_key="[YOUR_API_KEY]")

file = client.files.create(
    file=open("train_data_prepared.jsonl", "rb"),
    purpose="fine-tune"
)
print(file)
tuned_model = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
)
print(tuned_model)

job = client.fine_tuning.jobs.retrieve(tuned_model.id)
print(job.status)
while job.status != "succeeded":
    job = client.fine_tuning.jobs.retrieve(tuned_model.id)
    print(job.status)
    time.sleep(5)
print(job.fine_tuned_model)

completion = client.chat.completions.create(
    model=job.fine_tuned_model,
    messages=[
        {"role": "user", "content": "The Adventure Begins ->"}
    ]
)
print(completion.choices[0].message.content)


client.models.delete(job.fine_tuned_model)
