all:
	@echo "no default make rule defined"

help:
	cat Makefile

requirements:
	python3 -m pip install --upgrade -r requirements.txt

deploy_local:
	scripts/deploy_local.sh

deploy:
	scripts/deploy.sh
