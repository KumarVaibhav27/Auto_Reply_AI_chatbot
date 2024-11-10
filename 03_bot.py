import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key ="",
)

def Last_message_from_sender(chat_log, sender_name=""):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    else:
        False

def check_for_exit_phrases(chat_log):
    exit_phrases = ["bye", "good night", "talk to you later", "see you tomorrow"]
    # Check if any exit phrase is in the last message
    return any(phrase.lower() in chat_log.lower() for phrase in exit_phrases)

# Click on the whatsapp icon at coordinates (293, 1056)
pyautogui.click(293, 1056)
time.sleep(1)  # Wait for the action to complete

while True:
    # Drag from (662, 100) to (1800, 960) to select the text
    pyautogui.moveTo(662, 100)
    pyautogui.dragTo(1800, 959, duration=1, button='left')
    time.sleep(0.5)  # Wait a bit after selecting the text

    # Copy the selected text to clipboard (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1726,444)
    time.sleep(1)  # Wait a moment for the copy action to complete

    # Retrieve the copied text from clipboard into a variable
    chat_history = pyperclip.paste()

    # Output the copied text (optional)
    print("Copied Text:", chat_history)

    if check_for_exit_phrases(chat_history):
        # Copy 'bye' to clipboard
        pyperclip.copy("bye")
        time.sleep(1)

        # Click to focus and send 'bye' message
        pyautogui.click(924, 1001)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.sleep(1)
        pyautogui.press('enter')
        print("Conversation ended with 'bye'.")
        break

   
    if Last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"Reply like Kumar Vaibhav , who speaks both Hindi as well as English. Analyze the chat history and respond like Kumar Vaibhav on the basis of last text message received. Output should be next chat response text message only and it should be very humanize text.."},
                {"role":"user","content":chat_history}
            ]
        )
        response = completion.choices[0].message.content

        # Copy the text variable to the clipboard
        pyperclip.copy(response)
        time.sleep(1)

        # Click at (924, 1001) to focus the paste location
        pyautogui.click(924, 1001)
        time.sleep(1)  # Brief pause to ensure focus

        # Paste the text (Ctrl+V) and press Enter
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.sleep(1) # Wait for 1 second to ensure the paste command is completed
        pyautogui.press('enter')
