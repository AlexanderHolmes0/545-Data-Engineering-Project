# 545 Group Project Repository

## Overview

Welcome to the 545 Group Project repository! This repository is dedicated to the DevOps and Data Engineering aspects of our project. Here, you will find everything you need to set up, manage, and deploy our project infrastructure and data pipelines

## Project Description

This repository is a part of our group project for course 545. Our project involves building a data-driven application that provides insights from a data source. The DevOps and Data Engineering team is responsible for managing the infrastructure, setting up data pipelines, and ensuring smooth data processing.

## Github Actions YAML Script

This script [main.yml](.github/workflows/main.yml) sets up a Python environment in a Microsoft Server Farm and runs `main.py` everyday day at midnight EST.

## Database Backup 

The backup of our database is run before new records are inserted at midnight EST every day. This is found in the file [backup.csv](backup.csv).

## Scraping Python 

The Python script that scrapes data from a website checks the data, and then inserts it into an Aiven database is in the file named [main.py](main.py).

## Meeting Notes

Meetings notes are contained in the file [Meetings.md](Meetings.md).

## Database Creation

SQL to create our `Feature_Store` table [DDL_Feature_Store.sql](DDL_Feature_Store.sql).

## API

Our example API is housed in the file [API.py](API.py).

## Requirements.txt

This is the requirements file for the `main.py` script to run [requirements.txt](requirements.txt).

## Dashboard

Dashboard file housed in [Dash.pbix](Dash.pbix)

## Group Contract 

[bonus-assignment-03.txt](bonus-assignment-03.txt)

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

---

Thank you for your interest in our 545 Group Project DevOps and Data Engineering repository. If you have any questions or encounter issues, please don't hesitate to reach out to the project maintainers.

Happy coding! 🚀
