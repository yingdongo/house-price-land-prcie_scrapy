import scrapy
import datetime
import time
from lianjia_scrapy.items import LandItem

class LandSpider(scrapy.Spider):
    name = "land"
          
    url = 'https://land.3fang.com/market/510100_{district_id}_1_2_2____1_0_{page}.html'
    districts = ['jinjiang','qingyang','wuhou','chenghua','jinniu','tianfuxinqu','gaoxin7','shuangliu','wenjiang','pidou','longquanyi','xindou','qingbaijiang','xinjin','jintang','chongzhou','dujiangyan','dayi','pujiang','pengzhou','qionglai']
    district_ids = ['510104','510105','510107','510108','510106','510186','510103','510122','510115','510124','510112','510114','510132','510113','510121','510184','510181','510129','510131','510182','510183']
    def start_requests(self):
        for district_id in self.district_ids:
            yield scrapy.Request(self.url.format(district_id=district_id, page=1), callback=self.parse,meta={'page': 1, 'district_id':district_id})

    def parse(self, response):
        house_urls = response.css('#landlb_B04_22 > dd> div.list28_text.fl > h3 > a::attr(href)').extract()
        district_id = response.meta.get('district_id') 
        count = response.css('body > div.main > div.mt10.clr > div.area650.fl > div.nav_tab01 > div.tdxx.fr > span::text').extract_first()
        for url in house_urls:
            url = 'https://land.3fang.com' + url
            yield scrapy.Request(url=url, callback=self.parse_land,meta={'district_id':district_id})
        if int(count)>0:
            page = response.meta.get('page') + 1
            yield scrapy.Request(self.url.format(district_id=district_id, page=page), callback=self.parse,meta={'page': page ,'district_id':district_id})
    def parse_land(self, response):
        item = LandItem()
        time.sleep(2)
        item['title'] = response.css('#printData1 > div.tit_box01::text').extract_first()

        total_land_area = response.css('#printData1 > div:nth-child(5) > table > tbody > tr:nth-child(2) > td:nth-child(1) > em::text').extract_first()
        item['total_land_area'] = total_land_area if total_land_area!='暂无' else None
        construction_land_area = response.css('#printData1 > div:nth-child(5) > table > tbody > tr:nth-child(2) > td:nth-child(2) > em::text').extract_first()
        item['construction_land_area'] = construction_land_area if construction_land_area!= '暂无' else None
        floor_area = response.css('#printData1 > div:nth-child(5) > table > tbody > tr:nth-child(3) > td:nth-child(1) > em::text').extract_first()
        item['floor_area'] = floor_area if floor_area != '暂无' else None
        trade_result = response.css("#printData1 > div:nth-child(5) > div.banbox > table > tbody > tr:nth-child(1) > td:nth-child(1)::text").extract_first()
        item['trade_result'] = trade_result if trade_result != '暂无' else None
        land_id = response.css("#printData1 > div.menubox01.mt20 > span::text").extract_first()
        item['land_id'] = land_id[5:]
        item['district_id'] = response.meta.get('district_id')
        plot_ratio = response.css("#printData1 > div:nth-child(5) > table > tbody > tr:nth-child(4) > td:nth-child(1)::text").extract_first()
        item['plot_ratio'] = plot_ratio if plot_ratio != '暂无' else None
        commercial_ratio=response.css("#printData1 > div:nth-child(5) > table > tbody > tr:nth-child(5) > td:nth-child(1)::text").extract_first()
        item['commercial_ratio'] = commercial_ratio if commercial_ratio!='暂无' else None
        location=response.css("#printData1 > div:nth-child(5) > table > tbody > tr:nth-child(7) > td:nth-child(2)::text").extract_first()
        item['location'] = location if location != '暂无' else None
        land_usage=response.css("#printData1 > div:nth-child(5) > table > tbody > tr:nth-child(8) > td:nth-child(2) > a::text").extract_first()
        item['land_usage'] = land_usage if land_usage != '暂无' else None
        starting_price = response.css("#printData1 > div:nth-child(5) > div.banbox > table > tbody > tr:nth-child(4) > td:nth-child(1)::text").extract_first()
        item['starting_price'] = starting_price[0:-2] if starting_price!='暂无' else None
        buyer = response.css("#printData1 > div:nth-child(5) > div.banbox > table > tbody > tr:nth-child(1) > td:nth-child(2)::text").extract_first()
        item['buyer'] = buyer if buyer!='暂无' else None
        unit_price = response.css("#printData1 > div:nth-child(5) > div.banbox > table > tbody > tr:nth-child(5) > td:nth-child(1)::text").extract_first()
        item['unit_price'] = unit_price[0:-1] if unit_price!='暂无' else None
        total_price = response.css("#printData1 > div:nth-child(5) > div.banbox > table > tbody > tr:nth-child(4) > td:nth-child(2)::text").extract_first()
        item['total_price'] = total_price[0:-2] if total_price!='暂无' else None
        trade_form=response.css("#printData1 > div:nth-child(5) > table > tbody > tr:nth-child(6) > td:nth-child(2)::text").extract_first()
        item['trade_form'] = trade_form if trade_form!='暂无' else None
        trade_time=response.css("#printData1 > div:nth-child(5) > div.banbox > table > tbody > tr:nth-child(3) > td:nth-child(1)::text").extract_first()
        item['trade_time'] = datetime.date.fromisoformat(trade_time) if trade_time!='暂无' else None
        item['writeTime']  = datetime.datetime.now()
        yield item
