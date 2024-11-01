# Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures


## Overview

This application is a sophisticated conversational AI model with advanced capabilities for text generation, speech recognition, speech synthesis, natural language understanding, contextual awareness, and dynamic avatar representation with perfect lip-sync and gestures. Leveraging state-of-the-art AI models, particularly transformers and stable diffusion, the application allows users to interact through either text input or voice via a websocket connection for real time communication. The model processes the user inputs, generate contextually relevant response instantly and deliver a compelling, animated avatar interaction.

## Capabilities Implementation

The application's core features were implemented as follows;

* **Text Generation**: `llama3-8b-8192` model was used for text responses generation. Llama, as a state of the art model excels at natural language understanding and generating relevant response. Langchain framework was used to configure the model and set up a conversation chain, where a predefined system prompt guide the model responses and behaviour. An in-memory conversation store, managed via a Python dictionary (which could be replaced by Redis for scaling), appends messages to the session ID to track conversation history. The `Groq API` serves the model due to its high throughput and low-latency performance, enabling quick and efficient text generation. *Groq is reported to serve LLM and other transformer-based models using LPU (Language Processing Unit) in place of GPU.*
  
* **Speech-to-text**: The `whisper-large-v3-turbo` model handles the transcription of voice input to text. Known for its accuracy in speech recognition, this model is also served through the `Groq API`, which ensures low latency in converting spoken input to text. The transcribed text is then processed by the `llama3-8b-8192` model to generate a relevant response.

* **Text-to-speech**: Although, this functionality was eventually removed as a standalone service from the application in order to conserve resource usage and stick to using a single service which combines speech synthesis and avatar demonstration. Elevenlabs API was used for synthesizing speech from text.

* **Avatar Demonstration**: D-ID developer API was used for avatar demonstration. D-ID API creates photorealistic videos using generative AI. Two methods were defined to interact with the avatar video creation endpoints;

  `generate_clip`: Initiates the avatar video creation, vocalizing the text response of the language model with perfect lip sync and gesture. 

  `get_video`: A custom polling service that periodically checks the video generation status and provides the video URL once it’s ready. 


The video creation time typically varies between 30-50 seconds, depending on the length of the text response.


## Model Choice Decision Table

The model selections for powering various tasks in the application are summarized below, with justifications for each choice.

| Task                       | Choice                                   | Alternative                                            | Reason for choice                               |
| -------------------------- |----------------------------------------  | ------------------------------------------------------ |-------------------------------------------------|
| Text generation/LLM        | `llama3-8b-8192` with Groq API           | `llama3-8b-8192` with Transformers library             | Chose `llama3-8b-8192` + Groq API due to GPU unavailability and the application’s user scale. `llama3-8b-8192` + text streaming implementation using Transformers library provides a scalable and efficient alternative.|
| Speech-to-text             | `whisper-large-v3-turbo` with Groq API   | `whisper-large-v3-turbo` with Transformers library     | Similar to the LLM decision, `whisper-large-v3-turbo` is preferred with Groq API, balancing performance and scalability in the absence of GPU hardware.
| Text-to-speech             | Elevenlabs API                           | `myshell-ai/MeloTTS-English` with Transformers library | Due to GPU limitations and the application's scale, ElevenLabs API was chosen for its high-quality TTS capabilities, though open-source ASR models would work well with GPU hardware.
| Avatar Demonstration       | D-ID API                                 | `LivePortrait` with custom code                        | Similar reason as priors applies. Due to GPU constraints for running the LivePortait code which performs on same scale as D-ID, the D-ID API was used instead

I bear a personal opinion that using developer APIs for small-scale applications with limited users offers cost and resource savings compared to custom GPU deployments. For larger user bases, investing in custom deployments with GPU support may provide better control and scalability.

This application runs on a CPU machine.

## Conversation Flow

The conversation flow begins with the user inputs either text or voice. Text inputs are sent directly to the large language model, which processes the message to generate a contextually relevant response. For voice inputs, the application transcribes the audio into text using speech-to-text functionality before sending it to the LLM. The generated response from the LLM is sent to the user and also passed to the avatar demonstration module, which creates a synchronized video with lip-sync and gestures, delivering a dynamic and engaging interaction experience.

*I developed a client-side application using React JS to provide a user interface for interacting with the application which can be accessed [here](http://34.55.139.78/). **Caveat:** My frontend development skill is not the best.*

## Cloud Deployment

I deployed both the conversational AI WebSocket service and the frontend application to Google Cloud Platform (GCP), utilizing a virtual machine instance I configured specifically for this purpose.

## Challenges Encountered

1. **Real-Time Avatar Video Streaming:** A challenge I faced was implementing real-time streaming for the generated avatar video from D-ID. The setup required a WebRTC connection, which is typically more adaptable when managed from the client-side. To address this, I devised a custom solution by building a polling service that regularly checks the video generation status from the D-ID API endpoint and sends the video url immediately upon creation, allowing for near-real-time updates. Collaborating with a frontend engineer to implement true streaming would yield a more seamless experience
2. **Voice Recording on Cloud:** A slight issue is experienced with recording voice from the frontend application on the cloud deployment due to missing SSL certificate, required by browser

## Conclusion

The application successfully fulfills its primary objectives, demonstrating capabilities in text generation, speech recognition, and avatar interaction using real-time communication via websocket connection. This foundational functionality sets a strong base for further development, where additional features and enhancements could make the application even more versatile and robust. With continued development, the application has the potential to deliver a more immersive and interactive user experience, adapting to evolving requirements and providing scalable solutions for broader use cases.
