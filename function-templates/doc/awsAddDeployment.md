# Add a function to auto deployment for AWS
We need to adjust `aws/lambda.tf` and `aws/deployment.sh` to add a new function to the auto deployment.

- Node:
    - `aws/deploy.sh`:
        1. Add `./build.sh ../functions/<your-function-name>` before `terraform init`.
        2. Adjust the line number in the `showURL` block: `terraform show | tail -n 3` (example for deploying 3 functions) 
    - `aws/lambda.tf`:
        1. Add `"<your_function_name>"` to the function_names array.
        2. Add the path of the zip file to the function_paths array (normally this should be: `"tmp/<your_function_name.zip"`)
        3. Add `"nodejs14.x"` to function_runtimes.
        4. Add `"index.handler"` to function_handlers.
        5. Add `[]` to function_layers. Your locals block should now look similar to this:
            ```
            locals {
                function_names = ["template-node","template-python","<your_function_name>"]
                function_paths = ["tmp/template-node.zip","tmp/template-node.zip","tmp/<your_function_name.zip"]
                function_runtimes = ["nodejs14.x","python3.8","nodejs14.x"]
                function_handlers = ["index.handler","lambda_function.lambda_handler","index.handler"]
                function_layers = [[],[],[]]
            }
            ```
        6. Add a new `aws_api_gateway_deployment` block:
            ```
            resource "aws_api_gateway_deployment" "example<index_in_function_names_array>" {
                depends_on = [
                    aws_api_gateway_integration.lambda[<index_in_function_names_array>],
                    aws_api_gateway_integration.lambda_root[<index_in_function_names_array>],
                ]

                rest_api_id = aws_api_gateway_rest_api.example[<index_in_function_names_array>].id
                stage_name  = local.function_names[<index_in_function_names_array>]
            }
            ```
        7. Add a new output block at the end of `aws/lambda.tf`:
            ```
            output "url_<your-function-name>" {
                value = aws_api_gateway_deployment.example<index_in_function_names_array>.invoke_url
            }
            ```
- Python:
    - `aws/deploy.sh`:
        1. Add `./build.sh ../functions/<your-function-name>` before `terraform init`.
    - `aws/lambda.tf`:
        1. Add `"<your_function_name>"` to the function_names array.
        2. Add the path of the zip file to the function_paths array (normally this should be: `"tmp/<your_function_name.zip"`)
        3. Add `"python3.8"` to function_runtimes.
        4. Add `"lambda_function.lambda_handler"` to function_handlers.
        5. Add `[aws_lambda_layer_version.<your_layer_name>.arn]` if you need custom dependencies or otherwise `[]` to function_layers. Your locals block should now look similar to this:
            ```
            locals {
                function_names = ["template-node","template-python","<your_function_name>"]
                function_paths = ["tmp/template-node.zip","tmp/template-node.zip","tmp/<your_function_name.zip"]
                function_runtimes = ["nodejs14.x","python3.8","python3.8"]
                function_handlers = ["index.handler","lambda_function.lambda_handler","lambda_function.lambda_handler"]
                function_layers = [[],[],[aws_lambda_layer_version.<your_layer_name>.arn]]
            }
            ```
        6. Add a new `aws_api_gateway_deployment` block:
            ```
            resource "aws_api_gateway_deployment" "example<index_in_function_names_array>" {
                depends_on = [
                    aws_api_gateway_integration.lambda[<index_in_function_names_array>],
                    aws_api_gateway_integration.lambda_root[<index_in_function_names_array>],
                ]

                rest_api_id = aws_api_gateway_rest_api.example[<index_in_function_names_array>].id
                stage_name  = local.function_names[<index_in_function_names_array>]
            }
            ```
        7. Add a new output block at the end of `aws/lambda.tf`:
            ```
            output "url_<your-function-name>" {
                value = aws_api_gateway_deployment.example<index_in_function_names_array>.invoke_url
            }
            ```