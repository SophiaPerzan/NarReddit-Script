# NarrReddit

An script which automates the process of turning the top reddit posts from a given subreddit into a subway surfers style tiktok narration

## Setup

Install dependencies by running `pip install -r requirements.txt`

Put a video files to be used for the background in the background-videos directory.

Create a new reddit app. You can do so at this link: <https://www.reddit.com/prefs/apps>

Select script from the radio button menu. Set the redirect uri to <http://localhost:8080>

Get the gentle forced aligner <https://github.com/lowerquality/gentle> and start the server

Create an elevenlabs account if you do not already have one

Get an OpenAI API key

Create a .env file using the .env.template

Populate the .env variables

-   NOTE: You can filter posts by character limit in the .env file. It is recommended to set them to something other than the defaults as otherwise you may burn through your elevenlabs API char limit very quickly.
-   NOTE: You will need an API key with access to gpt-4 in order to use it. Expect higher api costs if doing so.

Run the script

TODO:
-   Use GPT-4 for translation of content to other languages
