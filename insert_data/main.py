import threading
import time
import requests

API_URL = "http://127.0.0.1:3008"
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzQ3Mjk1NDI4LCJleHAiOjE3NDc5MDAyMjh9.fo4HKZWkxnLO1Du5oncvvyhHLab1J49lIQjrN8_0818"


def fetch_data():
    # 这里放置获取数据的逻辑
    print("正在获取数据...")
    # 模拟数据获取的延迟
    time.sleep(2)
    # 假设获取到的数据
    data = "获取到的数据"
    process_data(data)

def process_data(data):

    # 这里放置处理数据的逻辑
    print(f"处理数据: {data}")

def get_all_product_data():
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(API_URL+"/common/all/MProduct", headers=headers)

        # 检查响应状态
        response.raise_for_status()
        return response.json()  # 返回 JSON 格式的响应
    except requests.exceptions.HTTPError as err:
        print(f"HTTP错误: {err}")
    except Exception as e:
        print(f"发生错误: {e}")

def get_all_product_variant_data():
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(API_URL+"/common/all/MProduct", headers=headers)

        # 检查响应状态
        response.raise_for_status()
        print("===========all_product_data==================")
        print(response.json())
        return response.json()  # 返回 JSON 格式的响应
    except requests.exceptions.HTTPError as err:
        print(f"HTTP错误: {err}")
    except Exception as e:
        print(f"发生错误: {e}")

def insert_product_data(data):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(API_URL+"/common/create/MProduct", headers=headers, json=data)

        # 检查响应状态
        response.raise_for_status()
        return response.json()  # 返回 JSON 格式的响应
    except requests.exceptions.HTTPError as err:
        print(f"HTTP错误: {err}")
    except Exception as e:
        print(f"发生错误: {e}")

def insert_product_variant_data(data):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(API_URL+"/common/create/MProductVariant", headers=headers, json=data)

        # 检查响应状态
        response.raise_for_status()
        return response.json()  # 返回 JSON 格式的响应
    except requests.exceptions.HTTPError as err:
        print(f"HTTP错误: {err}")
    except Exception as e:
        print(f"发生错误: {e}")

def update_product_data(data):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    update_id = data['_id']
    try:
        response = requests.put(API_URL+f'/common/update/{update_id}/MProduct', headers=headers, json=data)
        response.raise_for_status()
        return response.json()  # 返回 JSON 格式的响应
    except requests.exceptions.HTTPError as err:
        print(f"HTTP错误: {err}")
    except Exception as e:
        print(f"发生错误: {e}")

def update_product_variant_data(data):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    update_id = data['_id']
    try:
        response = requests.put(API_URL+f'/common/update/{update_id}/MProductVariant', headers=headers, json=data)
        response.raise_for_status()
        return response.json()  # 返回 JSON 格式的响应
    except requests.exceptions.HTTPError as err:
        print(f"HTTP错误: {err}")
    except Exception as e:
        print(f"发生错误: {e}")

def delete_product_data(data):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    json_data = {"_ids":[data]}
    try:
        response = requests.delete(API_URL+'/common/reallyDelete/MProduct', headers=headers, json=json_data)
        response.raise_for_status()
        return response.json()  # 返回 JSON 格式的响应
    except requests.exceptions.HTTPError as err:
        print(f"HTTP错误: {err}")
    except Exception as e:
        print(f"发生错误: {e}")

def delete_product_variant_data(data):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    json_data = {"_ids":[data]}
    try:
        response = requests.delete(API_URL+'/common/reallyDelete/MProductVariant', headers=headers, json=json_data)
        response.raise_for_status()
        return response.json()  # 返回 JSON 格式的响应
    except requests.exceptions.HTTPError as err:
        print(f"HTTP错误: {err}")
    except Exception as e:
        print(f"发生错误: {e}")

def start_timer(interval):
    while True:
        fetch_data()
        time.sleep(interval)  # 设置间隔时间


if __name__ == "__main__":
    # interval = 10  # 每隔10秒获取一次数据
    # timer_thread = threading.Thread(target=start_timer, args=(interval,))
    # timer_thread.start()

    products = [
        {
            "_id": "67c6a51e7141102f1820a222",
            "title": {
                "en": "demo Productkk",
                "zh": "demo Productkk",
                "cn": "demo Productkk"
            }
        },{
            "_id": "67c6a51e7141102f1820a244",
            "title": {
                "en": "demo Productpp",
                "zh": "demo Productpp",
                "cn": "demo Productpp"
            }
        },{
            "_id": "67c6a51e7141102f1820a288",
            "title": {
                "en": "demo Productll",
                "zh": "demo Productll",
                "cn": "demo Productll"
            }
        }
    ]

    product_variants = [{
        "_id":"67c6a51e7141102f1820a233",
        "product_id": "67c6a51e7141102f1820a222",
        "title": {
            "en": "demo Product11",
            "zh": "demo Product11",
            "cn": "demo Product11"
        },
        "price":100
    },{
        "_id":"67c6a51e7141102f1820a255",
        "product_id": "67c6a51e7141102f1820a244",
        "title": {
            "en": "demo Product22",
            "zh": "demo Product22",
            "cn": "demo Product22"
        },
        "price":200
    },{
        "_id":"67c6a51e7141102f1820a277",
        "product_id": "67c6a51e7141102f1820a266",
        "title": {
            "en": "demo Product33",
            "zh": "demo Product33",
            "cn": "demo Product33"
        },
        "price":300
    }]
    

    # print(f"product_id:"+insert_product_data(product)['data']['_id'])
    # print(f"product_variant_id:"+insert_product_variant_data(product_variant)['data']['_id'])

    all_product_data = get_all_product_data()
    all_product_variant_data = get_all_product_variant_data()
    # 数据库没有数据直插入
    if(0 == len(all_product_data['data'])):
        for product in products:
            insert_product_data(product)

    elif (0 == len(all_product_variant_data['data'])):
        for product_variant in product_variants:
            insert_product_variant_data(product_variant)
    else:
        all_product_data_id = [obj['_id'] for obj in all_product_data["data"] ]
        all_product_data_variant_id = [obj['_id'] for obj in all_product_variant_data["data"] ]
        print("all product id")
        print(all_product_data_id)
        print("all product variant id")
        print(all_product_data_variant_id)
        # 检测机制
        ## product
        ### 1. 插入新的产品
        for product in products:
            if product['_id'] not in all_product_data_id:
                print(f"insert product_id:{product['_id']}")
                insert_product_data(product)  # 插入新产品
            else:
                print(f"update product_id:{product['_id']}")
                update_product_data(product)   # 更新已有产品

        ### 3. 删除不存在的产品
        for product_id in all_product_data_id:
            if not any(product['_id'] == product_id for product in products):
                print(f"delete product_id:{product_id}")
                delete_product_data(product_id)

        ## product_variant
        ### 1. 插入新的产品变体
        for product_variant in product_variants:
            if product_variant['_id'] not in all_product_data_variant_id:
                print(f"insert product_variant_id:{product_variant['_id']}")
                insert_product_variant_data(product_variant)
            else:
                print(f"update product_variant_id:{product_variant['_id']}")
                update_product_variant_data(product_variant)
            
        ### 3. 删除不存在的产品变体
        for product_variant_id in all_product_data_variant_id:
            if not any(product_variant_id == product_variant['_id'] for product_variant in product_variants):
                print(f"delete product_variant_id:{product_variant_id}")
                delete_product_variant_data(product_variant_id)

    # get_all_product_variant_data()