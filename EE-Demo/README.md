[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# EE-Demo
This repository provides the opportunity to quickly set up the Apollo Runtime system to observe the (visualized) orchestration of simple example workflows.

## Demonstrations

This project contains a series of demonstrations with varying prerequisites. The entry for each demonstration is annotated with a link to a readme containing more detailed setup instructions.

Demonstration | Prerequisites | Readme Link | Youtube Link
--------------|---------------|-------------| -------------
Basic Functionality and GUI | - Java (11+) <br> - Gradle | [Basic Functionality](https://github.com/Apollo-Core/EE-Demo/tree/master/documentation/BasicFunctionality) | [Basic Functionality](https://www.youtube.com/watch?v=KFoT99tpJBk)


## Prerequisites

## Running the Demo.

1. Clone the repository.

2. Using the terminal, switch to the directory containing the `build.gradle` file and run `gradlew build` to automatically download the dependencies and build the project.

3. Run the command `gradlew run` to start Apollo's configuration GUI.

4. Click the "Load" button and load any of the configurations from the `configs/` folder of the project, e.g., `singleAtomicConfig.xml`.

5. Click the "Run" button.

