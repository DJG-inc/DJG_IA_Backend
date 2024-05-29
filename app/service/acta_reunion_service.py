import speech_recognition as sr
from ..utils.prompt_builder import build_prompt_minutes
from ..service.ia_service import configure_ai
import os
from pydub import AudioSegment

def transcribe_audio_to_text(audio_file_path):
    # Convertir el archivo de audio a formato WAV
    audio = AudioSegment.from_file(audio_file_path)
    wav_file_path = audio_file_path.replace(".mp3", ".wav")
    audio.export(wav_file_path, format="wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as source:
        audio = recognizer.record(source)
    os.remove(wav_file_path)  # Eliminar el archivo WAV temporal

    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None

def generate_acta_reunion(audio_file_path):
    transcribed_text = transcribe_audio_to_text(audio_file_path)
    if not transcribed_text:
        return None

    prompt = build_prompt_minutes(transcribed_text)
    model = configure_ai()
    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    response = convo.last.text
    return response