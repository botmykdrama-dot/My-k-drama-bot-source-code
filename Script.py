class script(object):
    START_TXT = """
Hello {}, <b>I'm My K-Drama Bot</b>

Here you can download Korean Tv series. you can search Dramas Via inline. I can also add filters in telegram groups.  Just add me to your groups and enjoy 🎊

Tap Help 🆘 To get more informations

Powered by @myKdrama_botupdats
"""
    HELP_TXT = """
Here is the help foe my commands"""
    ABOUT_TXT = """✯ My Name: <code>My K-Drama Bot</code>
✯ Update on: <code>June 27, 2022</code>
✯ Library: <code>Pyrogram</code>
✯ Language: <code>Python 3</code>
✯ Database: <code>MongoDB</code>
✯ Srever: <code>Heroku</code>
✯ Build Status: <code>v2.5.5</code>"""
    SOURCE_TXT = """  """
    NOTE_TEXT = """
<b>My K-Drama Bot Special Notes:</b> 

If you want to use PM mod please join <b>My K-Drama Hub</b> or add me to your group and enjoy it

Sorry for inconvenience...
    """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. My K-Drama Bot should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>Add a filter in chat</code>
• /filters - <code>List all the filters of a chat</code>
• /del - <code>Delete a specific filter in chat</code>
• /delall - <code>Delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- My K-Drama Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. My K-Drama Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/myKdrama_botupdats)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>Connect a particular chat to your PM</code>
• /disconnect  - <code>Disconnect from a chat</code>
• /connections - <code>List all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of My K-Drama Bot.

<b>Commands and Usage:</b>
• /id - <code>Get id of a specified user.</code>
• /info  - <code>Get information about a user.</code>
• /imdb  - <code>Get the film information from IMDb source.</code>
• /search  - <code>Get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for admins.

<b>Commands and Usage:</b>
• /logs - <code>To get the rescent errors</code>
• /stats - <code>To get status of files in db.</code>
• /delete - <code>To delete a specific file from db.</code>
• /users - <code>To get list of my users and ids.</code>
• /chats - <code>To get list of the my chats and ids </code>
• /leave  - <code>To leave from a chat.</code>
• /disable  -  <code>Do disable a chat.</code>
• /ban  - <code>To ban a user.</code>
• /unban  - <code>To unban a user.</code>
• /channel - <code>To get list of total connected channels</code>
• /broadcast - <code>To broadcast a message to all users</code>"""
    STATUS_TXT = """<b>My K-Drama Bot Stats</b> 📊

 ★ Total Files \t: <code>{}</code>
 ★ Total Users \t: <code>{}</code>    
 ★ Total Chats \t: <code>{}</code>
 ★ Used Storage\t: <code>{}</code>
 ★ Free Storage\t: <code>{}</code>
 
 ╭━ 💖━ 🤍━ 💖━ 🤍━ 💖
╰╮┏┳┳┳┓┏┳┳┳┳┓
┏┻╋╋┻┻┫┣┻╋╋┻┫
┗ⓞ┻┻━ⓞ┻┻ⓞ┻┻ⓞ┻
"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
 
