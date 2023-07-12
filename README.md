# NarrReddit

NarrReddit is a script that automates the process of converting top-rated Reddit posts into engaging, Subway Surfers-style TikTok narrations. It supports translation into multiple languages, enabling you to transform a single trending Reddit post into multilingual video content, all in an automated fashion!

## Features

- Scrapes a chosen subreddit for the highest-rated post.
- Generates Text-to-Speech (TTS) audio from the post.
- Creates subtitles for the audio.
- Overlays the generated audio and subtitles onto a selected background video.
- Supports translation into multiple languages.

## Setup

Follow these steps to set up NarrReddit:

1. Install the required dependencies by running `pip install -r requirements.txt`.

2. Place your preferred video files to be used as backgrounds in the `background-videos` directory.

3. Create a new Reddit application at this [link](https://www.reddit.com/prefs/apps). Choose 'script' from the radio button menu and set the redirect URI to `http://localhost:8080`.

4. Set up the [Gentle forced aligner](https://github.com/lowerquality/gentle) and start the server.

5. Sign up for an Elevenlabs account if you don't have one already.

6. Obtain an OpenAI API key.

7. Create a `.env` file using the `.env.template` provided in the repository.

8. Populate the `.env` variables as per your requirements.

   - **Note**: You can adjust the character limit for posts in the `.env` file. It's advisable to use a limit other than the defaults to avoid exhausting your Elevenlabs API character limit too quickly.
   
   - **Note**: You'll need an API key with access to GPT-4 for this feature. Bear in mind that using GPT-4 may result in higher API costs.

9. Run the script to start creating engaging video content from top-rated Reddit posts!
