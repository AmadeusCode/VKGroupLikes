# -*- coding: utf-8 -*-
config = {
    'login'             :   'YOUR_LOGIN',       # Your VK login
    'password'          :   'YOUR_PASSWORD',    # Your VK password
    'token'             :   'YOUR_TOKEN',       # Your VK token
    'group_id'          :    -1,		# Group id Like -xxxxxxxxx
    'count_last_posts'  :    1,	                # Count of last posts to be liked
    'liked_last_posts'  :    True,			    # Procedure of Liked Last Count of Wall Posts. | True or False
    'liked_new_posts'   :    False,		        # Start deamon to liked new group post.        | True or False
    'cooldown_like'     :    1,                 # Cooldown between liked last group posts in seconds. !Very low cooldawn may cause captcha error
    'cooldown_check'    :    360                # Cooldown between check new posts from group in seconds.
}
