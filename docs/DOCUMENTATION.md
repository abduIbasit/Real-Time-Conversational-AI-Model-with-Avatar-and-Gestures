# Real-Time-Conversational-AI-Model-with-Avatar-and-Gestures


## Overview

The application is a converstional model with capabilities of text generation, speech recognition, speech synthesis, natural language understanding, context awareness, and avatar representation/demonstration with lip sync and gestures. The app uses state-of-the-art AI models, particularly transformers and stable diffusion model. 

A user can interact with the model either by text input or voice, the model processes the user message, understand it and generate a contextually relevant response with avatar representation, with minimal latency

## Capabilities Implementation

The application capabilities were implemented as thus;

* **Text Generation**: `llama3-8b-8192` was used for text generation/processing. Llama, as a state of the art model excels at natural language understanding and generating response. Langchain framework was used to configure the model and set up a conversation chain. A system prompt was defined to guide the model behaviour. An in-memory conversation store was created using python dictionary (this would typically be replaced with an in-memory database like Redis for enterprise scale usage, although the dictionary works exceptionally well for this prototype), the dictionary manages conversation history by appending messages to provided session_id. Groq API was used to serve the `llama3-8b-8192` model due to it incredibly fast generation throughput and low-latency performance. Groq is reported to serve LLM and other transformer based models using LPU (Language Processing Unit) in place of GPU.
  
* **Speech-to-text**: `whisper-large-v3-turbo` was used for speech to text functionality. `whisper-large-v3-turbo` performs well in understanding speech and transcribing to text. Groq API was again used to serve the whisper model for transcription, at lightning speed. The transcribed text is passed into the text generation service as input prompt for which the text generation model `llama3-8b-8192` generates a response for.

* **Text-to-speech**: Although, this functionality was eventually removed as a standalone service from the application, a text-to-speech was created to synthesize speech from text. Elevenlabs API was used for synthesizing speech/voiceover for text. The functionality was removed in order to conserve resource usage and stick to using a single service which combines speech synthesis and avatar demonstration.

* **Avatar Demonstration**: D-ID developer API was used for avatar demonstration


## Conversation Flow

## Challenges Encountered

## Conclusion
