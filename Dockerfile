FROM python:3.11

RUN python -m pip install moviepy git+https://github.com/openai/whisper.git
RUN apt update && apt install -y ffmpeg

WORKDIR /app
COPY subtitles_with_whisper.py subtitles_with_whisper.py

ENTRYPOINT ["python", "subtitles_with_whisper.py"]
# docker build -t subtitle .
# docker run -it --rm -u 1000 -v $(pwd)/models:/app/models -v $(pwd)/media:/app/media subtitle media/day00-introduction.mp4