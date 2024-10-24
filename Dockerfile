FROM python:3.12.6-slim

# install pipenv 
RUN pip install pipenv

# non-root user
RUN useradd -ms /bin/bash my-user

# establish the default user 
USER my-user

# command that will be executed
CMD ["tail", "-f", "/dev/null"]