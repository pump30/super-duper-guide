import requests
import json
import wordcloud
import matplotlib.pyplot as plt

# 1.请求数据


url = "https://api.yimian.xyz/coro"
data = requests.get(url).text

# 2.解析数据
city_dict = {}
json_data = json.loads(data)
print(len(json_data))
for p in json_data:
    if 'cites' in p:
        for c in p["cities"]:
            cityName = c["cityName"]
            cCount = c['confirmedCount']
            sCount = c['suspectedCount']
            total = int(cCount) + int(sCount)
            city_dict[cityName] = total
    else:
        cityName = p["provinceName"]
        cCount = p['confirmedCount']
        sCount = p['suspectedCount']
        total = int(cCount) + int(sCount)
        city_dict[cityName] = total
print(city_dict)

# 3.写入文件
with open('city_count.txt', 'w') as f:
    for k, v in city_dict.items():
        f.write(f'{k}:{v}\n')

# 3.生成词云
#ccloud = wordcloud.WordCloud(background_color='white', width=2000, height=1000,
                          #   font_path='C:\Windows\Fonts\微软雅黑\msyhbd.ttc')
#ccloud.generate_from_frequencies(frequencies=city_dict)

#plt.figure()
#plt.imshow(ccloud, interpolation='bilinear')
#plt.axis('off')
#plt.show()

#4.生成爱心词云
import numpy as np
import PIL

heart_mask=np.array(PIL.Image.open('heart.png'))
ccloud = wordcloud.WordCloud(background_color='white', mask=heart_mask,width=2000, height=1000,
                             font_path='C:\Windows\Fonts\微软雅黑\msyhbd.ttc')
ccloud.generate_from_frequencies(frequencies=city_dict)

plt.figure(dpi=2000)
plt.imshow(ccloud, interpolation='bilinear')
plt.axis('off')
plt.show()