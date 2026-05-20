from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._api import YouTubeTranscriptApi as YTAPI
import os
import re

def get_video_id(url):
    match = re.search(r'(?:v=|youtu\.be/)([^&\n?#]+)', url)
    return match.group(1) if match else None

def fetch_and_save(video_url, author_name, video_title):
    video_id = get_video_id(video_url)
    if not video_id:
        print(f"Could not extract video ID from {video_url}")
        return

    try:
        ytt_api = YouTubeTranscriptApi()
        fetched = ytt_api.fetch(video_id)
        full_text = ' '.join([entry.text for entry in fetched])

        folder = f"research/youtube-transcripts/{author_name}"
        os.makedirs(folder, exist_ok=True)

        filename = f"{folder}/{video_title}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {video_title}\n\n")
            f.write(f"**URL:** {video_url}\n\n")
            f.write("---\n\n")
            f.write(full_text)

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error fetching transcript for {video_url}: {e}")

# Videos to fetch
videos = [
    ("https://www.youtube.com/watch?v=8gi8tCb3Q4I", "alex-berman", "cold-email-masterclass"),
    ("https://www.youtube.com/watch?v=llxqzy0yhLU", "alex-berman", "cold-email-subject-lines"),
    ("https://www.youtube.com/watch?v=XEK4B8mCzNo", "alex-berman", "cold-email-copywriting"),
    ("https://www.youtube.com/watch?v=izSIXotnAfg", "alex-berman", "cold-email-follow-up-strategy"),
    ("https://www.youtube.com/watch?v=BASMa1apk-I", "alex-berman", "cold-email-agency-outreach"),
]

for url, author, title in videos:
    fetch_and_save(url, author, title)