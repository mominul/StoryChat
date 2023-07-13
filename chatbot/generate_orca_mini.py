local_path = (
    "/Users/mominul/Downloads/orca-mini-3b.ggmlv3.q4_0.bin"
)

# import requests

# from pathlib import Path
# from tqdm import tqdm

# Path(local_path).parent.mkdir(parents=True, exist_ok=True)

# # Example model. Check https://github.com/nomic-ai/gpt4all for the latest models.
# url = 'http://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin'

# # send a GET request to the URL to download the file. Stream since it's large
# response = requests.get(url, stream=True)

# # open the file in binary mode and write the contents of the response to it in chunks
# # This is a large file, so be prepared to wait.
# with open(local_path, 'wb') as f:
#     for chunk in tqdm(response.iter_content(chunk_size=8192)):
#         if chunk:
#             f.write(chunk)

# Callbacks support token-wise streaming
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain import PromptTemplate, LLMChain
def generate_orc(question):
    template="""
	Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request in 100 words.

	### Instruction:
	Instruction

	### Input:
	{question}

	### Response:

    """

    prompt = PromptTemplate(template=template, input_variables=["question"])
    callbacks = [StreamingStdOutCallbackHandler()]

    # Verbose is required to pass to the callback manager
    llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)

    # If you want to use a custom model add the backend parameter
    # Check https://docs.gpt4all.io/gpt4all_python.html for supported backends
    llm = GPT4All(model=local_path, backend="gptj", callbacks=callbacks, verbose=True)

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    answer=llm_chain.run(question)
    return answer
