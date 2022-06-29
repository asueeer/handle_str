.PHONY: docker

docker:
	docker run --network=host --rm -v ${PWD}:/app/ -v ${PWD}/../functions:/functions/ chrisengelhardt/apollo-autodeploy

docker-mappings:
	docker run --network=host --rm -v ${PWD}:/app/ -v ${PWD}/../functions:/functions/ chrisengelhardt/apollo-autodeploy --mappings