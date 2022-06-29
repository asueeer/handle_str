URL=https://vwpgrh2m2x5ktbzgbkr2sia3440mitnh.lambda-url.us-east-2.on.aws

test:
	@python3 test.py


curl:
	@curl --location --request POST 'https://vwpgrh2m2x5ktbzgbkr2sia3440mitnh.lambda-url.us-east-2.on.aws' \
	--header 'Content-Type: application/json' \
	--data-raw '{ \
			"s": "one one one two one", \
			"p": "one", \
			"w": 2, \
			"m": 2 \
	}'

