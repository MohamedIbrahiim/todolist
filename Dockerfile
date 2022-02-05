# pull official base image
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y netcat


# copy project
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


COPY entrypoint.sh /code/
RUN chmod +x  /code/entrypoint.sh
## collect static
##RUN python manage.py collectstatic --no-input
#
ENTRYPOINT ["sh", "/code/entrypoint.sh"]