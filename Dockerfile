FROM ubuntu
RUN apt-get update
RUN apt-get -y upgrade 
RUN apt-get install -y git 
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install flask
WORKDIR /home/ubuntu
RUN git clone https://github.com/lovvvan/TPCaaS.git
WORKDIR TPCaaS/app
RUN git clone https://github.com/lovvvan/tweet_pronoun_files.git
RUN pip install celery
RUN pip install termgraph
RUN pip install flower
WORKDIR /home/ubuntu/TPCaaS/app
EXPOSE 5000
ENV PATH="${PATH}:/usr/games/"
CMD ["python3","pronoun_counter.py"]