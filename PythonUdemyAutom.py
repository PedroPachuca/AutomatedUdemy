from json import loads 
from bs4 import BeautifulSoup
import mechanize

importio_url = "https://api.import.io/store/data/5ff13e3c-2c37-447c-bb1a-28da65e118b7/_query?input/webpage/url=http%3A%2F%2Fgrowthcoupon.com%2Fstores%2Fudemy-coupons%2F&_user=482e5f94-ba64-4e8a-8a23-073abe2f2d4c&_apikey=482e5f94ba644e8a8a23073abe2f2d4c8b895edbbbd53af9fd553fdd6ebd3c3441250119385aaa0cd48dfe4ef6bdb5d3efe0d6649221846915d94c53eb831f47808517a6eaa6466d01031b0f7dc95b9b"
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
sign_in = br.open("https://www.udemy.com/join/login-popup/")
br.select_form(nr=3)
br["email"] = "EMAIL"
br["password"] = "PASSWORD"
logged_in = br.submit()

growthcoupon = br.open(importio_url)
json_obj = loads(growthcoupon.read())

    
for course_links in json_obj["results"]:
    course_page = br.open(course_links["couponcode_link"])
    soup = BeautifulSoup(course_page)
    for link in soup.find_all("a"):
        req_link = link.get('href')
        if 'https://www.udemy.com/payment/checkout' in str(req_link):
            print req_link
            br.open(str(req_link))
            print "Done!"
            break
