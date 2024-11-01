# Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures


## Setup Instructions for Running Locally

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

#### 3. Run the Application

Run the application with the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 
```
The application would be accessible at ws://localhost:8000/ws/conversation. Note: You can specify different host and port.

#### 4. Interact with the Application

Interact with the application via any websocket client. Request expects the following parameters:

*session_id: required* - A session id for conversation history management.

*prompt: optional* - A prompt text which the model responds to.

*audio: optional* - An audio blob or voice recording which the model responds to.

Note: One of either prompt or audio needs to be sent but not both. Here is an example request body:

```json
{
"session_id": "xgsj5207dcjdpkql1",
"prompt": "What are large language models"
}
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

Interact with the application following the [steps](https://github.com/abduIbasit/Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures/blob/master/README.md#4-interact-with-the-application)

Read the application development documentation here: [docs](https://github.com/abduIbasit/Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures/blob/master/docs/DOCUMENTATION.md)
