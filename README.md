# NarrReddit

NarrReddit is a script that automates the process of converting top-rated Reddit posts into engaging, Subway Surfers-style TikTok narrations. It supports translation into multiple languages, enabling you to transform a single trending Reddit post into multilingual video content, all in an automated fashion!

## Features

- **Content Generation**: NarrReddit uses GPT-4 to enhance and translate Reddit posts, enabling the creation of multilingual content.

- **Reddit Scraping**: The script scrapes your chosen subreddit to find the highest-rated post.

- **Intelligent Text-to-Speech (TTS) Audio Generation**: NarrReddit generates TTS audio from the post, intelligently determining the speaker's gender and adjusting the TTS voice accordingly.

- **Subtitles Creation**: NarrReddit can also create subtitles for the generated audio.

- **Video Overlays**: The script overlays the generated audio and subtitles onto a selected background video, creating a complete, ready-to-upload video.


## Setup

Follow these steps to set up NarrReddit:

1. Install ffmpeg and make it accessible via the $PATH environment variable. [More information](https://github.com/kkroening/ffmpeg-python#installation)

2. Install the required dependencies by running `pip install -r requirements.txt`.

3. Place your preferred video files to be used as backgrounds in the `background-videos` directory.

4. Create a new Reddit application at this [link](https://www.reddit.com/prefs/apps). Choose 'script' from the radio button menu and set the redirect URI to `http://localhost:8080`.

5. Set up the [Gentle forced aligner](https://github.com/lowerquality/gentle) and start the server.

6. Sign up for an Elevenlabs account if you don't have one already.

7. Obtain an OpenAI API key.

8. Create a `.env` file using the `.env.template` provided in the repository.

9. Populate the `.env` variables as per your requirements.

   - **Note**: You can adjust the character limit for posts in the `.env` file. It's advisable to use a limit other than the defaults to avoid exhausting your Elevenlabs API character limit too quickly.
   
   - **Note**: You'll need an API key with access to GPT-4 for this feature. Bear in mind that using GPT-4 may result in higher API costs.

10. Run the script to start creating engaging video content from top-rated Reddit posts!
