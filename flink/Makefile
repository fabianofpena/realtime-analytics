# Variáveis
IMAGE_NAME = retail-enrichment-app
TAG = 1.3
REGISTRY = fabianofpena

# Alvos
all: build tag push

build: download_jars
	@docker build --platform linux/amd64 -t $(IMAGE_NAME):$(TAG) .

tag:
	@docker tag $(IMAGE_NAME):$(TAG) $(REGISTRY)/$(IMAGE_NAME):$(TAG)

push:
	@docker push $(REGISTRY)/$(IMAGE_NAME):$(TAG)

download_jars:
	sh jarfile_download.sh

.PHONY: all build tag push download_jars
