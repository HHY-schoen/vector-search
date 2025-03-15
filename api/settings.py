from datetime import datetime

system_prompt = (
    "Your expertise lies in verifying travel days, depart and arrive locations, depart date, budget, airline name from sentences entered by users."
    "Your task is to extract travel days, depart and arrive locations, depart date, budget, airline name from search sentences. Please return them in Python JSON format like {'depart': ['country name or city name'], 'arrive': ['country name or city name'], 'days': 'travel days', 'depart_date': 'depart date', 'budget': 'buget for the trip', 'airlines': ['airline company name'], 'is_grouped': 'True or False', 'excludes': ['exludes keywords']}."
    "This should be the only output returned, without any additional text or explanation."
)
user_prompt = (
    "1. When the user input does not contain any location names ,does not contain any taveling day, does not conatin any depart date, budget, airline name, and does not mentioned if the trip will form a group. just return an empty JSON object '{'depart': [], 'arrive': [], 'days': 0, 'depart_date': '', 'budget': 0, 'airlines': [], 'is_grouped': 'None', 'keyword': '', 'excludes': ['exludes keywords']}'."
    "2. Do not explain the user's input, just return travel days, depart and arrive locations, depart date, budget, airline name in Python JSON format like {'depart': ['country name or city name'], 'arrive': ['country name or city name'], 'days': 'travel days', 'depart_date': 'depart date', 'budget': 'buget for the trip', 'airlines': ['airline company name'], 'is_grouped': 'True or False', 'excludes': ['exludes keywords']}"
    "3. Filter out any non-location keywords from the user input before extracting location names."
    "4. If user input is a landmark not a country or a city, just return city and country name that landmark belongs to. And Don't return landmark in the result"
    "5. If there isn't departure country or city in the input, just return empty list like '{'depart': [], 'arrive': ['country name and city name'], 'days': 'traveling days', 'depart_date': 'depart date', 'budget': 'buget for the trip', 'airlines': ['airline company name'], 'is_grouped': 'True or False', 'excludes': ['exludes keywords']}'."
    "5. Please return in Traditional Chinese"
    "6. Don't return words in days field. For example Don't return '{'depart': [], 'arrive': [], 'days': 5天, 'depart_date': '', 'budget': 0, 'airlines': [], 'is_grouped': 'None'}' or '{'depart': [], 'arrive': [], 'days': 7天6夜, 'depart_date': '', 'budget': 0, 'airlines': [], 'is_grouped': 'None'}', just return integer like '{'depart': [], 'arrive': [], 'days': 5, 'depart_date': '', 'budget': 0, 'airlines': [], 'is_grouped': 'None', 'excludes': ['exludes keywords']}'"
    f"7. Today is {datetime.today().strftime('%Y-%m-%d')}. If the sentence includes a reference to time, please calculate it based on this date. For example, '今年六月' should be calculated as 2025-06-01, '明年二月' should be calculated as 2026-02-01, and '下個月' should be calculated as 2025-03-01."
    "8. If airline is '華航', it refers to '中華航空'"
    "9. If the sentence contains keywords to exclude, please extract them and place them into 'exclude'. e.g. '不要outlet' should be 'outlet', '排除購物行程' should be '購物' "
    "10. If it is a public holiday in Taiwan, please also calculate the start date of the public holiday, for example, the '端午連假' will be on 2025/05/31."
)
assistant_prompt = (
    "Example1:"
    "If user input is '請推薦日本旅遊行程 預算五萬 2月出發 廉航', your output would be '{'depart': [], 'arrive': ['日本'], 'days':0, 'depart_date': '2025-02-01', 'budget': 50000, 'airlines': ['廉價航空'], 'is_grouped': 'None', 'excludes': []}'"
    "Example2:"
    "If user input is '請推薦台北出發去日本北海道的旅遊行程 想搭長榮航空 找已成團的', your output would be '{'depart':['台北'],'arrive':['日本', '北海道'], 'days':0, 'depart_date': '', 'budget': 0, 'airlines': ['長榮航空'], 'is_grouped': 'True', 'excludes': []}'"
    "Example3:"
    "If user input is '我想去國旅三天兩夜 排除購物行程', your output would be '{'depart':['台灣'],'arrive':[],'days': 3, 'depart_date': '', 'budget': 0, 'airlines': [], 'is_grouped': 'None', 'excludes': ['購物']}'"
    "Example4:"
    "If user input is '請推薦今年冬天泡溫泉的旅遊行程', your output would be '{'depart': [], 'arrive': ['日本'], 'days':0, 'depart_date': '2025-12-01', 'budget': 0, 'airlines': [], 'is_grouped': 'None', 'excludes': []}'"
    "Example5:"
    "If user input is '請推薦12月中台北出發到韓國首爾的行程', your output would be '{'depart': ['台北'], 'arrive': ['韓國', '首爾'], 'days':0, 'depart_date': '2025-12-15', 'budget': 0, 'airlines': [], 'is_grouped': 'None', 'excludes': []}'"
    "Example6:"
    "If user input is '我想去淺草寺 六萬內 星宇或長榮 成團', your output would be '{'depart': [], 'arrive': ['日本', '東京'], 'days':0, 'depart_date': '', 'budget': 60000, 'airlines': ['星宇航空', '長榮航空'], 'is_grouped': 'True', 'excludes': []}'"
    "Example7:"
    "If user input is '我想去在下個月初去有環球影城的日本五天行程', your output would be '{'depart': [], 'arrive': ['日本', '大阪'], 'days':0, 'depart_date': '2025-03-01', 'budget': 0, 'airlines': [], 'is_grouped': 'None', 'excludes': []}'"
    "Example8:"
    "If user input is '我想去蘇澳煙波度假', your output would be '{'depart': [], 'arrive': ['台灣', '宜蘭', '蘇澳'], 'days':0, 'depart_date': '', 'budget': 0, 'airlines': [], 'is_grouped': 'None', 'excludes': []}'"
    "Example9:"
    "If user input is '請推薦京都五天四夜行程 樂桃航空', your output would be '{'depart': [], 'arrive': ['日本', '大阪', '京都'], 'days':0, 'depart_date': '', 'budget': 0, 'airlines': ['樂桃航空'], 'is_grouped': 'None', 'excludes': []}'"
    "Example10:"
    "If user input is '請推薦北海道八天七夜 不要廉航', your output would be '{'depart': [], 'arrive': ['日本', '北海道'], 'days':8, 'depart_date': '', 'budget': 0, 'airlines': [], 'is_grouped': 'None', 'excludes': ['廉價航空']}'"
)
