import argparse

import pendulum
import requests
from github import Github

GET_UP_ISSUE_NUMBER = 1

SHANBAY_API = "https://apiv3.shanbay.com/uc/checkin/logs?user_id={shanbay_username}&ipp=10&page=1"
SHANBAY_RECORD_MESSAGE = "打卡日期 {learn_date}\r\n学习 {used_minutes} 分钟 {used_seconds} 秒，背单词 {num} 个"
DEFAULT_RECORD = "获取扇贝记录出错啦，检查检查代码吧"

TIMEZONE = "Asia/Shanghai"

def log(token):
    return Github(token)


def get_today_shanbay_status(issue):
    comments = list(issue.get_comments())
    if not comments:
        return False
    latest_comment = comments[-1]
    now = pendulum.now(TIMEZONE)
    latest_day = pendulum.instance(latest_comment.created_at).in_timezone(
        "Asia/Shanghai"
    )
    is_today = (latest_day.day == now.day) and (latest_day.month == now.month)
    return is_today


def get_latest_record(shanbay_username):
    try:
        r = requests.get(SHANBAY_API.format(shanbay_username=shanbay_username))
        if r.ok:
            record_list = r.json().get("objects")
            if len(record_list) > 0:
                # get the latest one
                latest_record = record_list[0]
                learn_date = latest_record.get("date")
                task = latest_record.get("tasks")[0]
                # get reciting words number
                num = task.get("num")
                used_time = task.get("used_time")
                used_minutes = divmod(used_time, 60)[0]
                used_seconds = divmod(used_minutes, 60)[1]

                return SHANBAY_RECORD_MESSAGE.format(
                    learn_date=learn_date, num=num, used_minutes=used_minutes, used_seconds=used_seconds
                )
    except:
        print("get SHANBAY_API wrong")
        return DEFAULT_RECORD
    

def main(github_token, repo_name, shanbay_username, tele_token, tele_chat_id):
    u = log(github_token)
    repo = u.get_repo(repo_name)
    issue = repo.get_issue(GET_UP_ISSUE_NUMBER)
    is_today = get_today_shanbay_status(issue)
    body = get_latest_record(shanbay_username)

    if is_today:
        print('今天已经打过卡啦')
        comment = list(issue.get_comments())[-1]
        comment.edit(body)
    else:
        issue.create_comment(body)
    
    if tele_token and tele_chat_id:
        requests.post(
                url="https://api.telegram.org/bot{0}/{1}".format(
                    tele_token, "sendMessage"
                ),
                data={
                    "chat_id": tele_chat_id,
                    "text": body,
                },
            )
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    parser.add_argument("--shanbay_username", help="shanbay_username", nargs="?", default="", const="")
    parser.add_argument("--tele_token", help="tele_token", nargs="?", default="", const="")
    parser.add_argument("--tele_chat_id", help="tele_chat_id", nargs="?", default="", const="")
    options = parser.parse_args()
    main(
        options.github_token,
        options.repo_name,
        options.shanbay_username,
        options.tele_token,
        options.tele_chat_id,
    )