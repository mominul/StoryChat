local_path = (
    "/Users/mominul/Downloads/orca-mini-3b.ggmlv3.q4_0.bin"
)
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain import PromptTemplate, LLMChain
from fpdf import FPDF

class SpecalizedChatBot:
    def __init__(self):
        self.template="""
	    Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request in 100 words.

    	### Instruction:
	    Create children storybook style writting if the input is related to children storybook related topics otherwise just give normal answer.
       
	    ### Input:
	    {question}

	    ### Response:

        """

        self.prompt = PromptTemplate(template=self.template, input_variables=["question"])
        self.callbacks = [StreamingStdOutCallbackHandler()]

        # Verbose is required to pass to the callback manager
        self.llm = GPT4All(model=local_path, callbacks=self.callbacks, verbose=True)

        # If you want to use a custom model add the backend parameter
        # Check https://docs.gpt4all.io/gpt4all_python.html for supported backends
        self.llm = GPT4All(model=local_path, backend="gptj", callbacks=self.callbacks, verbose=True)

        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm)
        self.pdf_gen=FPDF()


    def generate_response(self,question):
        result=self.llm_chain.run(question)
        self.pdf_gen.add_page()
        self.pdf_gen.set_font('Arial', 'B', 8)
        self.pdf_gen.multi_cell(0, 10, result)

        pdf_string=self.pdf_gen.output("random", 'S')
        print(pdf_string)
        return pdf_string



        

    

        

