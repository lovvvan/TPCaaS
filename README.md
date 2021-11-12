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

To start the service, first clone the github repo
```shell
git clone https://github.com/lovvvan/TPCaaS.git
```

Then create a new key pair with the following command and name it "beancloud"
```shell
ssh-keygen -b 2048 -t rsa
```

Save the public key file under Compute -> Key pairs -> import key pair on openstack web
page.

Download the API Access - the openstack RC file from the web page and source it
```shell
source <name_of_API_access_file>
```

Navigate into the TPCaas folder and create the instance by running the command:
```shell
python ssc-instance-userdata.py
```

This will take a few seconds. After you get a printing statement back in the terminal saying
that the instance is in ACTIVEstate you open the openstack web page and attach a floating
ip manually to the instance.
The service is then good to go as long as the instance had enough time to install the
programs from the booting process (that can take a while so to be safe you can wait about
15 min).

## Usage

The user can then access the service by running the following command in a terminal with
your floating ip instead of “<your-floating-ip>”
 ```shell
curl -i http://<your-floating-ip>:5000/pronoun_counter
```
  
After waiting for the celery worker to count the pronouns (roughly about 2.5 minutes) the
TPCaaS will give the user the output seen below.
  
  ![Bar chart showing the numbers of times the different pronouns occur in the tweets](https://github.com/lovvvan/TPCaaS/blob/main/ResultFromTPCaaS.PNG?raw=true)


