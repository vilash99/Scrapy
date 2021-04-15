from scrapy.http import Request
from scrapy.spiders import CSVFeedSpider


class ScraperSpider(CSVFeedSpider):
    name = 'scraper111'
    start_urls = ['file:///E:/Scrapy%20Practice/Oreleans_Scraping/oreleans/orelansurl.csv']
    delimiter = ','
    headers = ['URL']    

    
    def parse_row(self, response, row):         
        yield Request(url = row['URL'], callback = self.scrapData)           
     

    def scrapData(self, response):
        print("Working URL - " + response.url)     
        
        
        def extract_with_css(query, index):            
            extractData = ""
            try:
                extractData = response.css(query).extract()[index]
            except:
                extractData = ""
            
            return extractData
        
        #Extrct building Image        
        try:
            data = response.css("td img").extract()
            photo = data[len(data)-1] #Get Last Image   
        except:
            photo = ""        
        
        #Extract Tax Bill URL
        TaxBillURL = ""
        try:
            TaxBillURL = response.css('a[href*="http://services.nola.gov/service.aspx?load=treasury"]::attr(href)').get()
        except:
            TaxBillURL = ""
        
        yield {
            'URL': response.url,            
            'Ownername': extract_with_css("td.owner_value", 0),   
            'Todaydate': response.css("td.owner_value").extract()[1],
            'Mailingaddress': response.css("td.owner_value").extract()[2],
            'Municipaldistrict': response.css("td.owner_value").extract()[3],
            'Locationaddress': response.css("td.owner_value").extract()[4],
            'TaxBillURL': TaxBillURL,
            'Propertyclass': response.css("td.owner_value").extract()[6],
            'Subdivisionname': response.css("td.owner_value").extract()[8],
            'Landarea': response.css("td.owner_value").extract()[9],
            'Buildingarea': response.css("td.owner_value").extract()[11],
            'Parcelmap': response.css("td.owner_value").extract()[17],
            'Assessmentarea': response.css("td.owner_value").extract()[19],
            'Viyear': response.css("td.tax_value").extract()[0],
            'Vilandvalue': response.css("td.tax_value").extract()[1],
            'Vibuildingvalue': response.css("td.tax_value").extract()[2],
            'Vitotalvalue': response.css("td.tax_value").extract()[3],
            'Viassessedlandvalue': response.css("td.tax_value").extract()[4],
            'Viassessedbuildingvalue': response.css("td.tax_value").extract()[5],
            'Vitotalassessedvalue': response.css("td.tax_value").extract()[6],
            'Vihomesteadexemptionvalue': response.css("td.tax_value").extract()[7],
            'Vitaxableassessment': response.css("td.tax_value").extract()[8],
            'Stdate1': response.css("tr.even td.sales_value").extract()[0],
            'Stprice1': response.css("tr.even td.sales_value").extract()[1],
            'Stgrantor1': response.css("tr.even td.sales_value").extract()[2],
            'Stgrantee1': response.css("tr.even td.sales_value").extract()[3],
            'Stdate2': response.css("tr.odd td.sales_value").extract()[0],
            'Stprice2': response.css("tr.odd td.sales_value").extract()[1],
            'Stgrantor2': response.css("tr.odd td.sales_value").extract()[2],
            'Stgrantee2': response.css("tr.odd td.sales_value").extract()[3],
            'Stdate3': response.css("tr.even td.sales_value").extract()[6],
            'Stprice3': response.css("tr.even td.sales_value").extract()[7],
            'Stgrantor3': response.css("tr.even td.sales_value").extract()[8],
            'Stgrantee3': response.css("tr.even td.sales_value").extract()[9],            
            'Buildingphoto': photo,
        }
        
        
