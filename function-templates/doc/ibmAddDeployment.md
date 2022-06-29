# Add a function to auto deployment for IBM
We need to adjust `ibm/ibm.tf` and `ibm/deployment.sh` to add a new function to the auto deployment.
- Node:
    - `ibm/deploy.sh`:
        1. Add `./build.sh --installNode ../functions/<your-function-name>` if you need custom dependencies or otherwise `./build.sh ../functions/<your-function-name>` before `terraform init`
    - `ibm/lambda.tf`:
        1. Add `"<your-function-name>"` to the `node_functions` array. Your locals block should now look similar to this:
            ```
            locals {
                node_functions = ["template-node","<your-function-name>"]
                function_docker_names = ["template-python"]
                function_docker_images = ["ibmfunctions/action-python-v3.7"]
            }
            ```
        2. Add a new output block at the end of `ibm/ibm.tf`:
            ```
            output "url_<your-function-name>" {
                value = "${ibm_function_action.functions_docker[<index_in_node_functions_array>].target_endpoint_url}.json"
            }
            ```
- Python:
    - `ibm/deploy.sh`:
        1. Add `./build.sh ../functions/<your-function-name>` before `terraform init`
    - `ibm/lambda.tf`:
        1. Add `"<your-function-name>"` to the `function_docker_names` array.
        2. Add `<your_docker_hub_username>/<layer-name>` if you need custom dependencies or otherwise `"ibmfunctions/action-python-v3.7"` to `function_docker_images` array. Your locals block should now look similar to this:
            ```
            locals {
                node_functions = ["template-node"]
                function_docker_names = ["template-python","<your-function-name>"]
                function_docker_images = ["ibmfunctions/action-python-v3.7","<your_docker_hub_username>/<layer-name>"]
            }
            ```
        3. Add a new output block at the end of `ibm/ibm.tf`:
            ```
            output "url_<your-function-name>" {
                value = "${ibm_function_action.functions_docker[<index_in_function_docker_names_array>].target_endpoint_url}.json"
            }
            ```