PWD := $(shell pwd)
DOCKER = docker run -it \
        --rm \
		--mount type=bind,source=$(PWD),target=/app \
		--name $@ \
		python:3.8-alpine \

test:
	$(DOCKER) sh -c 'cd /app/2019; python test.py -v TestDay5.test_step_2_06'

day_%:
	$(DOCKER) sh -c 'cd /app/2019; python $@.py'

