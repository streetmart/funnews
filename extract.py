# pip3 install newspaper3k 
from newspaper import Article  
from unidecode import unidecode 
import re
import json
# from newspaper import Article  
def lambda_handler(event, context):
	# url='https://www.thehindu.com/news/national/india-coronavirus-lockdown-august-7-2020-live-updates/article32290620.ece' 

	url=None
	# print(a.title)
	# print(a.summary)
	try:
		url=event['queryStringParameters']['url']
	except Exception as e:
		result={}
		result['error']="please pass url"
		return {
		'statusCode': 400,
		'headers': {"content-type": "application/json"},
		'body': json.dumps(result)
		}
	a=Article(url) 
	a.download()
	a.parse()
	a.nlp()
	# print(event)
	# print(context)
	quotes=re.findall('"([^"]*)"',unidecode(a.text)) 
	result={}
	result['title']=a.title
	result['text']=a.text
	result['summary']=a.summary
	result['quotes']=quotes
	result['quotes_num']=len(quotes)
	return {
		'statusCode': 200,
		'headers': {"content-type": "application/json"},
		'body': json.dumps(result)
		}
#     url='https://www.thehindu.com/news/national/india-coronavirus-lockdown-august-7-2020-live-updates/article32290620.ece' 
#     a=Article(url) 
#     a.download()
#     a.parse()
#     a.nlp()
#     print(a.title)
#     print(a.summary)
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps(a.title)
#     }

#print(a.text)