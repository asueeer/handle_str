# Create a custom AWS Python layer
If your python function requires dependencies, which are not included in the default AWS runtime, you need to create a custom AWS layer:
1. Create a copy of the `aws/layers/template-layer` and name it accordingly
2. Navigate to your copy of the folder from above.
3. Add all the required pip dependencies to `requirements.txt`.
4. Execute:
```
docker run -v "$PWD":/var/task "public.ecr.aws/sam/build-python3.8" /bin/sh -c "pip install -r requirements.txt -t python/lib/python3.8/site-packages/; exit"
```
5. Create a zip file with:
```
zip -r ../<your_layer_name>.zip python
```
6. Adjust `aws/lambda.tf`:
    1. Add a new layer to the terraform script:
        ```
        resource "aws_lambda_layer_version" "<your_layer_name>" {
            filename   = "./layers/<your_layer_name>.zip"
            layer_name = "<your_layer_name>"
            
            compatible_runtimes = ["python3.8"]
        }
        ```
    2. Follow [this](./awsAddDeployment.md) guide for the rest of the adjustments.