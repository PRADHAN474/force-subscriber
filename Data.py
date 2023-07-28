from pyrogram.types import InlineKeyboardButton
from Config import BOT_USERNAME

class Data:
    # Start Message
    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {} 🥀✨

ɪ ᴄᴀɴ ғᴏʀᴄᴇ  ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴜsᴇʀ ᴛᴏ ᴊᴏɪɴ  ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ.
 ᴛʜᴇ ᴄʜᴀᴛ ᴄᴀɴ ʙᴇ ᴀ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ɪᴛ ᴄᴀɴ ᴘʀɪᴠᴀᴛᴇ ᴏʀ ᴘᴜʙʟɪᴄ.
 ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ʙᴀʙʏ !



    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="home")],
    ]

    # Rest Buttons
    buttons =[ [ InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
    InlineKeyboardButton("ᴀʙᴏᴜᴛ ", callback_data="about")
    ]
             ]
   
# Help Message
    HELP = """
𝟷) ᴀᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ᴀ ɢʀᴏᴜᴘ. 
𝟸) ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴀs ᴀᴅᴍɪɴ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ғᴏʀᴄᴇ ʏᴏᴜʀ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ. ɪᴛ ᴄᴀɴ ʙᴇ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ, ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴀᴛᴇ. 
𝟹) ᴜsᴇ /fsub chat_id /username ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ғᴜɴᴄᴛɪᴏɴᴀʟ. ᴜsᴇ /id ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴄʜᴀᴛ ɪᴅ.
 ᴇxᴀᴍᴘʟᴇ : /fsub -𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶 ᴏʀ /forcesubsribe -𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶 
𝟺) [ᴏᴘᴛɪᴏɴᴀʟ] ᴜsᴇ /settings ᴛᴏ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs! 
𝟻) ʏᴏᴜ ᴀʀᴇ ɢᴏᴏᴅ ᴛᴏ ɢᴏ. ʟᴇᴀᴠᴇ ᴛʜᴇ ʀᴇsᴛ ᴛᴏ ᴍᴇ.

 ✨ ᴀᴠᴀɪʟᴀʙᴇ ᴄᴍᴅs ʙᴀʙʏ  ✨ 
/start -  sᴛᴀʀᴛ ғᴏʀᴄᴇ sᴜʙsʀɪʙᴇ ʙᴏᴛ 
/fsub - sᴇᴇ ᴄᴜʀʀᴇɴᴛ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀᴛ 
/fsub chat_id/username- ғᴏʀᴄᴇ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ
/settings - ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs 
/id - ɢᴇᴛ ᴛʜᴇ ᴄʜᴀᴛ ɪᴅ ᴏғ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ
/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ 
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ 
☞︎︎︎ ɴᴏᴛᴇ - ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ /forcesubsribe ɪɴsᴛᴇᴀᴅ ᴏғ /fsub
"""

# About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ  ғᴏʀᴄᴇ sᴜʙ 


ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ :  [™°‌ 🫧 🇴 🇽 𝐘 𝐆 𝐄 𝐍](https://t.me/PRADHAN474)

ᴜᴘᴅᴀᴛᴇ   : [𐏓 ⃪༏‌⃪🔥᪵᪳🇧𝐀𝐖𝐀𝐍𝐃𝐄𝐑𝐋𝐎𝐊𐏓⃪༏‌⃪🔥᪵᪳❛🥀𓆪](https://t.me/BWANDARLOK)

ʀᴇᴘᴏ      :[ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ ](https://t.me/PRADHAN474)
    """
