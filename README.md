# Advent of Code

## Running

### With Python 3.8

    python day_<number>.py

### Using docker

    docker run -it \
           --rm \
           --mount type=bind,source=$(pwd),target=/app \
           --name advent-of-code \
           python:3.8-alpine \
           sh -c 'cd /app/2019; python day_<number>.py

## Testing

    make test
