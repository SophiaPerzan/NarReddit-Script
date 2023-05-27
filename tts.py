from elevenlabs import set_api_key, generate, voices, save

class TTS:
    def __init__(self, env):
        self.env = env
        set_api_key(env['ELEVENLABS_API_KEY'])
        self.voices = voices()

    def createAudio(self, title, text):
        audio = generate(text, voice=self.voices[2], model="eleven_monolingual_v1")
        fileName = 'speech.mp3'
        save(audio, fileName)
        return fileName