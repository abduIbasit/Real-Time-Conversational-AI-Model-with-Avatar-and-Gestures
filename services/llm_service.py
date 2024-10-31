from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq

from .config import settings

store = {}


class LLMService:
    def __init__(self):
        # Define the system prompt template
        template = "You are a virtual tutor named Vastlearn AI 🤖, skilled in academics. \
                    Engage users professionally."
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", template),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{query}"),
            ]
        )

        # Configure the model and set up the conversation chain
        llm = ChatGroq(model=settings.LLM_MODEL_NAME, temperature=0.3)
        self.chain = prompt_template | llm
        self.conversation_chain = RunnableWithMessageHistory(
            self.chain,
            self.get_session_memory,
            input_messages_key="query",
            history_messages_key="history",
        )

    # Method to retrieve or create chat history for the session
    def get_session_memory(self, session_id):
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    # Generate response with session-based configuration
    def generate_response(self, query: str, session_id: str) -> str:
        config = {"configurable": {"session_id": session_id}}
        return self.conversation_chain.invoke({"query": query}, config=config).content


llm_service = LLMService()
