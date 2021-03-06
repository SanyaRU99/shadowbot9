import os
import utils
import ast

ver_msg = 'Shadow Bot by YBAR community'

isHerokuInstance = True
message_delay = 0.3

if isHerokuInstance:
    community_token = os.environ.get('vk_api_token')
    group_id = int(os.environ.get('vk_group_id'))
    message1 = utils.adjust_message_text(os.environ.get('message1'))
    message2 = utils.adjust_message_text(os.environ.get('message2'))
    message3 = utils.adjust_message_text(os.environ.get('message3'))
    msgs = [message1, message2, message3]
    controllers = ast.literal_eval(os.environ.get('admins'))

else:
    community_token = "xyi"  # group token
    group_id = 196979388  # vk group id without club
    message1 = utils.adjust_message_text("pwned.solution test msg1")
    message2 = utils.adjust_message_text("pwned.solution test msg2")
    message3 = utils.adjust_message_text("pwned.solution test msg3")
    msgs = [message1, message2, message3]
    controllers = [331320136]  # admins list
