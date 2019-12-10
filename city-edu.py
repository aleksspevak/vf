import vk_api
from mydata import vkdata
import vf

vk_session = vk_api.VkApi(vkdata.login, vkdata.password)
vk_session.auth()
vk = vk_session.get_api()

city = [['id','title']]
for i in range(20):
    l = [p for p in range(i*1000,(i+1)*1000)]
    name1 = vk.database.getCitiesById(city_ids=l)
    for name in name1:
        city1 = []
        if len(name.get('title')) > 0:
            city1.append(name.get('id'))
            city1.append(name.get('title'))
            city.append(city1)
vf.saveinf('city',city)

edu=[['id','title']]
for i in city:
    name1 = vk.database.getUniversities(city_id=i[0])
    for name in name1.get('items'):
        edu1 = []
        if len(name.get('title')) > 0:
            edu1.append(name.get('id'))
            edu1.append(name.get('title'))
            edu.append(edu1)
vf.saveinf('edu',edu)
print(edu)
