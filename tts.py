from elevenlabs import set_api_key, generate, voices, save
import os


class TTS:
    def __init__(self, env):
        self.env = env
        set_api_key(env['ELEVENLABS_API_KEY'])
        self.voices = voices()
        # if these voice names don't exist in your ElevenLabs account, then this script will fail here
        # Paola and Arthur unfortunately did not exist for me, that's why I changed them to Rachel and Adam, who are default voices
        self.Female = self.findVoice(self.voices, "Rachel")
        self.Male = self.findVoice(self.voices, "Adam")

    def findVoice(self, voices, name):
        for voice in voices:
            if voice.name == name:
                return voice
        return None

    def createAudio(self, text, gender, language="english", selected_voice_name=None):
        user_selected_voice = self.findVoice(self.voices, selected_voice_name)
        voice = self.Female
        if gender == "M":
            voice = self.Male
        if user_selected_voice != None:
            voice = user_selected_voice
        if language == "english":
            audio = generate(
                text, voice=voice, model="eleven_monolingual_v1")
            fileName = os.path.join('tts-audio-files', 'english.mp3')
        else:
            audio = generate(
                text, voice=voice, model="eleven_multilingual_v1")
            fileName = os.path.join('tts-audio-files', language+'.mp3')
        save(audio, fileName)
        return fileName
