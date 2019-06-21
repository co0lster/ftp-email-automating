import requests
import textwrap

def login(username, password, phpsessid):
    url = "https://www.zak.lodz.pl/forum/people.php"
    payload = "ReturnUrl=https%3A%2F%2Fwww.zak.lodz.pl%2Fforum%2F&PostBackAction=SignIn&Username=" + username + "&Password=" + password + "&btnSignIn=Kontynuuj"
    headers = {
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'Origin': "https://www.zak.lodz.pl",
        'Upgrade-Insecure-Requests': "1",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'Referer': "https://www.zak.lodz.pl/forum/people.php?ReturnUrl=https%3A%2F%2Fwww.zak.lodz.pl%2Fforum%2F,https://www.zak.lodz.pl/forum/people.php",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Cookie': "PHPSESSID=" + phpsessid,
        'Postman-Token': "faf22e72-9f88-49d7-96ff-e99cb78cb77b,9a50e78e-7758-47d6-9ebc-95e23665ca02",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.status_code)


def getKey(phpsessid):
    headers = {
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'Origin': "https://www.zak.lodz.pl",
        'Upgrade-Insecure-Requests': "1",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'Referer': "https://www.zak.lodz.pl/forum/people.php?ReturnUrl=https%3A%2F%2Fwww.zak.lodz.pl%2Fforum%2F,https://www.zak.lodz.pl/forum/people.php",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Cookie': "PHPSESSID=" + phpsessid,
        'Postman-Token': "faf22e72-9f88-49d7-96ff-e99cb78cb77b,9a50e78e-7758-47d6-9ebc-95e23665ca02",
        'cache-control': "no-cache"
    }
    resp = requests.request("GET", "https://www.zak.lodz.pl/forum/categories.php", headers=headers)
    if resp.text.__contains__("Niezalogowany"):
        print('NOT LOGGED IN')
    else:
        return resp.text[1006:1038]


def logout(formPostBackKey, phpsessid):
    url = "https://www.zak.lodz.pl/forum/people.php"

    querystring = {"PostBackAction": "SignOutNow", "FormPostBackKey": formPostBackKey}

    headers = {
        'Connection': "keep-alive",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'Referer': "https://www.zak.lodz.pl/forum/",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Cookie': "PHPSESSID=" + phpsessid,
        'Cache-Control': "no-cache",
        'Postman-Token': "e238e821-5882-492d-a1a3-41a9c2f5824d,fed3b4a8-9e44-4b89-ade7-ba17f3fad5b9",
        'Host': "www.zak.lodz.pl",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.status_code)


def post(key, name, body, phpsessid):
    import requests

    url = "https://www.zak.lodz.pl/forum/post.php"

    payload = "FormPostBackKey=" + key + "&DiscussionID=&CommentID=&AuthUserID=&UserDiscussionCount=&PostBackAction=SaveDiscussion&CategoryID=5&Name=" + name + "&WhisperUsername=&Body=" + body + "&FormatType=text"
    headers = {
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'Origin': "https://www.zak.lodz.pl",
        'Upgrade-Insecure-Requests': "1",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'Referer': "https://www.zak.lodz.pl/forum/post.php?CategoryID=5",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Cookie': "PHPSESSID=" + phpsessid,
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)



def comment(key, discussion_id, body, phpsessid):
    import requests

    url = "https://www.zak.lodz.pl/forum/post.php"

    payload = "FormPostBackKey=" + key + "&CommentID=0&DiscussionID=" + discussion_id + "&PostBackAction=SaveComment&UserCommentCount=0&AuthUserID=0&WhisperUsername=&Body=" + body + "&FormatType=Text"
    headers = {
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'Origin': "https://www.zak.lodz.pl",
        'Upgrade-Insecure-Requests': "1",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Cookie': "PHPSESSID=" + phpsessid,
        'cache-control': "no-cache",
        'Postman-Token': "712d7fef-5111-471d-bd19-93a116cf139c"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


def phpsessid():
    import requests

    url = "https://www.zak.lodz.pl/forum/"

    headers = {
        'Connection': "keep-alive",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Cache-Control': "no-cache",
        'Postman-Token': "47edfeb1-baa6-4476-acbe-68e3b0dd2f05,a21a6b56-01c3-4d05-93d6-17f4adf916c1",
        'Host': "www.zak.lodz.pl",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)

    x = response.headers.get('Set-Cookie')
    return x.split(';')[0][10:]


def send_to_forum(nick, password, postanowienia):
    body = postanowienia[1:]
    sessid = phpsessid()
    login(nick, password, sessid)
    le = len(body)
    print(le)
    if le < 9972:
        post(getKey(sessid), postanowienia.split('\n', 2)[1], body, sessid)
    else:
        print("Split this file into chunks!")
        # lines = textwrap.wrap(body, 9972)
        # id = post(getKey(sessid), postanowienia.split('\n', 2)[1], body,sessid)
        # for posts in lines[1:]:
        #     comment(getKey(sessid), id, posts)
    logout(getKey(sessid), sessid)