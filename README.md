# Reddit Groq Bot

This project is a Reddit bot that uses Groq AI to generate and post content automatically. The bot also has the capability to comment on top posts in a specified subreddit.

## Features

- **Automated Posting**: Posts AI-generated content to Reddit at user-specified intervals.
- **Groq AI Integration**: Uses Groq AI to generate engaging content and comments.
- **Error Handling**: Includes basic error handling and logging for seamless operation.
- **Commenting**: Automatically comments on the top posts in the subreddit.

## Requirements

- Python 3.7+
- Reddit account
- Groq API key

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd reddit_groq_bot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
   Create a `.env` file in the project root and add the following variables:
   ```
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USERNAME=your_username
   REDDIT_PASSWORD=your_password
   REDDIT_USER_AGENT=your_user_agent
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Run the bot:**
    ```bash
    python reddit_bot.py
    ```

## Usage

### Posting to Reddit

The bot generates content using a prompt and posts it to a subreddit. You can configure the subreddit and post interval by modifying the `POST_INTERVAL_HOURS` and `post_to_reddit` function.

### Commenting on Posts

The bot automatically generates comments using Groq AI and replies to the top posts in a specified subreddit.

### Scheduling

Posts are scheduled at intervals defined by `POST_INTERVAL_HOURS` (default is 6 hours).

## File Structure

- `reddit_bot.py`: Main bot script containing all functions and logic.
- `requirements.txt`: Dependencies required to run the bot.

## Functions Overview

### `generate_content(prompt)`
Generates content using Groq AI based on the provided prompt.
- **Args:**
  - `prompt` (str): The prompt to guide Groq AI.
- **Returns:**
  - `content` (str): The body text of the post.
  - `title` (str): The title of the post.

### `post_to_reddit(subreddit_name, content, title)`
Posts the generated content to Reddit.
- **Args:**
  - `subreddit_name` (str): The subreddit to post to.
  - `content` (str): The body text of the post.
  - `title` (str): The title of the post.

### `schedule_posts()`
Schedules posts to Reddit at regular intervals.

### `comment_on_posts(subreddit_name)`
Comments on the top posts in a specified subreddit.
- **Args:**
  - `subreddit_name` (str): The subreddit to comment on.

## Example Prompt

```text
Generate content for the post on AI development with 'title' and 'text' as the key fields.
```

## Dependencies

- `praw`: Python Reddit API Wrapper.
- `groq`: Groq AI Python SDK.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Feel free to fork the repository and submit pull requests to improve the project.

