import panel as pn
from openai import OpenAI

pn.extension()
OPENAI_API_KEY = "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"
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",   # OpenRouter endpoint
    api_key=OPENAI_API_KEY
)

context = [
    {
        "role": "system",
        "content": """
You are SnackBot 🤖, a friendly assistant for a snack and beverage shop 🏪.
You greet the customer 👋, collect the order (snacks 🍔, drinks 🥤, sides 🍟, desserts 🍨),
ask for sizes where applicable 📏, suggest extras and combos 🍕,
then ask if it's pickup 🏃‍♂️ or delivery  🛵.

Wait until the full order is collected, then summarize it clearly 📝
and ask if the user wants to add anything else ➕.

If delivery, ask for address 🏠.
Finally, collect payment 💳, upi id is rohankolwale@oksbi.

If it asks for delivery agents number 📞 9404819359.
Keep responses short, friendly, 😄 and conversational 🗨️.

Menu:

Snacks:
Veg burger 🍔 80, 60, 50
Chicken burger 🍗🍔 100, 80, 70
Sandwich 🥪 70, 50

Sides:
Fries 🍟 50, 40
Nuggets 🍗 90
Garlic bread 🥖🧄 60

Drinks:
Coke 🥤 40, 30, 20
Cold coffee ☕❄️ 80, 60
Milkshake 🥛🍫 100, 80

Desserts:
Brownie 🍫 60
Ice cream 🍨 50, 80

Extras:
Extra cheese  🧀 20
Extra sauce 🥫 10
Spicy mayo 🌶️ 15


This all are the prices present after the products in dollers.
"""
    }
]

inp = pn.widgets.TextInput(placeholder="Type your message...",width=400)
button = pn.widgets.Button(name="Send",width=100)
chat_history = []
chat_box = pn.Column(height=400, scroll=True,auto_scroll_limit=1, sizing_mode="stretch_width")                                         # Panel container for chat messages

def get_response(messages):
    """
    Sends the full conversation context to OpenRouter and returns AI reply
    """
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",  # Model (you can change later)
        messages=messages
    )
    return response.choices[0].message.content

def chat(event):
    user_input = inp.value.strip()
    
    if not user_input:
        return
    
    inp.value = ""
    
    context.append({
        "role": "user",
        "content": user_input
    })
    
    bot_reply = get_response(context)

    context.append({
        "role": "assistant",
        "content": bot_reply
    })

    chat_history.append(
        pn.Row(
            pn.pane.Markdown(
                # USER
                f"<div style='background:white;color:black ;padding:10px; border-radius:10px;'>You: {user_input}</div>",
                width=400
            ),
            align="end"
        )
    )
    
    chat_history.append(
        pn.Row(
            pn.pane.Markdown(
                # BOT
            f"<div style='background:#FFF5E1; color:black; padding:10px; border-radius:10px;'><b>Bot:</b> {bot_reply}</div>",
            width=400
            ),
            align="start"
        )
    )
    
    chat_box[:] = chat_history

button.on_click(chat)

app = pn.Column(
    pn.pane.Markdown("## 🍔 SnackBot Chat"),
    pn.Spacer(height=10),
    chat_box,
    pn.Spacer(height=10),
    pn.Row(inp, button, align="center")
)

pn.config.raw_css.append("""
body {
    background: linear-gradient(135deg, #F08080, #f8b4b4);
}
""")
app.servable()