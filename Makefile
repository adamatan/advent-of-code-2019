PWD := $(shell pwd)
DOCKER = docker run -it \
        --rm \
		--mount type=bind,source=$(PWD),target=/app \
		--name advent-of-code \
		python:3.8-alpine \

test:
	$(DOCKER) sh -c 'cd /app/2019; python test.py -v'

day_%:
	$(DOCKER) sh -c 'cd /app/2019; python $@.py'

