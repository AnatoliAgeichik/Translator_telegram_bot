FROM python

COPY app bot/app/
COPY database bot/database/
COPY requirements.txt bot/requirements.txt
COPY .env bot/.env
WORKDIR bot
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
