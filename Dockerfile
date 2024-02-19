# SET BASE IMAGE OS
FROM python:3.12-alpine3.18

# UPDATE AND INSTALL GIT, BUILD ESSENTIAL
RUN apk update && apk add --no-cache git build-base

# CLONE REPOSITORY
RUN git clone https://github.com/alaskanlearner/gadja-v6.1 /home/fsub  ; chmod 777 /home/fsub ; chmod 777 /home/fsub

# WORKDIR
WORKDIR /home/fsub

# SET GIT CONFIG
RUN git config --global user.name "alaskanlearner"
RUN git config --global user.email "alif.jogja016@gmail.com"

# IGNORE PIP WARNING 
ENV PIP_ROOT_USER_ACTION=ignore

# UPDATE PIP
RUN pip install -U pip
RUN pip install -U requests
# INSTALL REQUIREMENTS
RUN pip install -U \
                --no-cache-dir \
                -r requirements.txt

# COMMAND TO RUN
CMD ["python", "main.py"]