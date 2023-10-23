#/bin/bash

docker build -t subtitle .
docker run -it --rm -u 1000 \
  -v $(pwd)/models:/app/models \
  -v $(pwd)/media:/app/media \
  subtitle $@

# docker run -it --rm -u 1000 -v $(pwd)/models:/app/models -v $(pwd)/media:/app/media subtitle media/day00-introduction.mp4