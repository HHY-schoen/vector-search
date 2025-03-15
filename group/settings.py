index_map = {
    "settings": {
        "index": {
            "number_of_shards": 2,
            "number_of_replicas": 1,
            "analysis": {
                "analyzer": {
                    "group_import": {
                        "type": "custom",
                        "tokenizer": "jieba_index",
                        "filter": ["lowercase", "jieba_stop"],
                    },
                    "group_search": {
                        "type": "custom",
                        "tokenizer": "whitespace",
                        "filter": ["lowercase", "jieba_stop", "jieba_synonym"],
                    },
                },
                "filter": {
                    "jieba_stop": {
                        "type": "stop",
                        "stopwords_path": "jieba/stopwords/stopwords.txt",
                    },
                    "jieba_synonym": {
                        "type": "synonym",
                        "synonyms_path": "jieba/synonyms/synonyms.txt",
                        "updateable": True,
                    },
                },
                "normalizer": {
                    "lowercase": {"type": "custom", "filter": ["lowercase"]}
                },
            },
        }
    },
    "mappings": {
        "properties": {
            # 產品編號
            "PROD_NO": {"type": "keyword", "normalizer": "lowercase"},
            # 產品名稱
            "PROD_NAME": {
                "type": "text",
                "analyzer": "group_import",
                "search_analyzer": "group_search",
                "fields": {"keyword": {"type": "keyword", "normalizer": "lowercase"}},
            },
            # 產品名稱
            "PROD_NAME_1": {"type": "text"},
            # 商品類別
            "PROD_TYPEM": {"type": "text"},
            # 商品子類別
            "PROD_SUBTYPE": {"type": "keyword"},
            # 主題
            "PROD_SUBJECT": {"type": "keyword", "normalizer": "lowercase"},
            # 國家
            "PROD_COUNTRY": {"type": "keyword", "normalizer": "lowercase"},
            # 城市
            "PROD_CITY": {"type": "keyword", "normalizer": "lowercase"},
            # 經緯度
            "PROD_GEO_COORD": {"type": "geo_point"},
            # 圖片網址
            "IMAGEURL": {"type": "text"},
            # 商品說明
            "PROD_DESC": {
                "type": "text",
                "analyzer": "group_import",
                "search_analyzer": "group_search",
            },
            # 價格
            "PROD_AMT_D": {"type": "float"},
            # 產品網址
            "WEB": {"type": "text"},
            # 圖片代碼
            "PIC_NO": {"type": "keyword"},
            # BU T 圖片網址
            "T_IMAGE_URL": {"type": "text"},
            # BU P 圖片網址
            "P_IMAGE_URL": {"type": "text"},
            # BU N 圖片網址
            "N_IMAGE_URL": {"type": "text"},
            # 出團雄獅國家
            "GO_COUNTRY": {"type": "keyword", "normalizer": "lowercase"},
            # 線別ID
            "PROD_LINE_ID": {"type": "keyword", "normalizer": "lowercase"},
            # 線別中文名
            "PROD_LINE_NAME": {"type": "keyword", "normalizer": "lowercase"},
            # 副線別ID
            "PROD_LINED_ID": {"type": "keyword", "normalizer": "lowercase"},
            # 副線別中文名
            "PROD_LINED_NAME": {"type": "keyword", "normalizer": "lowercase"},
            # 地區ID
            "AREA_ID": {"type": "keyword", "normalizer": "lowercase"},
            # 地區中文名
            "AREA_NAME": {"type": "keyword", "normalizer": "lowercase"},
            # 細地區ID
            "AREAD_ID": {"type": "keyword", "normalizer": "lowercase"},
            # 細地區中文名
            "AREAD_NAME": {"type": "keyword", "normalizer": "lowercase"},
            # 目的地ID
            "WEB_AREA_ID": {"type": "keyword", "normalizer": "lowercase"},
            # 目的地
            "PROD_DESTN": {"type": "keyword", "normalizer": "lowercase"},
            # 目的地資料
            "DESTINATION_LIST": {
                "type": "nested",
                "properties": {
                    # CMS國家ID
                    "COUNTRY_ID": {
                        "type": "keyword",
                        "normalizer": "lowercase",
                        "eager_global_ordinals": True,
                    },
                    # CMS國家名稱
                    "COUNTRY_NAME": {"type": "keyword", "normalizer": "lowercase"},
                    # CMS國家簡稱
                    "COUNTRY_ABBR": {"type": "keyword", "normalizer": "lowercase"},
                    # CMS城市ID
                    "CITY_ID": {
                        "type": "keyword",
                        "normalizer": "lowercase",
                        "eager_global_ordinals": True,
                    },
                    # CMS城市名稱
                    "CITY_NAME": {"type": "keyword", "normalizer": "lowercase"},
                    # CMS城市簡稱
                    "CITY_ABBR": {"type": "keyword", "normalizer": "lowercase"},
                    # CTO國家ID
                    "CTO_COUNTRY_ID": {"type": "keyword", "normalizer": "lowercase"},
                    # CTO國家名稱
                    "CTO_COUNTRY_NAME": {"type": "keyword", "normalizer": "lowercase"},
                    # CTO城市ID
                    "CTO_CITY_ID": {"type": "keyword", "normalizer": "lowercase"},
                    # CTO城市名稱
                    "CTO_CITY_NAME": {"type": "keyword", "normalizer": "lowercase"},
                },
            },
            # 地區同義詞列表
            "AREA_SYNONYM_LIST": {"type": "keyword", "normalizer": "lowercase"},
            # 短產品名稱
            "SHORTEN_TOUR_NAME": {
                "type": "text",
                "analyzer": "group_import",
                "search_analyzer": "group_search",
            },
            # 短產品名稱
            "SHORTEN_TOUR_NAME_1": {"type": "text"},
            # 內部顯示名稱
            "TOUR_INSIDE_NAME": {
                "type": "text",
                "analyzer": "group_import",
                "search_analyzer": "group_search",
            },
            # 內部顯示名稱
            "TOUR_INSIDE_NAME_1": {"type": "text"},
            # 標準團名ID
            "TBM0_CODE": {"type": "keyword", "normalizer": "lowercase"},
            # 標準團名
            "PROD_ONM": {
                "type": "text",
                "analyzer": "group_import",
                "search_analyzer": "group_search",
            },
            # 標準團名
            "PROD_ONM_1": {"type": "text"},
            # 標準團名等級
            "PROD_ONM_LEVEL": {
                "properties": {
                    "LEVEL_ID": {"type": "keyword"},
                    "LEVEL_NAME": {"type": "text"},
                }
            },
            # B2C 最低售價
            "B2C_LOW_PRICE": {"type": "float"},
            # B2B 最低售價
            "B2B_LOW_PRICE": {"type": "float"},
            # 城市動線
            "CITY_FLOW": {
                "type": "text",
                "analyzer": "group_import",
                "search_analyzer": "group_search",
            },
            # POI列表
            "POI_INFO": {
                "type": "nested",
                "properties": {
                    # POI編號
                    "POINO": {"type": "keyword", "normalizer": "lowercase"},
                    # POI名稱
                    "POINAME": {"type": "keyword", "normalizer": "lowercase"},
                    # 緯度
                    "LAT": {"type": "float"},
                    # 經度
                    "LON": {"type": "float"},
                },
            },
            # 行程天數
            "PROD_DAYS": {"type": "integer"},
            # 出發地
            "PROD_SFCITY": {"type": "keyword", "normalizer": "lowercase"},
            # 出發地資料
            "DEPARTURE_LIST": {
                "type": "nested",
                "properties": {
                    # 城市代碼
                    "CITY_CODE": {"type": "keyword", "normalizer": "lowercase"},
                    # 城市名稱
                    "CITY_NAME": {"type": "keyword", "normalizer": "lowercase"},
                },
            },
            # 建檔單位
            "PROD_PROF": {"type": "keyword", "normalizer": "lowercase"},
            # 日行程說明
            "ITINERARY_DESC": {
                "type": "text",
                "analyzer": "group_import",
                "search_analyzer": "group_search",
            },
            # 每日行程說明
            "DAILY_DESC": {
                "type": "nested",
                "properties": {
                    # 天數(第幾天)
                    "DAY": {"type": "integer"},
                    # 描述
                    "TRAVEL_POINT": {"type": "text"},
                    # 特點
                    "SPECIAL_NOTE": {"type": "text"},
                    # 內容
                    "SUMMARY": {"type": "text"},
                },
            },
            # 每日景點
            "ITINERARY_ATTRACTION": {
                "type": "nested",
                "properties": {
                    # 天數(第幾天)
                    "DAY": {"type": "integer"},
                    "ATTRACTION_LIST": {
                        "type": "nested",
                        "properties": {
                            # 景點編號
                            "ATTRACTION_ID": {
                                "type": "keyword",
                                "normalizer": "lowercase",
                            },
                            # 景點名稱
                            "ATTRACTION_NAME": {
                                "type": "keyword",
                                "normalizer": "lowercase",
                            },
                            #
                            "FIT_INTERVAL": {"type": "integer"},
                            # 到達時間
                            "ARRIVAL_TIME": {"format": "HH:mm", "type": "date"},
                            # 停留時間
                            "RESIDENCE_TIME": {"format": "HH:mm", "type": "date"},
                            # 訪問方式
                            "VISIT_WAY": {"type": "integer"},
                            # 介紹
                            "INTRODUCTION": {"type": "text"},
                            # POI列表
                            "POI_LIST": {"type": "keyword", "normalizer": "lowercase"},
                        },
                    },
                },
            },
            # 每日餐食
            "ITINERARY_MEAL": {
                "type": "nested",
                "properties": {
                    # 天數(第幾天)
                    "DAY": {"type": "integer"},
                    # 早餐
                    "BREAKFAST": {"type": "text"},
                    # 早午餐
                    "BRUNCH": {"type": "text"},
                    # 午餐
                    "LUNCH": {"type": "text"},
                    # 午晚餐
                    "LINNER": {"type": "text"},
                    # 晚餐
                    "DINNER": {"type": "text"},
                    # 宵夜
                    "SUPPER": {"type": "text"},
                },
            },
            # 每日住宿
            "ITINERARY_HOTEL": {
                "type": "nested",
                "properties": {
                    # 天數(第幾天)
                    "DAY": {"type": "integer"},
                    # 住宿
                    "HOTEL": {"type": "text"},
                },
            },
            # 關鍵字字串
            "KEYWORDS": {"type": "text"},
            # 關鍵字列表
            "KEYWORD_LIST": {"type": "keyword", "normalizer": "lowercase"},
            # 旅遊型態列表
            "TRIP_TYPE_LIST": {
                "type": "nested",
                "properties": {
                    # 來源
                    "NAME": {"type": "text"},
                    # 特色代碼
                    "CODE": {"type": "keyword"},
                    # 關聯主題代碼
                    "RELATED_THEME_ID": {"type": "keyword"},
                },
            },
            # 旅遊館群組列表
            "TRAVEL_GROUP_LIST": {
                "type": "nested",
                "properties": {
                    # 旅遊館代碼
                    "ROOM_ID": {"type": "keyword", "normalizer": "lowercase"},
                    # 旅遊館名稱
                    "ROOM_NAME": {"type": "text"},
                    # 旅遊館群組名稱
                    "GROUP_NAME": {"type": "text"},
                    # 負責單位
                    "PROF": {"type": "keyword", "normalizer": "lowercase"},
                    # 負責單位名稱
                    "PROF_NAME": {"type": "text"},
                },
            },
            # 標籤列表
            "TAG_LIST": {
                "type": "nested",
                "properties": {
                    # 標籤名稱
                    "TAG_NAME": {
                        "type": "text",
                        "fields": {
                            "keyword": {"type": "keyword", "normalizer": "lowercase"}
                        },
                    },
                    # 標籤編號
                    "TAG_NO": {"type": "integer"},
                    # 標籤排序
                    "TAG_SORT": {"type": "integer"},
                },
            },
            # 組合標籤列表
            "COMBINE_TAG_LIST": {"type": "keyword"},
            # 節令
            "FESTIVAL": {"type": "keyword", "normalizer": "lowercase"},
            # 特色溫泉
            "SPECIAL_SPA": {"type": "keyword", "normalizer": "lowercase"},
            # 特色餐食
            "SPECIAL_MEAL": {"type": "keyword", "normalizer": "lowercase"},
            # 目標客群
            "TARGET_CUST": {"type": "keyword", "normalizer": "lowercase"},
            # 團資料
            "GROUP_INFO": {
                "type": "nested",
                "properties": {
                    # 團號
                    "PROD_NO": {"type": "keyword", "normalizer": "lowercase"},
                    # 產品號
                    "PROD_PROD": {"type": "keyword", "normalizer": "lowercase"},
                    # 開團公司
                    "PROD_PRODCOMP": {"type": "keyword", "normalizer": "lowercase"},
                    # 團號 match pattern
                    "PROD_NO_MATCH_PATTERN": {
                        "type": "keyword",
                        "normalizer": "lowercase",
                    },
                    # 出團雄獅國家
                    "GO_COUNTRY": {"type": "keyword", "normalizer": "lowercase"},
                    # 銷售幣別
                    "SALE_CURR": {"type": "text"},
                    # 銷售幣別ISO
                    "SALE_CURR_ISO": {"type": "text"},
                    # B2C 最低售價
                    "B2C_LOW_PRICE": {"type": "float"},
                    # B2B 最低售價
                    "B2B_LOW_PRICE": {"type": "float"},
                    # 出發日
                    "PROD_DATE_BEGIN": {"type": "date"},
                    # 工作日
                    "DATE_BEGIN_WEEKDAY": {"type": "integer"},
                    # 站台Bu
                    "TOUR_BU": {"type": "keyword"},
                    # 是否有會員限購價
                    "IS_VIP": {"type": "integer"},
                    # 會員限購價最低價
                    "VIP_ORIG_PRICE": {"type": "float"},
                    # 總團位數
                    "TOTAL_SEATS": {"type": "integer"},
                    # 可賣位數
                    "QUOTA_SEATS": {"type": "integer"},
                    # 有位沒繳訂金
                    "HK_SEATS": {"type": "integer"},
                    # 有位有繳訂金
                    "KK_SEATS": {"type": "integer"},
                    # 候補數量
                    "HL_SEATS": {"type": "integer"},
                    # 保留位數
                    "KEEP_SEATS": {"type": "integer"},
                    # PAK團位數
                    "PAK_SEATS": {"type": "integer"},
                    # 候補有繳訂金位數
                    "OB_SEATS": {"type": "integer"},
                    # SERP上可賣位數
                    "QUOTA_SEATS_SERP": {"type": "integer"},
                    # 團控狀態
                    "PROD_FULL": {"type": "keyword", "normalizer": "lowercase"},
                    # 保證出團
                    "PROD_GO": {"type": "integer"},
                    # 主題旅遊代碼
                    "THEME_ID": {"type": "keyword"},
                    # 行程目的地代碼
                    "ARRIVE_ID": {"type": "keyword"},
                    # 行程目的地線別代碼
                    "ARRIVE_LINE_ID": {"type": "keyword"},
                    # 行程目的地副線別代碼
                    "ARRIVE_LINED_ID": {"type": "keyword"},
                    # 行程目的地旅遊地區代碼
                    "ARRIVE_WEB_AREA_ID": {"type": "keyword"},
                    # 產品BU
                    "PROD_BU": {"type": "keyword", "normalizer": "lowercase"},
                    # 產品BU名稱
                    "PROD_BU_NAME": {"type": "text"},
                    # 銷售對象
                    "PROD_SALE": {"type": "keyword", "normalizer": "lowercase"},
                    # 上下車資料
                    "STATION_INFO": {
                        "type": "nested",
                        "properties": {
                            # 集合地點
                            "PLACE": {"type": "text"},
                            # 集合地點代碼
                            "PLACE_ID": {"type": "keyword", "normalizer": "lowercase"},
                            # 集合時間
                            "MUSTER_TIME": {"format": "HH:mm", "type": "date"},
                            # 地址
                            "ADDRESS": {"type": "text"},
                            # 集合城市代碼
                            "CITY_CODE": {"type": "keyword", "normalizer": "lowercase"},
                            # 集合城市中文名
                            "CITY_CNAME": {"type": "text"},
                        },
                    },
                    # 航班資料
                    "FLIGHT_INFO": {
                        "type": "nested",
                        "properties": {
                            # 航空公司代碼
                            "FLIGHT_CARR_ID": {
                                "type": "keyword",
                                "normalizer": "lowercase",
                            },
                            # 航空公司
                            "FLIGHT_CARR": {"type": "text"},
                            # 航班編號
                            "FLIGHT_NO": {"type": "keyword", "normalizer": "lowercase"},
                            # 起飛機場
                            "FLIGHT_DEPARTURE_AIRPORT": {"type": "text"},
                            # 起飛機場國家代碼
                            "FLIGHT_DEPARTURE_COUNTRY_CODE": {
                                "type": "keyword",
                                "normalizer": "lowercase",
                            },
                            # 起飛機場城市代碼
                            "FLIGHT_DEPARTURE_CITY_CODE": {
                                "type": "keyword",
                                "normalizer": "lowercase",
                            },
                            # 起飛機場城市名稱
                            "FLIGHT_DEPARTURE_CITY_NAME": {"type": "text"},
                            # 起飛日期
                            "FLIGHT_DEPARTURE_DATE": {"type": "date"},
                            # 起飛時間
                            "FLIGHT_DEPARTURE_TIME": {"type": "text"},
                            # 抵達機場
                            "FLIGHT_ARRIVE_AIRPORT": {"type": "text"},
                            # 抵達機場國家代碼
                            "FLIGHT_ARRIVE_COUNTRY_CODE": {
                                "type": "keyword",
                                "normalizer": "lowercase",
                            },
                            # 抵達機場城市代碼
                            "FLIGHT_ARRIVE_CITY_CODE": {
                                "type": "keyword",
                                "normalizer": "lowercase",
                            },
                            # 抵達機場城市名稱
                            "FLIGHT_ARRIVE_CITY_NAME": {"type": "text"},
                            # 抵達日期
                            "FLIGHT_ARRIVE_DATE": {"type": "date"},
                            # 抵達時間
                            "FLIGHT_ARRIVE_TIME": {"type": "text"},
                            # 航班方向 (1：去程、9：回程、O：中段、X：湊票不含此段)
                            "DIRECTION": {
                                "properties": {
                                    "ID": {
                                        "type": "keyword",
                                        "normalizer": "lowercase",
                                    },
                                    "NAME": {"type": "text"},
                                }
                            },
                            # 是否為中段航班
                            "IS_MIDDLE": {"type": "boolean"},
                            # 飛行時間
                            "FLIGHT_TIME": {"type": "text"},
                        },
                    },
                    # 去程航班起飛時間
                    "FLIGHT_DEPARTURE_TIME_OUTBOUND": {
                        "format": "HH:mm",
                        "type": "date",
                    },
                    # 回程航班起飛時間
                    "FLIGHT_DEPARTURE_TIME_INBOUND": {
                        "format": "HH:mm",
                        "type": "date",
                    },
                    # 產品開團狀態
                    "STATUS": {"type": "integer"},
                    # T-B2C 產品網址
                    "T_B2C_URL": {"type": "text"},
                    # T-B2B 產品網址
                    "T_B2B_URL": {"type": "text"},
                    # T-B2E 產品網址
                    "T_B2E_URL": {"type": "text"},
                    # T-BBC 產品網址
                    "T_BBC_URL": {"type": "text"},
                    # P-B2C 產品網址
                    "P_B2C_URL": {"type": "text"},
                    # P-B2B 產品網址
                    "P_B2B_URL": {"type": "text"},
                    # N-B2C 產品網址
                    "N_B2C_URL": {"type": "text"},
                    # Agent Code
                    "AGENT_CODE": {"type": "keyword", "normalizer": "lowercase"},
                    # 轉需求單網址
                    "TARGET_URL": {"type": "text"},
                    # 點擊次數
                    "CLICK_COUNT": {"type": "integer"},
                    # 更新時間
                    "UPDATE_TIME": {"type": "integer"},
                },
            },
            # 是否國外
            "IS_FOREIGN": {"type": "boolean"},
            # 點擊次數
            "CLICK_COUNT": {"type": "integer"},
            # 摺疊用編號
            "COLLAPSE_ID": {"type": "keyword", "normalizer": "lowercase"},
            # 摺疊用編號
            "COLLAPSE_ID_1": {"type": "keyword", "normalizer": "lowercase"},
            # 是否主打
            "IS_TOP": {"type": "boolean"},
            # 是否主打順序
            "IS_TOP_SORT": {"type": "integer"},
            # 更新時間
            "UPDATE_TIME": {"type": "integer"},
            # 向量欄位
            "VectorB2CProdName": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorDailyDescription": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorDescription": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorTagName": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorTbm0Name": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorTourInsideName": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorTripTypeName": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            # 1125 add
            "VectorProdLineName": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorProdCountry": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorProdCityy": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorDepartureCity": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
            "VectorDestinationCity": {
                "type": "dense_vector",
                "dims": 1792,
                "index": True,
                "similarity": "cosine",
            },
        }
    },
}


vector_fields_map = [
    ("PROD_NAME", "VectorB2CProdName", None),
    ("PROD_ONM", "VectorTbm0Name", None),
    ("ITINERARY_DESC", "VectorDailyDescription", None),
    ("TOUR_INSIDE_NAME", "VectorTourInsideName", None),
    ("PROD_DESC", "VectorDescription", None),
    ("PROD_LINE_NAME", "VectorProdLineName", None),
    ("PROD_COUNTRY", "VectorProdCountry", None),
    ("PROD_CITY", "VectorProdCityy", None),
    ("TAG_LIST", "VectorTagName", "TAG_NAME"),
    ("TRIP_TYPE_LIST", "VectorTripTypeName", "NAME"),
    ("DEPARTURE_LIST", "VectorDepartureCity", "CITY_NAME"),
    ("DESTINATION_LIST", "VectorDestinationCity", "CITY_NAME"),
]
