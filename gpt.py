import openai


class GPT:
    def __init__(self, env) -> None:
        self.env = env
        openai.api_key = env['OPENAI_API_KEY']
        self.model = "gpt-3.5-turbo"
        if (env['USE_GPT_4'].upper() == 'TRUE'):
            self.model = "gpt-4"

    def getGender(self, text):
        instructions = "Given the following reddit post, determine the gender of the poster. Use the context of the post to aid you. If it is ambiguous, reply with the most likely answer. Reply with just a single letter, either M or F."
        return openai.ChatCompletion.create(model=self.model, messages=[{"role": "system", "content": instructions},
                                                                        {"role": "user", "content": text}], temperature=0.2).choices[0].message.content

    def expandAcronymsAndAbbreviations(self, text, language="english"):
        sharedInstructions = "edit it so that the abbreviations/acronyms are expanded, and correct grammar mistakes/correct for general ease of understanding. A text to speech program will use this as input, so make sure the output will be easily processed by the program. Add additional punctuation if necessary to make the speech flow better. You may leave commonly understood acronyms/abbreviations unexpanded."
        if language != "english":
            instructions = "Translate the following reddit post to " + \
                language+", then "+sharedInstructions + \
                " Then expand/convert all characters that are not letters, into the equivalent word/letter representation in the target language."
        else:
            instructions = "Given the following reddit post, "+sharedInstructions
        return openai.ChatCompletion.create(model=self.model, messages=[{"role": "system", "content": instructions},
                                                                        {"role": "user", "content": text}], temperature=0.1).choices[0].message.content

    def getSubtitles(self, text):
        instructions = "Given the following transcript, expand/convert all characters that are not letters, into the equivalent word/letter representation."
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": instructions},
                                                                             {"role": "user", "content": text}], temperature=0.1).choices[0].message.content
