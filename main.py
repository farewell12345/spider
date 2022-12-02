# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。

import requests
from bs4 import BeautifulSoup

github_url = "https://www.githubs.cn/top-china"

top_class_name = "repo-card"


def get_github_star():
    content = requests.get(github_url).content
    bs = BeautifulSoup(content, "lxml")
    top_3 = bs.find_all('div', {"class", top_class_name})
    list_data = []
    for t in top_3:
        data = {}
        url = t.find_next("a", {"class", "jss31"}).attrs['href']
        name = t.find_next("a", {"class", "jss31"}).text
        author = t.find_next("span", {"class", "Truncate-text Truncate-text--primary"}).text
        star = t.find_next("span", {"class", "MuiTypography-root ml-1 MuiTypography-caption MuiTypography-colorTextSecondary"}).text
        data['url'] = url
        data['name'] = name
        data['author'] = author
        data['star'] = star
        list_data.append(data)
    for i in list_data:
        print(i)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    get_github_star()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
