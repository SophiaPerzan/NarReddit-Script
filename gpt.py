import openai


class GPT:
    def __init__(self, env) -> None:
        self.env = env
        openai.api_key = env['OPENAI_API_KEY']

    def getGender(self, text):
        instructions = "Given the following reddit post, determine the gender of the poster. Use the context of the post to aid you. If it is ambiguous, reply with the most likely answer. Reply with just a single letter, either M or F."
        return openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "system", "content": instructions},
                                                                     {"role": "user", "content": text}], temperature=0.2).choices[0].message.content

    def expandAcronymsAndAbbreviations(self, text):
        instructions = "Given the following reddit post, edit it so that the abbreviations/acronyms are expanded, and correct grammar mistakes/correct for general ease of understanding. A text to speech program will use this as input, so make sure the output will be easily processed by the program. Add additional punctuation if necessary to make the speech flow better. You may leave commonly understood acronyms/abbreviations unexpanded."
        return openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "system", "content": instructions},
                                                                     {"role": "user", "content": text}], temperature=0.1).choices[0].message.content
