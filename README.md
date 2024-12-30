# PGRAM AUTOMATIC BOT

# Introduction

#### This Telegram bot allows you to send specific messages (entered by the administrator or a default message) to a specific chat.


# Setup


###### Before starting, you must rename the .env_example file to .env and fill in all the required fields


# Getting started


1. Clone the repository

```git clone https://github.com/SerhiiL06/forward-bot.git```


2. Change current repository

```cd forward-bot```

3. Create and activate virtual enviroment

```python -m venv venv  && source venv/bin/activate```

4. Run docker-compose 

```docker-compose up```

<br>

###### Before starting, you must 


# Features

##### The main class that implements the application logic is *TelethonService* (src/services/telethon_service.py). The following features are implemented in it:

<br>

<li>✅ Join to the channels / groups </li>
<li>✅ Start bots and forward message </li>
<li>✅ View posts</li>
<li>❌ Send reactions</li>
<li>❌ Boots channels</li>

<li> ✅ Sending GRAMs from all accounts to one </li>


<br>

##### All functions are implemented through celery-beat. You can see the schedule in the file core/celery.py. By default, tasks are launched every two hours. And tasks for the GRAMS sending are launched at 23:00 UTC.