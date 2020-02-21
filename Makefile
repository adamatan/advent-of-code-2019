PWD := $(shell pwd)
DOCKER = docker run -it \
        --rm \
		--mount type=bind,source=$(PWD),target=/app \
		--name $@ \
		python:3.8-alpine \

test:
	$(DOCKER) sh -c 'cd /app/2019; python test.py'

test_day_%:
	$(DOCKER) sh -c 'cd /app/2019; python test.py -v $(subst test_day_,TestDay,$@)'

day_%:
	$(DOCKER) sh -c 'cd /app/2019; python $@.py'

