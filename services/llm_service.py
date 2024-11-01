from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq

# Dictionary instance for In-memory chat history management,
# can be replaced with Redis in live application
store = {}


class LLMService:
    def __init__(self):
        """Configure the model and set up the conversation chain"""

        # System prompt template for the model
        template = "You are a virtual tutor named Vastlearn AI 🤖, skilled in academics. \
                    Engage users professionally."
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", template),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{query}"),
            ]
        )

        llm = ChatGroq(model="llama3-8b-8192", temperature=0.3, max_tokens=None)
        self.chain = prompt_template | llm
        self.conversation_chain = RunnableWithMessageHistory(
            self.chain,
            self.get_session_memory,
            input_messages_key="query",
            history_messages_key="history",
        )

    def get_session_memory(self, session_id):
        """Retrieve/create new chat history for the session"""
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    def generate_response(self, query: str, session_id: str) -> str:
        """Generate response with session-based configuration"""
        config = {"configurable": {"session_id": session_id}}
        return self.conversation_chain.invoke({"query": query}, config=config).content


llm_service = LLMService()
