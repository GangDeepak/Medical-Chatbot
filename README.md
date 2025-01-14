# Medical-Chatbot-GenAI

## How to Run?

### STEPS:

#### Clone the repository
Clone the repository from GitHub to your local machine using the following command:

```bash
git clone https://github.com/your-username/Medical-Chatbot-GenAI.git
cd Medical-Chatbot-GenAI
```
### STEP 01: Create a conda environment
Create a conda environment with Python 3.10 and activate it.

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### STEP 02: Install the requirements
Install the required dependencies listed in requirements.txt.

```bash
pip install -r requirements.txt
```

### STEP 03: Configure Pinecone credentials
Create a .env file in the root directory and add your Pinecone API credentials as follows:

``` bash
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### STEP 04: Download the Llama 2 Model
Download the quantized Llama 2 model from the following link. Save it inside the model/ directory.

Model: llama-2-7b-chat.ggmlv3.q4_0.bin


### STEP 05: Create the Pinecone Index
Once you've placed the model inside the model/ folder, create the index by running the following command. This will index your data and store it in Pinecone.

```bash
python store_index.py
```

### STEP 06: Start the Flask Application
After the index has been created, run the following command to start the Flask web application that will serve the chatbot.

```bash
python app.py
```

### STEP 07: Open the Chatbot Interface


### Tech Stack Used
The following technologies are used to build this chatbot:

#### Python: The programming language used for development.
#### LangChain: Used for chaining language model prompts and logic.
#### Flask: Web framework used to serve the chatbot as a web application.
#### Meta Llama2: A large language model used for the chat functionality.
#### Pinecone: A vector search engine used for efficient similarity search in the chatbot.

### Folder Structure
The project folder structure looks like this:

```bash
Medical-Chatbot-GenAI/
│
├── app.py               # Main Flask application
├── store_index.py       # Script for creating the Pinecone index
├── requirements.txt     # List of dependencies
├── .env                 # Environment variables for API keys
├── model/               # Folder containing Llama2 model
│   └── llama-2-7b-chat.ggmlv3.q4_0.bin
├── static/              # Static files (CSS, JavaScript, images)
├── templates/           # HTML templates for the chatbot UI
└── README.md            # Project documentation
```
