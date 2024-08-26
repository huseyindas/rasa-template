# Rasa X Chatbot Template

This repository provides a quick setup for a chatbot development environment integrating Rasa X, Rasa SDK, Duckling, and Nginx using Docker Compose. The template includes a configuration for custom actions, a Rasa webchat widget, and the Rasa X interface.

## Contents

- `docker-compose.yml`: Configures the Docker containers for Rasa X, Rasa SDK, Duckling, and Nginx.
- `actions/`: Contains custom actions. This folder includes a Dockerfile to build the custom actions container.
- `test.html`: A simple HTML file containing the Rasa webchat widget.
- `.env.example`: Example environment variables file. Copy this to `.env` and fill in the required values before starting the system.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/username/repo-name.git
    cd repo-name
    ```

2. Copy `.env.example` to `.env` and populate it with the required values:
    ```bash
    cp .env.example .env
    ```

3. Build and start the Docker containers:
    ```bash
    docker-compose up --build -d
    ```

4. Set the necessary permissions:
    ```bash
    sudo chown -R 1001:1001 database/ models/
    ```

5. After setup:
    - Access the Rasa X interface at `http://localhost:8080`.
    - Test the webchat widget at `http://localhost:8081/`.

## Usage

- Add your custom actions in the `actions/` directory and modify the Dockerfile as needed.
- Manage and train your models via the Rasa X interface.

## Contributing

If you'd like to contribute, please submit a pull request or open an issue.

---

This README provides all the steps and details needed to start using the project.
