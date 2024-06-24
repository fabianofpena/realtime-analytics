# Variáveis
BASE_IMAGE_NAME = flink-python-base
APP_IMAGE_NAME = retail-enrichment-app
TAG = 1.6
REGISTRY = fabianofpena

# Alvos
all: base app

# Alvo para a imagem base
base: build_base_image tag_base_image push_base_image

# Alvo para a imagem da aplicação
app: download_jars build_app_image tag_app_image push_app_image

build_base_image:
	@docker build --platform linux/amd64 -t $(BASE_IMAGE_NAME):$(TAG) -f Dockerfile.base .

tag_base_image:
	@docker tag $(BASE_IMAGE_NAME):$(TAG) $(REGISTRY)/$(BASE_IMAGE_NAME):$(TAG)

push_base_image:
	@docker push $(REGISTRY)/$(BASE_IMAGE_NAME):$(TAG)

build_app_image:
	@docker build --platform linux/amd64 -t $(APP_IMAGE_NAME):$(TAG) -f Dockerfile.app .

tag_app_image:
	@docker tag $(APP_IMAGE_NAME):$(TAG) $(REGISTRY)/$(APP_IMAGE_NAME):$(TAG)

push_app_image:
	@docker push $(REGISTRY)/$(APP_IMAGE_NAME):$(TAG)

download_jars:
	sh jarfile_download.sh

.PHONY: all base app build_base_image tag_base_image push_base_image build_app_image tag_app_image push_app_image download_jars
