# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonscraperItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/b/ref=bhp_brws_100bks?ie=UTF8&node=8192263011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=3NYHS4E51D00BH667TXW&pf_rd_r=3NYHS4E51D00BH667TXW&pf_rd_t=101&pf_rd_p=1d097b73-6dd4-48f4-a8d9-9d4c2b6d7c91&pf_rd_p=1d097b73-6dd4-48f4-a8d9-9d4c2b6d7c91&pf_rd_i=283155'
    ]

    def parse(self, response):
        items = AmazonscraperItem()

        book_name = response.css('.a-link-normal .a-size-base::text').extract()
        author = response.css('.acs_product-metadata__contributors::text').extract()
        price = response.css('.acs_product-price__dual-format-price .a-box-group:nth-child(1) .acs_product-price__buying').css('::text').extract()
        image_link = response.css('.aok-align-center::attr(src)').extract()

        items['book_name'] = book_name
        items['author'] = author
        items['price'] = price
        items['image_link'] = image_link

        yield items


