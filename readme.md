# README

## Deploy the lambda function

### If you want to deploy the handle_str lambda function:
run command   
`cd aws/function-templates && make docker`

### My AWS Lambda url is:
https://8lt8n6sx20.execute-api.us-east-1.amazonaws.com/HandleStr

### Test Task1:
`
curl --location --request POST 'https://8lt8n6sx20.execute-api.us-east-1.amazonaws.com/HandleStr' 
--header 'Content-Type: application/json' 
--data-raw '{
        "inputStr": "one one one two one",
        "pattern": "one",
        "wordNum": 2,
        "threshold": 2
}'
`

You will get result:   
`{"Count": 4, "NextStr": "one two one"}`