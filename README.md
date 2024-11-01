# Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures

Run the application locally using any of the explained setups. An essential initial step before any of the steps outlined is cloning this repository and navigating to the project directory by entering these commands in your terminal:

```bash
git clone https://github.com/abduIbasit/Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures.git
cd Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures
```

After navigating to the project directory, follow the steps for any of the setups to run.


## Setup Instructions for Running with Python

#### 1. Set Up the Environment

Ensure you have Python 3.8 or higher installed.

Create a virtual environment (recommended):

```bash
python -m venv env
source env/bin/activate
```

#### 2. Install Dependencies:

Run the below command from the directory where the requirements.txt is to install the packages

```bash
pip install -r requirements.txt
```

#### 3. Set environment variables
Set environment variables for GROQ_API and D-ID in .env file in the root directory

- GROQ API keys can be obtained from [https://console.groq.com/keys](https://console.groq.com/keys)

- D-ID API [https://www.d-id.com/api/](https://www.d-id.com/api/)

#### 4. Run the Application

Run the application with the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 
```
The application would be accessible at ws://localhost:8000/ws/conversation.

#### 5. Interact with the Application

Interact with the application via any websocket client. Request expects the following parameters:

***session_id: required*** - A session id for conversation history management.

***prompt: optional*** - A prompt text which the model responds to.

***audio: optional*** - An audio blob or voice recording which the model responds to.

**Note:** One of either prompt or audio needs to be sent but not both. Here is an example request body:

```json
{
"session_id": "xgsj5207dcjdpkql1",
"prompt": "What are large language models"
}
```

Response body is a text response from the model and an avatar demonstration

![demo](https://github.com/user-attachments/assets/a0c803ff-1214-4228-97b2-30b0a004e74c)

Alternatively, interact with the application using the frontend application I developed by cloning the repo [https://github.com/abduIbasit/Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures-Frontend.git](https://github.com/abduIbasit/Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures-Frontend.git)

## Setup Instructions for Running with Make

To run with `make`, ensure you have `make` and `python` installed on your computer.

- Simply set up and run the application in one go by entering this command in your terminal:
```bash
make setup
```

- Stop the application with:
```bash
make stop
```

- Clean up and remove the virtual environment with:
```bash
make clean
```


## Setup Instructions for Running on Docker

To run the application on Docker, follow the steps below.

#### 1. Build the docker image
```bash
docker build -t conversational-ai-app .
```

#### 2. Run the docker container
```bash
docker run -p 8000:8000 conversational-ai-app
```

After running the container, the application would be accessible at ws://localhost:8000/ws/conversation.

Interact with the application following the [step](#5-interact-with-the-application)

Read the application development documentation here: [docs](https://github.com/abduIbasit/Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures/blob/master/docs/DOCUMENTATION.md)
