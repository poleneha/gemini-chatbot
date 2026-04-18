# 🤖 NehaBot — AI Chatbot using Gemini API

A conversational AI chatbot built with Python and Google Gemini API.  
Supports multi-turn conversations with memory of previous messages in the session.

---

## ✨ Features

- 💬 Multi-turn conversation memory (remembers context within a session)
- ⚡ Powered by Google Gemini 1.5 Flash (free tier)
- 🎨 Colored terminal output for better readability
- 🛡️ Error handling for API failures and invalid input
- 🚪 Clean exit with session summary

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Google Gemini API | AI language model |
| google-generativeai | Official Gemini Python SDK |
| colorama | Colored terminal output |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API key
- Get a free API key from [Google AI Studio](https://aistudio.google.com)
- Open `chatbot.py` and replace `YOUR_API_KEY_HERE` with your actual key

### 4. Run the chatbot
```bash
python chatbot.py
```

---

## 💻 Demo

```
==================================================
   Welcome to NehaBot — Powered by Gemini AI
==================================================
  Type your message and press Enter to chat.
  Type 'quit' or 'exit' to stop.

You: What is machine learning?
NehaBot: Machine learning is a branch of AI where systems learn
from data to make predictions or decisions without being
explicitly programmed for each task.

You: Give me an example
NehaBot: A common example is email spam detection — the model
learns from thousands of emails to identify patterns that
distinguish spam from normal messages.
```

---

## 📁 Project Structure

```
gemini-chatbot/
│
├── chatbot.py          # Main chatbot application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔑 Getting a Free API Key

1. Visit [aistudio.google.com](https://aistudio.google.com)
2. Sign in with your Google account
3. Click **Get API Key** → **Create API key**
4. Copy and paste it into `chatbot.py`

---

## 👩‍💻 Author

**Neha Pole**  
BCA Student | AI Engineer Certified  
📧 nehapole72@gmail.com
