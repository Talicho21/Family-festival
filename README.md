# Family-festival

A Telegram bot that transforms photos into event posters with customized overlays and automatic face-centered cropping.

## Features
- **Automatic Face Detection & Framing**: Detects faces using OpenCV and centers the subject within the poster portrait area.
- **Dynamic Overlay**: Merges photos with the festival overlay template.
- **Fast & Responsive**: Async image processing using Pillow and OpenCV.
- **User Persistence**: Remembers users and processes incoming photos smoothly.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Talicho21/Family-festival.git
   cd Family-festival
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your bot token:**
   Create a `.env` file in the project root:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

5. **Run the bot:**
   ```bash
   python bot.py
   ```

