import google.generativeai as genai
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# ── CONFIG ─────────────────────────────────────────────
API_KEY = "AIzaSyAn0F9qITfbM6CNSqKctlIx0ycVSZ2itEs"   # <-- Paste your Gemini API key here
BOT_NAME = "NehaBot"
MODEL   = "gemini-1.5-flash"    # Free tier model
# ───────────────────────────────────────────────────────

def setup_model():
    """Configure Gemini API and return a chat session."""
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel(
        model_name=MODEL,
        system_instruction=(
            "You are a helpful, friendly, and concise AI assistant called NehaBot. "
            "Answer clearly and keep responses short unless asked for detail."
        )
    )
    # Start a chat session — this keeps conversation history automatically
    return model.start_chat(history=[])


def print_banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + f"   Welcome to {BOT_NAME} — Powered by Gemini AI")
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "  Type your message and press Enter to chat.")
    print(Fore.YELLOW + "  Type 'quit' or 'exit' to stop.\n")


def chat():
    print_banner()

    try:
        chat_session = setup_model()
    except Exception as e:
        print(Fore.RED + f"[Error] Could not connect to Gemini API: {e}")
        print(Fore.RED + "Make sure your API key is correct.")
        return

    conversation_count = 0

    while True:
        # Get user input
        try:
            user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL).strip()
        except KeyboardInterrupt:
            print(Fore.CYAN + "\n\nGoodbye! Have a great day!")
            break

        # Exit conditions
        if not user_input:
            continue
        if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
            print(Fore.CYAN + f"\n{BOT_NAME}: Goodbye! It was nice talking to you. 👋")
            break

        # Send message to Gemini and get response
        try:
            print(Fore.BLUE + f"{BOT_NAME}: " + Style.RESET_ALL, end="", flush=True)
            response = chat_session.send_message(user_input)
            print(response.text)
            conversation_count += 1

        except Exception as e:
            print(Fore.RED + f"[Error] Something went wrong: {e}")
            print(Fore.RED + "Please try again.")

        print()  # blank line between turns

    print(Fore.CYAN + f"\n[Session ended — {conversation_count} messages exchanged]")


if __name__ == "__main__":
    chat()
