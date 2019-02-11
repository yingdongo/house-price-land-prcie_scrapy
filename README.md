# house-price-land-prcie_scrapy


## Usage

成都房价地价信息(https://www.blocknews.xyz/)
爬虫源码,`community_spider.py`爬取成都小区的二手房参考均价, `land_spider.py`爬取成都拍卖住宅用地的相关信息。

## Configuration

使用前请在`pipelines.py`设置mysql.

## Install

```
docker build -t house-price-land-prcie_scrapy .
docker run -d house-price-land-prcie_scrapy

```
