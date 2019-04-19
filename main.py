# -*- coding: utf-8 -*-
#   Import standart libraries and vk_api
import requests, time, config, datetime
#   Install vk_api from pip
from os import system
try:
    import vk_api
except ImportError:
    print('Installing VK_API ...')
    system('pip install vk_api')
    import vk_api
#   Import config data
config = config.config
__version__ = 0.2
last_post_from_group = 0
print('Starting VKGroupLikes ...')
#   function start VK session
def vk_login():
    if config.get('token') != ('' or 'YOUR_TOKEN'):
        print('Successful login with token')
        vk_session = vk_api.VkApi(token=config.get('token'))
    elif (config.get('login') != ('' or 'YOUR_LOGIN') and config.get('password') != ('' or 'YOUR_PASSWORD')):
        print('Successful login')
        vk_session = vk_api.VkApi(config.get('login'), config.get('password') )
        vk_session.auth()
    elif config.get('group_id') == ('' or 'YOUR_GROUP_ID'):
        print('Please set group id')
        exit()
    else:
        print("You have not provided a login and password or token.\nLogin like: email or +7xxxxxxxxxx")
        exit()
    vk = vk_session.get_api()
    return vk
#   function check was there a post have like(return True or False)
def is_liked(post_id):
    if (vk.likes.isLiked(type = 'post', owner_id = config.get('group_id'), item_id = post_id)['liked']) == True:
        return True
    else:
        return False
#   function check last id(-1) post from group. (-1)id Because group may be have fixed post. return number
def get_last_id():
    last_id = vk.wall.get(owner_id = config.get('group_id'), count = 10)['items'][1]['id']
    return last_id
#   function return str current time
def get_time():
    today = datetime.datetime.today()
    return today.strftime("%H:%M:%S")
#   function liked last n posts
def last_posts(last_post, count):
    start_post = last_post - count
    last_post += 1; start_post += 1;
    time_start = time.time()
    print('{} Last Post is {}'.format(get_time(), str(get_last_id())) )
    for id in range(start_post, last_post):

            if is_liked(id) == False:
                try:
                    vk.likes.add(type = 'post', owner_id = config.get('group_id'), item_id = id)
                    print('{} Liked post {}'.format(get_time(), str(id)) )
                except vk_api.exceptions.ApiError:
                    print('{} Post Deleted {}'.format(get_time(), str(id)) )
                except vk_api.exceptions.ApiHttpError:
                    print( get_time() + ' Network Error')
            else:
                print(get_time() + ' Post Already Liked ' + str(id))
            time.sleep(config.get('cooldown_like'))
            result_time = time_start - time.time()
    print('{} All Done in {} seconds'.format(get_time(), str(abs(round(result_time, 3)))) )
    global last_post_from_group; last_post_from_group = id
#   function Liked all new posts
def new_posts():
    global last_post_from_group
    if last_post_from_group == 0:
        last_post_from_group = get_last_id()
    while True:
        if get_last_id() != last_post_from_group and not is_liked(get_last_id()):
            try:
                vk.likes.add(type = 'post', owner_id = config.get('group_id'), item_id = get_last_id())
                print( get_time() + ' Liked New Post!')
                last_post_from_group = get_last_id()
            except vk_api.exceptions.ApiError:
                print('{} Post Deleted {}'.format(get_time(), str(get_last_id())) )
                last_post_from_group = get_last_id()
            except vk_api.exceptions.ApiHttpError:
                print( get_time() + 'Network Error')
        else:
            print('{} All new posts liked, waiting {} seconds'.format(get_time(), config.get('cooldown_check')))
            time.sleep(config.get('cooldown_check'))
# Start Script and select mode
if __name__ == "__main__":
    vk = (vk_login())
    if config.get('liked_last_posts'):
        last_posts(get_last_id(), config.get('count_last_posts'))
    else:
        print('Edit config and select between liked_last_posts or liked_last_posts\nP.S Possible choose both')
    if config.get('liked_last_posts'):
        new_posts()
    else:
        print('Edit config and select between liked_last_posts or liked_last_posts\nP.S Possible choose both')
