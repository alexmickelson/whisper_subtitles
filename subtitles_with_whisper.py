from datetime import timedelta
import math
import subprocess
import sys
from time import time
from typing import Any
import whisper
from whisper.utils import get_writer
from moviepy.editor import AudioFileClip


def extract_audio(video_path: str):
    print(f"extracting audio from: {video_path}")
    audio_path = video_path[: -len(".mp4")] + ".wav"

    audioclip = AudioFileClip(video_path)
    open(audio_path, "w").close()  # delete any previous audio files
    audioclip.write_audiofile(audio_path)
    return audio_path


def transcribe_audio(input_audio_path: str):
    print(f"loading whisper model")
    model = whisper.load_model(
        "base.en", download_root="./models"  # options: tiny, base, small, medium, large
    )
    print(f"Whisper model loaded, extracting srt subtitles from : {input_audio_path}")
    transcribe = model.transcribe(
        input_audio_path,
        fp16=False,
        language="en",
        word_timestamps=True,
        task="transcribe",
        # verbose=True
    )

    word_options = {"highlight_words": False, "max_line_count": 1, "max_line_width": 55}
    vtt_writer = get_writer(output_format="vtt", output_dir="./media")
    vtt_writer(transcribe, input_audio_path, word_options)  # type: ignore

    srt_writer = get_writer(output_format="srt", output_dir="./media")
    srt_writer(transcribe, input_audio_path, word_options)  # type: ignore

def merge_mp4_and_sub_to_mkv(input_video_path: str):
    print("making merged mkv with subtitles")
    srt_path = input_video_path[: -len(".mp4")] + ".srt"
    output_path = input_video_path[: -len(".mp4")] + ".mkv"
    command = [
        'ffmpeg',
        '-i', input_video_path,
        '-i', srt_path,
        '-c', 'copy',
        '-c:s', 'srt',
        '-metadata:s:s:0', 'language=eng',
        output_path
    ]

    subprocess.run(command, check=True)



def print_time_interval(start_time):
    duration_in_seconds = time() - start_time
    only_minutes = math.floor(duration_in_seconds // 60)
    only_seconds = math.floor(duration_in_seconds % 60)
    print(f"durration: {only_minutes} min {only_seconds} sec")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python subtitles_with_whisper.py <filename>")
        sys.exit(1)

    video_filename = sys.argv[1]
    start_time = time()
    audio_path = extract_audio(video_filename)
    transcribe_audio(audio_path)
    # merge_mp4_and_sub_to_mkv(video_filename)

    print_time_interval(start_time)
