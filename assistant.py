
import webbrowser
import urllib.parse
import subprocess
import shutil

# Website URLs
SITES = {
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "chatgpt": "https://chatgpt.com",
    "gemini": "https://gemini.google.com"
}


def open_chrome(url):
    """Open a URL in Chrome, even if Chrome is not running."""

    chrome_paths = [
        shutil.which("chrome"),
        shutil.which("chrome.exe"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\Application\chrome.exe"
    ]

    import os
    chrome_paths[-1] = os.path.expandvars(chrome_paths[-1])

    for path in chrome_paths:
        if path and os.path.isfile(path):
            subprocess.Popen([path, url])
            return

    # Fallback: ask Windows to open the URL in the default browser.
    webbrowser.open(url)


def handle_command(command):
    command = command.lower().strip()

    # Remove common command prefixes
    for prefix in ["open ", "please open ", "go to "]:
        if command.startswith(prefix):
            command = command[len(prefix):].strip()
            break

    # Open supported websites
    for name, url in SITES.items():
        if name in command:
            print("Opening " + name.title() + "...")
            open_chrome(url)
            return

    # Search Google
    search_prefixes = [
        "search for ",
        "search ",
        "google ",
        "find "
    ]

    for prefix in search_prefixes:
        if command.startswith(prefix):
            query = command[len(prefix):].strip()

            if query:
                url = (
                    "https://www.google.com/search?q="
                    + urllib.parse.quote_plus(query)
                )
                print("Searching Google for:", query)
                open_chrome(url)
                return

    if command in ["exit", "quit", "stop"]:
        print("Assistant stopped. Goodbye!")
        return "exit"

    if command in ["help", "commands"]:
        print("""
Available commands:
  open youtube
  open facebook
  open chatgpt
  open gemini
  search Python tutorials
  google best coding websites
  exit
""")
        return

    print("Command not recognized. Type 'help'.")


print("=" * 40)
print("     PYTHON WEB ASSISTANT")
print("=" * 40)
print("Type 'help' to see commands.")
print("Type 'exit' to close the assistant.")

while True:
    command = input("\nYou: ")

    result = handle_command(command)

    if result == "exit":
        break
