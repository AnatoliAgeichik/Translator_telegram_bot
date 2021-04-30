FROM python

COPY app/connect_db.py bot/app/
COPY app/handle_msg.py bot/app/
COPY database/admin.py bot/database/
COPY database/create_database.sql bot/database/
COPY database/create_table.sql bot/database/
COPY requirements.txt bot/requirements.txt
COPY .env bot/.env
WORKDIR bot
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
