# ABOUT THIS REPO
This is a Django-based admin panel for the message distributor. The built-in Django admin dashboard is used to manage
projects and integrations with SMTP.BZ and Telegram and any other systems implemented in the future.

Languages supported:
- English
- Russian

# SETUP
The project uses MySQL database connection implemented via [mysqlclient](https://pypi.org/project/mysqlclient/) package.
Should any other SQL connection be used, additional packages should be installed.

- install project requirements listed in requirements.txt
- set database connection requisites in rabbit_admin/settings.py

If fresh DB connection is used:
- run migrations
- create superuser with Django ```createsuperuser``` command

Access the dashboard via root ```/``` route.

# PROJECT SUMMARY
This project is a set of microservices for distribution of an initial message with all kinds of services:
Telegram, E-mail or any other service as deemed necessary, including plain HTTP requests.

The idea of the project is to allow a user to set up a project with desirable endpoints and to send a message only once
to distribute it, including any media attached thereto.

The project utilizes [RabbitMQ](https://www.rabbitmq.com/) for message distribution.

The project consists of a receiver microservice to JSON-encode the initial text and attachments, and a dispatcher microservice to push the message into the project-related queues for further processing:

```
                                              --> endpoint microservice #1
                                              |    
incoming message --> receiver --> dispatcher ---> endpoint microservice #2
                                              |
                                              --> endpoint microservice #3 
```

The final distribution is performed by endpoint microservices, each implemented depending on capabilities of the
system used. Use of [RabbitMQ](https://www.rabbitmq.com/) allows to deploy as many clones of an endpoint microservice as
required in case if such channel is used extensively.

[Dashboard](https://github.com/PythonChoker/broker-admin)

Other microservices:

- [Receiver](https://github.com/PythonChoker/broker-receiver)
- [Dispatcher](https://github.com/PythonChoker/broker-dispatcher)
- [SMTP BZ Sender](https://github.com/PythonChoker/broker-smtp-bz)
- [Telegram Sender](https://github.com/PythonChoker/broker-telegram)