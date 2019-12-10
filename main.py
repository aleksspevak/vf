import vk_api
from mydata import vkdata
import vf

vk_session = vk_api.VkApi(vkdata.login, vkdata.password)
vk_session.auth()
vk = vk_session.get_api()

file = open('iba', 'r')

group_id = file.read()

group_users = vf.get_group_users(vk,group_id)
# print(group_users)
clean_group_users = vf.user_filter(vk,group_users)
# print(clean_group_users)
# vf.saveinf1('group_users',clean_group_users)
#clean_group_users = vf.getinf1('group_users')

# friend_list = vf.get_common_friend_list(vk,clean_group_users)
# print(friend_list)
# vf.saveinf('friend_list',friend_list)
friend_list = vf.getinf('friend_list')
print(clean_group_users,friend_list)
users_information = vf.get_user_information(vk,clean_group_users,friend_list,group_id)
# print(users_information)
vf.saveinf('users_information',users_information)

users_information = vf.getinf('users_information')
