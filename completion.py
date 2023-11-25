# Import necessary modules
import os  # Provides functions to interact with the operating system
from dotenv import load_dotenv  # Load environment variables from a .env file

# Load environment variables from .env file
load_dotenv()  # Loads environment variables from a .env file into the script's environment

from openai import AzureOpenAI  # Import the AzureOpenAI class from the openai library

# Create an instance of the AzureOpenAI class
client = AzureOpenAI(
    azure_endpoint=os.getenv("AOAI_AZURE_ENDPOINT"),
    api_version=os.getenv("AOAI_API_VERSION"),
    api_key=os.getenv("AOAI_API_KEY")  # Retrieve the OpenAI API key from environment variables
)

# Define a class called MyClass
class Completion:

    # Define a method called gptResponse that takes user_input as a parameter
    def gptResponse(user_input):

        # Generate chat completions using the OpenAI API
        completion = client.chat.completions.create(
            model= os.getenv("AOAI_MODEL"),
            messages=[
                {"role": "system", "content": "You are an AI assistant that helps people find information."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            
        )

        print(completion) # Print the completion object understand it better. 
        return completion.choices[0].message.content # Returns the desired Message

