# NarrReddit

An script which automates the process of turning the top reddit posts from a given subreddit into a subway surfers style tiktok narration

## Setup

Install dependencies by running `pip install -r requirements.txt`

Create a new reddit app. You can do so at this link: <https://www.reddit.com/prefs/apps>

Select script from the radio button menu. Set the redirect uri to <http://localhost:8080>

Create a .env file using the .env.template and populate the PRAW variables
NOTE: You can filter posts by character limit in the .env file. It is reccomended to set them to something other than the defaults as otherwise you may burn through your elevenlabs API char limit very quickly.

Create an elevenlabs account if you do not already have one

Paste your elevenlabs api key into the .env file

Pate your OpenAI API key in the .env file
NOTE: Currently the model used is GPT-4. You must have access to the GPT-4 model in order to run the script as-is

Run the script

TODO: 
Automated creation of subtitles to be added to the video
Ability to set GPT-3.5 as the openai model
