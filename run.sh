#/bin/bash


mkdir -p models
mkdir -p media

docker build -t subtitle .
docker run -it --rm -u 1000 \
  -v $(pwd)/models:/app/models \
  -v /home/alexm/Videos/1810/week-01:/app/media \
  subtitle $@
  # -v $(pwd)/media:/app/media \

# docker run -it --rm -u 1000 -v $(pwd)/models:/app/models -v $(pwd)/media:/app/media subtitle media/day00-introduction.mp4
# ./run.sh media/1-development-environment.mp4