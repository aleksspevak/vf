import csv

def get_group_users(vk,id_group):
    off = 0
    group_users = []
    while True:
        get_users = vk.groups.getMembers(group_id=id_group, offset=off)
        group_users = group_users + get_users.get('items')
        off += 1000
        if get_users.get('count') < off:
            break
    return group_users

def user_filter(vk,group_users):
    mud_users=[]
    for i in group_users:
        person = vk.users.get(user_id=i, fields='counters')
        if person[0].get('can_access_closed') == False :
            mud_users.append(i)
        elif person[0].get('is_closed') == True :
            mud_users.append(i)
        elif person[0].get('deactivated') == 'deleted':
            mud_users.append(i)
        elif person[0].get('deactivated') == 'banned':
            mud_users.append(i)
    for i in mud_users:
        group_users.remove(i)
    return group_users

def get_common_friend_list(vk,group_users):
    friend_list_end = []
    set_users = set(group_users)
    for i in group_users:
        user_friend_list = vk.friends.get(user_id=i)
        lists_friend = user_friend_list['items']
        lists_friend = set(lists_friend)
        lists_friend = lists_friend & set_users
        lists_friend = list(lists_friend)
        friend_list_end.append(lists_friend)
    return friend_list_end

def get_user_information(vk,group_users,friend_list,gi):
    user_information = []
    fieldss = ['group_id','id','first_name','last_name','bdate','city','home_town',
              'education','nfriends','nfollowers','ncommon',
              'about','activities','books','games','interests']
    user_information.append(fieldss)

    for i in range(len(group_users)):
        # group_users[i] = int(group_users[i])
        print(group_users[i])
        person_info = vk.users.get(user_id=group_users[i],
                              fields='first_name,last_name,about,bdate,books,'
                                     'activities,city,education,'
                                     'games,home_town,counters,interests')
        person_inf = person_info[0]
        print(person_inf)
        clean_person_inf = []
        for key in fieldss:
            if key == 'city' and key in person_inf:
                print(person_inf.get(key))
                if 'id' in person_inf.get(key):
                    clean_person_inf.append(person_inf.get(key).get('id'))
            elif key=='id':
                clean_person_inf.append(group_users[i])
            elif key=='group_id':
                clean_person_inf.append(gi)
            #elif key == 'phone' and 'contacts' in person_inf:
            #    if 'mobile_phone' in person_inf.get('contacts'):
            #        clean_person_inf.append(person_inf.get('contacts').get('mobile_phone'))
            #    else:
            #        clean_person_inf.append('')
            elif key == 'education' and 'university' in person_inf:
                clean_person_inf.append(person_inf.get('university'))
            #elif key in ['company_name','position','company_country','from','until'] and 'career' in person_inf :
            #   if key in person_inf.get('career'):
            #        clean_person_inf.append(person_inf.get('career').get(key))
            #    else:
            #        clean_person_inf.append('')
            elif key=='nfriends' and 'counters' in person_inf:
                if 'friends' in person_inf.get('counters'):
                    clean_person_inf.append(person_inf.get('counters').get('friends'))
                else:
                    clean_person_inf.append('')
            elif key=='nfollowers' and 'counters' in person_inf:
                if 'followers' in person_inf.get('counters'):
                    clean_person_inf.append(person_inf.get('counters').get('followers'))
                else:
                    clean_person_inf.append('')
            elif key=='bdate' and 'bdate' in person_inf:
                if len(person_inf.get('bdate'))<6:
                    a=str(person_inf.get('bdate'))+'.0000'
                    a=a.translate(str.maketrans('.', '/'))
                    clean_person_inf.append(a)
                else:
                    a = str(person_inf.get('bdate'))
                    a = a.translate(str.maketrans('.', '/'))
                    clean_person_inf.append(a)
            elif key=='ncommon':
                clean_person_inf.append(len(friend_list[i]))
            elif key in person_inf:
                clean_person_inf.append(person_inf.get(key))
            else:
                clean_person_inf.append('')
        user_information.append(clean_person_inf)
        print(clean_person_inf)
    return user_information

def saveinf(name,this):
    with open('%s.csv'%name, "w", newline="", encoding="utf-8" ) as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerows(this)

def saveinf1(name,this):
    with open('%s.txt'%name, "w", newline="", encoding="utf-8" ) as file:
        b=''
        for i in this:
            b=b+str(i)+','
        b=b[:-1]
        file.write(b)

def getinf(name):
    table = []
    csvFile = open('%s.csv'%name, "r",newline="",encoding="utf-8" )
    for row in csv.reader(csvFile,delimiter=';'):
        table.append(row)
    csvFile.close()
    return table

def getinf1(name):
    file = open('%s.txt'%name, "r", encoding="utf-8" )
    f=file.read()
    f.split(sep=',')
    return f
