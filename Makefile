PWD := $(shell pwd)

test:
	docker run -it \
        --rm \
		--mount type=bind,source=$(CURDIR),target=/app \
		--name advent-of-code \
		python:3.8-alpine \
		sh -c 'cd /app/2019; python test.py -v'