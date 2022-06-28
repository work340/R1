import requests, json, time, base64,random, string, re, os

#----Input authorization-----
auth = 'authorization:Bearer 51435|IEgOZV5m5IIbjJ0nAhWhVWDuBElXrEi9EtAvUrFb'



#COLOR CODES
B  = "\u001b[30;1m"
R  = "\u001b[31;1m"
G  = "\u001b[32;1m"
Y  = "\u001b[33;1m"
Bl = "\u001b[34;1m"
M  = "\u001b[35;1m"
C  = "\u001b[36;1m"
W  = "\u001b[37;1m"

while True:
  a = 0
  while a < 4:
    a = a + 1 
    data = f'"task_id":{a},"url":"","is_last":false,"key":null,"result":null'
    data = "{"+data+"}"
    lenth = str(len(data))
    url = "https://info.tmswp.com/api/task_compleat"
    headers = {"Host": "info.tmswp.com", "accept": "application/json, text/plain, */*", "authorization": f"{auth}", "content-type": "application/json", "content-length": "{}".format(lenth), "accept-encoding": "gzip", "user-agent": "okhttp/3.12.12"}
    r = requests.post(url, data=data, headers=headers)
    print("\n[✓]", r.json()["message"], f": {G}{a}")
    t = 35*1
    while t:
     minss = t // 60
     secsss = t % 60
     timerr = '{:02d}:{:02d}'.format(minss, secsss)
     print(R,  "\t\t    TIME LEFT:{}".format(W),timerr, end="\r")
     time.sleep(1)
     t -= 1
     
  #-------------------Math---------------   
  message = "Invalid Task"
  while message != "Task Completed":
    url2 = "https://info.tmswp.com/captcha/api/math"
    headers2 = {"Host": "info.tmswp.com", "accept": "application/json, text/plain, */*", "authorization": "Bearer 51435|IEgOZV5m5IIbjJ0nAhWhVWDuBElXrEi9EtAvUrFb", "accept-encoding": "gzip", "user-agent": "okhttp/3.12.12"}
    r2= requests.get(url2, headers=headers2)
    key = r2.json()["key"]
    imgg = r2.json()["img"][22:]
    
    
    #-------------------Final---------------
    imggg = bytes(imgg, 'utf-8')
    with open("captcha.png", "wb") as fh:
        fh.write(base64.decodebytes(imggg))
    
    url3 = "https://info.tmswp.com/api/task_compleat"
    
    text = os.popen("tesseract captcha.png - --psm 6").read()
    ff = re.findall(r'\d+', text)
    if len(ff)==2:
      num1 = ff[0]
      num2 = ff[1]
      num3 = int(num1) + int(num2)
      res = num3
      ran = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
      
      ran2 = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
      urls = f"https://www.bluehost.com/wordpress/wordpress-hosting/?utm_source=dcm&utm_medium=display&dclid=CjkKEQjwloCSBhCl_uOM0-6-{ran}v5RdyhvwJcWfwg9our-uDf-11iRoWR3YqBHE4gaj4beFj8Pw_wcB&gclid=CjwKCAjwloCSBhAeEiwA3hVo_SMfVL23fbdOtOZ6im43kpvPDcF5SZFe4DU8Cz2BZW5Zu0s9hGncUBoCHuYQAvD_BwE&utm_campaign=affiliate-link_rtpromo_PPC&utm_affiliate=gg{ran2}"
        
      data3 = f'"task_id":5,"url":"{urls}","is_last":true,"key":"{key}","result":"{res}"'
      data3 = "{"+data3+"}"
      lenth = str(len(data3))
      headers3 = {"Host": "info.tmswp.com", "accept": "application/json, text/plain, */*", "authorization": f"{auth}", "content-type": "application/json", "content-length": f"{lenth}", "accept-encoding": "gzip", "cookie": "XSRF-TOKEN=eyJpdiI6IkRmdWErcU9VNWhsZk12cG1LOUwrMkE9PSIsInZhbHVlIjoiUVJwdUg5Q2FucXQ2bERkbmY1bU40OUFDM2FGRjEzMVk1K1o0dUxTVXA4VWNQd0crenQ1WElUZWYzL2QrK1ZhRUk2bkh1V3ZVeEJCWjV6UUFRRWZvNnpjd3ZDK2dKRkxNYnhNZXBUL0E4eU5pMEs4TjhCTzV5ZktuaWN5bzRSRmkiLCJtYWMiOiI3YTM5OWE0N2IxYjY4NWVlZGZmMmQ1YjQxNmI5ZTkwODRjZTQ5N2Y2OWU1OGQ4YjkwMjc0ODRmNmVhNWUxYzY5IiwidGFnIjoiIn0%3D; webpay_session=eyJpdiI6IjFDYVZ5RTJwUzFiTjdFbFdxdjBmUVE9PSIsInZhbHVlIjoieEhKVUg3eVRBWStoQ0k4YVdQaUdENXVjVGFQTkdaWG5tM3NKaXJKU0MvOUl4S0RiOU1xSWg2YkV0SGpQWEpFdmlQSzNOMSs0SjgvSUNmRHhpOFgyOXBhUWtqaWJqRHRFTUFYNlhQcEE3cEhVaFhlNVE0K2NFZXNmQkNBZmNNSi8iLCJtYWMiOiI2NTMzZmJiNGIwYmQ3ODlmYzQyYTgwNjhhMTRiMjgyNDIyNmE2MjAzNGY0YTFjZDUxZTExNGRmZGRhNDc0YjY0IiwidGFnIjoiIn0%3D", "user-agent": "okhttp/3.12.12"}
      r3 = requests.post(url3, data=data3, headers=headers3)
      message = str(r3.json()["message"])
      print("\n[✓]", message, f": {G}5 ~~~~~~~~~~[ ROUND CMPLETED]~~~~~~~~~~")
        
    elif len(ff)==1 and len(ff[0])==2:
      num1 = ff[0][0]
      num2 = ff[0][1]
      num3 = int(num1) + int(num2)
      res = num3
    #res = input(f"{G}[{W}+{G}] {G}Input The Result: {Y}")
      ran = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
      
      ran2 = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
      urls = f"https://www.bluehost.com/wordpress/wordpress-hosting/?utm_source=dcm&utm_medium=display&dclid=CjkKEQjwloCSBhCl_uOM0-6-{ran}v5RdyhvwJcWfwg9our-uDf-11iRoWR3YqBHE4gaj4beFj8Pw_wcB&gclid=CjwKCAjwloCSBhAeEiwA3hVo_SMfVL23fbdOtOZ6im43kpvPDcF5SZFe4DU8Cz2BZW5Zu0s9hGncUBoCHuYQAvD_BwE&utm_campaign=affiliate-link_rtpromo_PPC&utm_affiliate=gg{ran2}"
        
      data3 = f'"task_id":5,"url":"{urls}","is_last":true,"key":"{key}","result":"{res}"'
      data3 = "{"+data3+"}"
      lenth = str(len(data3))
      
      
      headers3 = {"Host": "info.tmswp.com", "accept": "application/json, text/plain, */*", "authorization": f"{auth}", "content-type": "application/json", "content-length": f"{lenth}", "accept-encoding": "gzip", "cookie": "XSRF-TOKEN=eyJpdiI6IkRmdWErcU9VNWhsZk12cG1LOUwrMkE9PSIsInZhbHVlIjoiUVJwdUg5Q2FucXQ2bERkbmY1bU40OUFDM2FGRjEzMVk1K1o0dUxTVXA4VWNQd0crenQ1WElUZWYzL2QrK1ZhRUk2bkh1V3ZVeEJCWjV6UUFRRWZvNnpjd3ZDK2dKRkxNYnhNZXBUL0E4eU5pMEs4TjhCTzV5ZktuaWN5bzRSRmkiLCJtYWMiOiI3YTM5OWE0N2IxYjY4NWVlZGZmMmQ1YjQxNmI5ZTkwODRjZTQ5N2Y2OWU1OGQ4YjkwMjc0ODRmNmVhNWUxYzY5IiwidGFnIjoiIn0%3D; webpay_session=eyJpdiI6IjFDYVZ5RTJwUzFiTjdFbFdxdjBmUVE9PSIsInZhbHVlIjoieEhKVUg3eVRBWStoQ0k4YVdQaUdENXVjVGFQTkdaWG5tM3NKaXJKU0MvOUl4S0RiOU1xSWg2YkV0SGpQWEpFdmlQSzNOMSs0SjgvSUNmRHhpOFgyOXBhUWtqaWJqRHRFTUFYNlhQcEE3cEhVaFhlNVE0K2NFZXNmQkNBZmNNSi8iLCJtYWMiOiI2NTMzZmJiNGIwYmQ3ODlmYzQyYTgwNjhhMTRiMjgyNDIyNmE2MjAzNGY0YTFjZDUxZTExNGRmZGRhNDc0YjY0IiwidGFnIjoiIn0%3D", "user-agent": "okhttp/3.12.12"}
      r3 = requests.post(url3, data=data3, headers=headers3)
      message = str(r3.json()["message"])
      print("\n[✓]", message, f": {G}5 ~~~~~~~~~~[ ROUND CMPLETED]~~~~~~~~~~")
    t = 65*1
    while t:
       minss = t // 60
       secsss = t % 60
       timerr = '{:02d}:{:02d}'.format(minss, secsss)
       print(R,  "\t\t    TIME LEFT:{}".format(W),timerr, end="\r")
       time.sleep(1)
       t -= 1
    
  
