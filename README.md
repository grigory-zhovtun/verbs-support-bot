# Verbs Support Bot

Telegram and VK bots powered by Google DialogFlow for automated customer support. The bots recognize user intents and provide intelligent responses to frequently asked questions.

## Features

- Dual platform support: Telegram and VKontakte
- Natural language understanding via Google DialogFlow
- Automatic intent recognition with fallback handling
- VK bot stays silent on unknown queries (letting human operators respond)
- Training script for bulk intent creation from JSON

## Prerequisites

- Python 3.8 or later
- Google Cloud account with DialogFlow API enabled
- Telegram Bot Token (from @BotFather)
- VK Community Token with messaging permissions

## Installation and Setup

Clone the repository or download the scripts:

```bash
git clone <repository-url>
cd verbs-support-bot
```

(Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

Install dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

Configure environment variables:

Create a `.env` file in the project root directory and define the required variables.

### Required Environment Variables

| Variable | Description |
|----------|-------------|
| `TG_TOKEN` | Telegram Bot API token from @BotFather |
| `VK_TOKEN` | VK Community token with messaging permissions |
| `PROJECT_ID` | Google Cloud project ID for DialogFlow |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to Google Cloud service account JSON file |

Example `.env` file:

```
TG_TOKEN=your_telegram_bot_token_here
VK_TOKEN=your_vk_community_token_here
PROJECT_ID=your-dialogflow-project-id
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```

## Usage

Run Telegram bot:

```bash
python tg_bot.py
```

Run VK bot:

```bash
python vk_bot.py
```

Train DialogFlow intents from JSON file:

```bash
python train_dialogflow.py
```

## Project Structure

| File | Description |
|------|-------------|
| `tg_bot.py` | Telegram bot implementation |
| `vk_bot.py` | VKontakte bot implementation |
| `dialogflow_api.py` | DialogFlow API wrapper functions |
| `train_dialogflow.py` | Script for bulk intent training |
| `questions.json` | Training data with intents and responses |
