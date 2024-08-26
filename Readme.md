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
    - Test the webchat widget at `http://localhost:8081/test.html`.

## Post-Setup Instructions

Once the setup is complete, follow these steps:

1. In the Rasa X interface, navigate to the **Training -> NLU data** section and upload the `nlu.yml` file from the `data/` directory to populate your NLU data.

2. Go to the **Training -> Domain** section and upload the `domain.yml` file from the `data/` directory to set up your domain configuration.

3. In the **Training -> Rules** section, upload the `rules.yml` file from the `data/` directory to define your conversation rules.

4. For the **Training -> Configuration** section, open the `configuration.yml` file from the `data/` directory, copy its contents, and paste them into the configuration section in Rasa X, then save it.

5. After adding or updating your data, navigate to the **Models** section and click on **Add Model** -> **Train Model** to train your model.

6. Once the model is trained, you can activate it from the **Models** section.

## Usage

- Add your custom actions in the `actions/` directory and modify the Dockerfile as needed.
- Manage and train your models via the Rasa X interface.

## Contributing

If you'd like to contribute, please submit a pull request or open an issue.

---

This README provides all the steps and details needed to start using the project.
