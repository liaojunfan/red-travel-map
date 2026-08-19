from flask import Flask, request, jsonify, send_file
import math
from itertools import permutations

app = Flask(__name__)

red_sites = [
    {
        "name": "瓮安猴场会议会址",
        "lng": 107.4722,
        "lat": 27.0711,
        "intro": "猴场会议是红军长征途中一次重要的政治局会议，为遵义会议的召开奠定了基础。"
    },
    {
        "name": "瓮安红军渡江遗址",
        "lng": 107.4761,
        "lat": 27.0468,
        "intro": "红军强渡乌江遗址，见证红军长征渡江战斗的伟大历程。"
    },
    {
        "name": "荔波邓恩铭故居",
        "lng": 107.8803,
        "lat": 25.4272,
        "intro": "中共一大代表邓恩铭的故居，贵州红色革命发源地之一。"
    },
    {
        "name": "独山深河桥抗战遗址",
        "lng": 107.5321,
        "lat": 25.8110,
        "intro": "抗日战争黔南事变重要遗址。"
    },
    {
        "name": "都匀西山红军烈士纪念碑",
        "lng": 107.5144,
        "lat": 26.2682,
        "intro": "纪念在都匀地区牺牲的红军革命烈士。"
    }
]

def haversine(p1, p2):
    lon1, lat1 = p1
    lon2, lat2 = p2
    R = 6371
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dLon/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R*c

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Allow-Headers'] = '*'
    return response

#新增首页路由，访问根路径直接打开网页
@app.route("/")
def index():
    return send_file("map.html")

@app.route("/getRedSites",methods=["GET"])
def get_sites():
    return jsonify(red_sites)

@app.route("/calcSmartRoute",methods=["POST"])
def calc_route():
    data = request.get_json()
    selected_index = data.get("selected",[])
    if len(selected_index)<2:
        return jsonify({"code":-1,"msg":"至少选择2个景点！"})
    points = []
    for idx in selected_index:
        s = red_sites[idx]
        points.append([s["lng"],s["lat"]])
    n = len(points)
    min_dist = float("inf")
    best_perm = None
    start = 0
    others = list(range(1,n))
    for perm in permutations(others):
        path = [start] + list(perm)
        dist = 0
        for i in range(len(path)-1):
            dist += haversine(points[path[i]],points[path[i+1]])
        if dist<min_dist:
            min_dist = dist
            best_perm = path
    best_index_list = [selected_index[i] for i in best_perm]
    best_route = [red_sites[i] for i in best_index_list]
    return jsonify({
        "code":0,
        "total_km":round(min_dist,2),
        "route":best_route
    })

if __name__=="__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)