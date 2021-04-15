from scrapy.http import Request
from scrapy.spiders import CSVFeedSpider


class TaxscrapSpider(CSVFeedSpider):
    name = 'taxscrap'
    start_urls = ['file:///E:/Scrapy%20Practice/Oreleans_Scraping/oreleans/taxurl.csv']
    delimiter = ','
    headers = ['URL']

    def parse_row(self, response, row):
        yield Request(url = row['URL'], callback = self.scrapData)           
        
    
    def scrapData(self, response):
        print("Working URL - " + response.url)
        
        curURL = response.url
        
        if curURL.find('Type=1') >= 0:
            try:
                totalTaxDue = response.css('span#ctl10_TotalRealEstateTaxesDue::text').get()
            except:
                totalTaxDue = ""
            
            try:
                tmpHTML = response.css('table#ctl10_RealEstateTaxData').extract()[0]
            except:
                tmpHTML = ""
        
        elif curURL.find('Type=2') >= 0:            
            try:
                totalTaxDue = response.css('span#ctl10_TotalBusinessPersonalPropertyTaxesDue::text').get()
            except:
                totalTaxDue = ""
            
            try:
                tmpHTML = response.css('table#ctl10_BusinessPersonalPropertyTaxData').extract()[0]
            except:
                tmpHTML = ""
        
                
        #Split table tax data by row
        tmpArray = tmpHTML.split('</tr>')
        taxHTML = ""
        
        #Collect all Year and Tax Amount        
        for x in range(1, len(tmpArray)-1):            
            
            #Get Year-Type
            try:
                yType = tmpArray[x].split('</td>')[0]
                yType = yType.split('<td align="left">')[1]
                yType = yType.replace('\r\n', '').strip()
                yType = yType.replace('\r\n', '').strip()
            except:
                yType = ""
            
            
            #Get Due Amount
            try:
                taxDueHTML = tmpArray[x].split('<td align="right">')
                taxDue = taxDueHTML[len(taxDueHTML)-1]
                taxDue = taxDue.replace('</td>', '')
                taxDue = taxDue.replace('\r\n', '').strip()
            except:
                taxDue = ""
            
            
            #Merge both Values
            taxHTML =  taxHTML + yType + "XYBC" + taxDue + "|"
        
                      
        yield {
            'URL': response.url,
            'totalTaxDue': totalTaxDue,
            'TaxHTML': taxHTML,
        }