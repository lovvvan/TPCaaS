# TPCaaS
Twitter Pronoun Counter as a Service (TPCaaS) is a cloud service which counts the number
of times the swedish pronouns “han”, “hon”, “den”, “det”, “denna”, “denne” and “hen” occurs
in a fixed set of tweets.

## System Design
The TPCaaS consists of one celery worker with rabbitmq as the broker, and a flask REST
API that handles the requests. When a user requests the service, a request is sent to the
Flask REST API residing in the file “pronoun_counter.py”. The pronoun_counter then runs
the “run_task.py” file. Here the method “pronoun_count” from the celery tasks is being
called. The celery worker starts counting pronouns in an asynchronous call with the delay
method. The REST API waits for the response and outputs the result when it is ready.

## Setup 
The service is deployed by creating a VM instance with a python automation script and
contextualized with a cloud init text file and attaching a floating ip manually. During the
booting process several programs are being installed such as celery, rabbitmq, flask, and git,
and the python scripts responsible for the Twitter Pronoun Counter REST API application are
created. Rabbitmq, celery and the scripts that make up the TPCaaS are then started.

To start the service, first clone the github repo:

´´´shell
git clone https://github.com/lovvvan/TPCaaS.git
´´´
