class Find:

    def find_in_baidu (self, vaule):
        import requests as re
        from lxml import etree
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        url = 'https://www.baidu.com/s'
        
        params = {
            'wd' :vaule,
            'pn':
        }
        response = re.get(url=url, params=params, headers=headers).text
        etree = etree.HTML(response)
        link = etree.xpath('//div[@id="content_left"]//h3[@class="t"]')
        val = etree.xpath('//div [@id="content_left"]//div[@class="c-abstract"]')
        fp = open('1.txt', 'w', encoding="utf-8")
        for every_link, every_val in zip(link, val):
            title = every_link.xpath(".//text()")
            all_vau = every_val.xpath(".//text()")
            for all_titile in title:
                fp.write(all_titile)
            fp.write("\n")
            for vul in all_vau:
                fp.write(vul)
            fp.write("\n\n\n\n\n")





if __name__ == "__main__":
    find = Find()
    find.find_in_baidu("123")