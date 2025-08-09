from gtts import gTTS
import os
from pathlib import Path
from nova_voice.greetings import get_greeting
from assistant.branding import PROJECT_DIR_NAME

# In-memory session flag to prevent repeated greetings
_greeting_spoken = False

def speak_greeting():
    global _greeting_spoken
    if _greeting_spoken:
        return  # Skip if already spoken this session

    text = get_greeting()
    print(f"[Nova] Speaking: {text}")
    
    tts = gTTS(text=text, lang='en', tld='co.uk')

    # Use standard Linux config dir: ~/.local/share/<project>/sounds
    home = Path.home()
    output_dir = home / f".local/share/{PROJECT_DIR_NAME}/sounds"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "startup.mp3"
    tts.save(str(output_path))

    # Safe playback with fallback if mpg123 isn't installed
    if os.system("which mpg123 > /dev/null") == 0:
        os.system(f"mpg123 '{output_path}'")
    else:
        print("[⚠️ Nova] 'mpg123' not found. Please install it or use another player to listen to the greeting.")

    # ✅ Mark as played (in-memory only)
    _greeting_spoken = True

    return str(output_path)
