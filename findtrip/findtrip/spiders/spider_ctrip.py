import scrapy
from findtrip.items import FindtripItem
import json
from datetime import datetime, timedelta

class CtripSpider(scrapy.Spider):
    name = 'Ctrip'
    start_urls = [
            f"http://flights.ctrip.com/booking/XMN-BJS-day-1.html?DDate1={(datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')}"
            ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        # 定位到包含所有航班信息的最外层div
        flights = sel.xpath("//div[@class='seo-flight-list']/div[@class='list-content']/div[@class='list-content-item-transit']")
        
        items = []
        for flight in flights:
            item = FindtripItem()

            # 提取航空公司名称和飞机型号
            airline_names = flight.xpath(".//div[@class='airline-name']/text()").extract()
            plane_infos = flight.xpath(".//span[@class='plane-No']/text()").extract()
            
            plane_full_name = []
            for i in range(len(airline_names)):
                airline_names[i] = airline_names[i].strip()
                plane_infos[i] = plane_infos[i].strip()
                plane_full_name.append(airline_names[i] + ' ' + plane_infos[i])


            # 提取起降时间和机场信息
            depart_times = flight.xpath(".//div[@class='depart-box']/div[@class='time']/text()").extract()
            depart_airports = flight.xpath(".//div[@class='airport']/span[1]/text()").extract()

            arrive_times = flight.xpath(".//div[@class='arrive-box']/div[@class='time']/div/text()").extract()

            # 提取价格和舱位信息
            prices = flight.xpath(".//div[@class='price-detail']/span[@class='price']/dfn/following-sibling::text()").extract()
            cabin_classes = flight.xpath(".//div[@class='rate-detail']/div[@class='className']/text()").extract()

            transfer_duration = flight.xpath(".//span[@class='transfer-duration']/text()").extract()

            # 填充item
            item['site'] = 'Ctrip'
            item['plane_info'] = ", ".join(plane_full_name)
            item['departure_time'] = depart_times[0] if len(depart_times) > 0 else ''
            item['departure_airport'] = depart_airports[0]
            item['arrive_time'] = arrive_times[0] if len(arrive_times) > 0 else ''
            item['arrive_airport'] = depart_airports[1]
            item['price'] = prices[0] if len(prices) > 0 else ''
            item['cabin_class'] = cabin_classes[0] if len(cabin_classes) > 0 else ''
            item['transfer_duration'] = transfer_duration[0] if len(transfer_duration) > 0 else ''

            items.append(item)
        
        return items