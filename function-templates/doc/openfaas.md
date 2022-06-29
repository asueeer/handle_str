# OpenFaaS Functions

Apollo gives us the possibility to execute functions locally by using a Docker image. It supports function images written in the "OpenFaaS" style. Those functions use a specific template provided by OpenFaaS and are built using the [`faas-cli`](https://github.com/openfaas/faas-cli).

Before you begin building the functions, **make sure** that `faas-cli` and Docker are installed and available.
Adjust the file `openfaas/stack.yml` to include any newly generated functions.

The following parameters have to be set in the `.yml` file:

- `lang`: Describes the base template used by OpenFaaS. This should be equal to the value of the copied function.
- `handler`: The path to the function folder
- `image`: The Docker image name and tag. Include a Docker ID if you intend to push the image to a registry.

## Building

Build the function images by running the provided script in the `openfaas` directory:

```sh
./build.sh
```

Using the `-f` or `--file` flag, a filename can be supplied to match only a single `.y*ml` file describing functions (passing `-f stack` would search the directory using `stack.y*ml`).
All files matching `*.y*ml` are used per default to find function descriptions. The `-p` or `--publish` flag can be supplied to also push the built functions to a container registry.

## Type Mappings File
Adjust the provided template `typeMappings.json` by creating one function block for each of your functions and editing their function type and image name.
