
# Tilavihkutin

Amatsooni-seittijumalanpalvelus: Osavaltioruumiinosantoiminnot


## Prerequisites

    sudo npm install -g serverless
    npm install

## Deploy

    sls deploy

## Step Functions 101

A *state machine* is a collection of *states*, described with a *definition* written in [ASL](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html).

State types: Task, Choice, Wait, Fail, Pass, Succeed, Parallel.

An *execution* runs the state machine. Execution may provide input data for the machine.


TODO: *activities* allow running tasks on EC2 instances, ECS services etc.
