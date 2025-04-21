from retriever import Retriever
import openai
import os
from dotenv import load_dotenv
from loguru import logger
load_dotenv()

# if not api_key:
#     raise EnvironmentError("A variável de ambiente 'OPENAI_API_KEY' não foi definida.")

logger.remove()
logger.add("system.log", format="{time} | {level} | {message}", level="INFO")
logger.add(lambda msg: print(msg), format="<green>{time}</green> | {level} | {message}", level="INFO", colorize=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

logger.info("Application started.")

def ask_llm(question, context):
    prompt = f"""Answer the following question based only on the provided context.
Context: {context}
Question: {question}"""

    try:
        logger.debug(f"Sending question to LLM: {question}")
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        logger.success("LLM response received successfully.")
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.exception("Failed to get a response from the LLM.")
        return "Sorry, something went wrong when generating the answer."

def main():
    try:
        logger.info("Loading Retriever and data.")
        retriever = Retriever("data/dataset.json")
        logger.success("Retriever initialized successfully.")
    except Exception as e:
        logger.exception("Failed to initialize retriever.")
        return

    print("Ask a question (type 'exit' to quit):")
    while True:
        try:
            query = input(">>> ")
            if query.lower() in ["exit", "quit"]:
                logger.info("User exited the application.")
                break

            logger.debug(f"Received user question: {query}")
            docs = retriever.search(query)
            context = "\n".join(docs)
            logger.debug("Context retrieved for the query.")

            answer = ask_llm(query, context)
            print("Answer:")
            print(answer)
            print("-" * 50)
        except KeyboardInterrupt:
            logger.warning("Keyboard interruption. Exiting.")
            break
        except Exception as e:
            logger.exception("Unexpected error during interaction.")

if __name__ == "__main__":
    main()
