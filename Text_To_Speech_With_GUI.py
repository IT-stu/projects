import pyttsx3
import tkinter as tk

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to handle the input and text-to-speech
def speak_text():
    text = entry.get()
    if text.lower() == 'exit':
        engine.say("Okey the program was terminated !")
        engine.runAndWait()
        root.quit()  # Close the GUI window
    else:
        engine.setProperty('rate', 180)
        engine.say(text)
        engine.runAndWait()

# Initialize the main window
root = tk.Tk()
root.title("Text-to-Speech App")

# Configure the window layout
root.geometry("400x200")
root.resizable(False, False)

# Create and place the widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter text:")
label.pack()

entry = tk.Entry(frame, width=50)
entry.pack(pady=10)

speak_button = tk.Button(frame, text="Speak", command=speak_text)
speak_button.pack()

# Run the main loop
root.mainloop()
