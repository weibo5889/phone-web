import googlemaps
import pandas
import json 
import os

api_key = os.environ.get('MAP_token')
gmaps = googlemaps.Client(key=api_key)

#取得台南火車站的地理編碼
geocode_result = gmaps.geocode("汐止火車站")
#取得經緯度
loc = geocode_result[0]['geometry']['location']
rad = input("輸入範圍: ")

result = gmaps.places_nearby(keyword="餐廳", location=loc, radius=rad, language="zh-TW")
restaurants = result['results']

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

if restaurants:
     with open('results.txt', 'w', encoding='utf-8') as f:
        f.write("附近的餐厅有：\n")
        for restaurant in restaurants:
            name = restaurant.get('name', 'Unknown')
            place_id = restaurant.get('place_id', 'Place ID not available')
            
            # 构建餐厅的Google地图链接
            if place_id != 'Place ID not available':
                restaurant_link = "https://www.google.com/maps/place/?q=place_id:{}".format(place_id)
                f.write("{} - {}\n".format(name, restaurant_link))


#用gmaps.places_radar這個代碼來查total有幾個結果
#print("台南火車站為中心"+str(rad)+"公尺的餐廳數量: "+str(len(gmaps.places_nearby(keyword="餐廳",location=loc, radius=rad)['results'])))
