# Variáveis
IMAGE_NAME = kafka-connect-strimzi
TAG = 3.6.1
REGISTRY = fabianofpena

# Alvos
all: build tag push

build:
	@docker build --platform linux/amd64 -t $(IMAGE_NAME):$(TAG) .

tag:
	@docker tag $(IMAGE_NAME):$(TAG) $(REGISTRY)/$(IMAGE_NAME):$(TAG)

push:
	@docker push $(REGISTRY)/$(IMAGE_NAME):$(TAG)

.PHONY: all build tag push
