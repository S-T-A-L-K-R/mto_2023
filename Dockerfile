FROM python:3.8.16-slim-buster

CMD ["bash"]
RUN apt update
RUN apt install -y git-all
RUN apt install make
RUN apt install build-essential