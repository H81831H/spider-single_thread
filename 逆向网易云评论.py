import requests, json, re, time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Referer": "https://music.163.com/",
}

i = "YkkGqOhs3e0AKgXO"
g = '0CoJUm6Qyw8W8jud'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
e = '010001'

# encSecKey（写死的）
def get_encSeckey():
    return "b684a2bae5d847f7af65ce192d104b5740dc24c14f1f64a38d84f504a5e8fe38ce1e101f7d8e554aec4b185821d7dc7c732138f1c6319418051a80658323bd497dcd805549381201d96d6d7fe3311bef9339b4683e36729188a9f095cad533498131e6ed824b3fa66edab19f0e41eb56fb7dba83778dd98e6ec8c41c9e96f6d9"

# AES加密params
def enc_params_b(a, b):
    key = b.encode("utf-8")
    iv = "0102030405060708".encode("utf-8")
    plaintext = a.encode("utf-8")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return b64encode(ciphertext).decode("utf-8")

def get_params(data):
    h = enc_params_b(data, g)
    h = enc_params_b(h, i)
    return h


if __name__ == "__main__":
    all_comments = []

    cursor = "-1"
    pageNo = 1
    csrf_token = ""

    while True:
        print(f"正在爬取第 {pageNo} 页...")

        data = {
            "csrf_token": csrf_token,
            "cursor": cursor,
            "offset": "0",
            "orderType": "1",
            "pageNo": str(pageNo),
            "pageSize": "20",
            "rid": "R_SO_4_3320292186",
            "threadId": "R_SO_4_3320292186"
        }

        res = requests.post(url, data={"params": get_params(json.dumps(data)), "encSecKey": get_encSeckey()}, headers=headers).json()

        # 评论内容
        comments = res["data"]["comments"]

        if not comments:
            print("无更多评论，爬取结束！")
            break

        # 保存内容
        for c in comments:
            content = c["content"]
            all_comments.append(content)
            print(content)

        # 下一页 cursor = 当前页最后一条评论的 time
        cursor = comments[-1]["time"]

        pageNo += 1
        time.sleep(1)    # 防止反爬

    # 输出结果
    print(f"共爬取 {len(all_comments)} 条评论")
    for c in all_comments[:50]:
        print("示例评论：", c)
