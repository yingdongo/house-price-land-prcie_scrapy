import scrapy
import datetime
from lianjia_scrapy.items import CommunityItem

class CommunitySpider(scrapy.Spider):
    name = "community"
    url = 'https://cd.lianjia.com/xiaoqu/{district}/pg{page}/'
    districtsInfo = {'jinjiang':{'name':'锦江区','district_id':'510104','level':'1'},'qingyang':{'name':'青羊区','district_id':'510105','level':'1'},'wuhou':{'name':'武侯区','district_id':'510107','level':'1'},'gaoxin7':{'name':'高新区','district_id':'510103','level':'1'},'chenghua':{'name':'成华区','district_id':'510108','level':'1'},'jinniu':{'name':'金牛区','district_id':'510106','level':'1'},'tianfuxinqu':{'name':'天府新区','district_id':'510106','level':'2'},'gaoxinxi1':{'name':'高新西区','district_id':'510124','level':'2'},'shuangliu':{'name':'双流区','district_id':'510122','level':'2'},'wenjiang':{'name':'温江区','district_id':'510115','level':'2'},'pidou':{'name':'郫都区','district_id':'510124','level':'2'},'longquanyi':{'name':'龙泉驿区','district_id':'510112','level':'2'},'xindou':{'name':'新都区','district_id':'510114','level':'2'},'tianfuxinqunanqu':{'name':'天府新区南区','district_id':'510186','level':'2'}}
    districts = ['jinjiang','qingyang','wuhou','gaoxin7','chenghua','jinniu','tianfuxinqu','gaoxinxi1','shuangliu','wenjiang','pidou','longquanyi','xindou','tianfuxinqunanqu']
    def start_requests(self):
        for district in self.districts:
            yield scrapy.Request(self.url.format(district=district, page=1), callback=self.parse,meta={'page': 1, 'district': district, 'retryCount':0})

    def parse(self, response):
        house_urls = response.css('.xiaoquListItem> div.info > div.title > a::attr(href)').extract()
        totalCount = response.css('body > div.content > div.leftContent > div.resultDes.clear > h2 > span::text').extract_first()
        district = response.meta.get('district') 
        for url in house_urls:
            yield scrapy.Request(url=url, callback=self.parse_house,meta={'district': district})
        retryCount = response.meta.get('retryCount') 
        if int(totalCount) == 0: 
            if retryCount < 5:
                page = response.meta.get('page') 
                retryCount += 1
                yield scrapy.Request(self.url.format(district=district, page=page), callback=self.parse,meta={'page': page, 'district': district, 'retryCount':retryCount}, dont_filter=True)
        else :
            retryCount = 0 
            page = response.meta.get('page') + 1
            yield scrapy.Request(self.url.format(district=district, page=page), callback=self.parse,meta={'page': page, 'district': district, 'retryCount':retryCount}, dont_filter=True)
    def parse_house(self, response):
        item = CommunityItem()
        district = response.meta.get('district') 
        item['community_name'] = response.css('body > div.xiaoquDetailbreadCrumbs > div.fl.l-txt > a:nth-child(9)::text').extract_first()
        item['community_id']  = response.css("body > div.xiaoquDetailbreadCrumbs > div.fl.l-txt > a:nth-child(9)::attr(href)").extract_first().split('/')[2]
        item['building_age'] = response.css("body > div.xiaoquOverview > div.xiaoquDescribe.fr > div.xiaoquInfo > div:nth-child(1) > span.xiaoquInfoContent::text").extract_first()[0:4]
        price= response.css("body > div.xiaoquOverview > div.xiaoquDescribe.fr > div.xiaoquPrice.clear > div > span.xiaoquUnitPrice::text").extract_first()
        item['community_average_price'] = price
        item['district'] = self.districtsInfo[district]['name']
        item['district_id'] = self.districtsInfo[district]['district_id']
        item['level'] = self.districtsInfo[district]['level']
        date_data = datetime.datetime(2018,12,31)
        item['year'] = date_data.year
        item['month'] = date_data.month
        price_dict={'price':price,'writeTime': datetime.datetime.now()}
        item['writeTime']  = datetime.datetime.now()
        print('item:')
        print(item)
        yield item
