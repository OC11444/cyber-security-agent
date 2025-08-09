# adapts/voice_adapter.py

from nova_voice.voice_input import listen_for_command


def get_voice_input():
    return listen_for_command()
