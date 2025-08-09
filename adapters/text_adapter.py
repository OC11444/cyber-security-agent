# adapters/text_adapter.py

def get_text_input() -> str:
    try:
        return input("[💬] Type your command: ").strip()
    except KeyboardInterrupt:
        print("\n[❌] Input cancelled by user.")
