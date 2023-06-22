# NarrReddit

An script which automates the process of turning the top reddit posts from a given subreddit into a subway surfers style tiktok narration

## Setup

Install dependencies by running `pip install -r requirements.txt`

Put a video file to be used for the background in the background-videos directory. The video must be longer than the length of the generated narration, so I reccomend something 5 mins or longer. (I may fix this in the future)

Create a new reddit app. You can do so at this link: <https://www.reddit.com/prefs/apps>

Select script from the radio button menu. Set the redirect uri to <http://localhost:8080>

Create a .env file using the .env.template and populate the PRAW variables
* NOTE: You can filter posts by character limit in the .env file. It is reccomended to set them to something other than the defaults as otherwise you may burn through your elevenlabs API char limit very quickly.

Create an elevenlabs account if you do not already have one

Paste your elevenlabs api key into the .env file

Paste your OpenAI API key in the .env file and set whether or not you want to use GPT-4
* NOTE: You will need an API key with access to gpt-4 in order to use it. Expect higher api costs if doing so.

Set the filename of the background video you want to use in the BG_VIDEO_FILENAME field of the .env file

Run the script

TODO:
* Automated creation of subtitles to be added to the video
* Picking a random background video from a library
* Ability for background videos to be shorter than the narration
