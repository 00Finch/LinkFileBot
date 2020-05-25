# LinkPreviewBot

LinkFileBot is a Reddit bot, made using Praw which detects comments with embedded links and replies with a short blurb of information (e.g. title, website) on the linked site.

## Usage
### Main Usage
Use command
```bash
python3 LinkFileBot.py
```
to launch the script via a bash shell

OR

Use command 
```
python3 LinkFileBot.py > dev/null &
```
to run the script silently in the background

### Modules
*Content finder
This module accepts a link to a webpage as an argument and returns a description formatted for Reddit Markdown
  ```
  python3 ContentFinder.py <url_to_webpage>
 ```
 *NSFW
 This Module accepts a word as an argument and retuns `True` if NSFW content is detected
   ```
   python3 nsfw.py <word>
  ```
