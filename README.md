# Fit app

Just one more simple web app for fitness

## Features

- **Food list**: list of stored ingredients indicating the number of calories per 100 g.
- **Calories calculator**: TODO


## Installation

1. Clone repo:
   ```bash
   git clone https://github.com/Sigmadsen/fitapp.git
2. Install Docker
3. Copy .env_example and save as .env file
4. Set up your creds in .env file
5. Build and up docker container with docker-compose
6. Run migrations inside the docker container:
    ```bash
   docker-compose exec web python manage.py migrate