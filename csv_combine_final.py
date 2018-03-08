#!/usr/bin/python3
from xml.dom.minidom import parse
import csv
import glob

files = glob.glob("/home/hotsea/2014/*.xml")

f = open('/home/hotsea/IRS/Filer2014.csv', 'w+')
csvwriter = csv.writer(f)
head = ['EIN', 'BusinessNameLine1Txt', 'BusinessNameControlTxt', 'PhoneNum', 'AddressLine1Txt', 'CityNm', 'StateAbbreviationCd', 'ZIPCd', 'TaxYr']
csvwriter.writerow(head)




for file in files:

	dom = parse(file)


	preparer = dom.getElementsByTagName('Filer')
	ein = dom.getElementsByTagName('EIN')
	name = dom.getElementsByTagName('BusinessNameLine1Txt')
	name1 = dom.getElementsByTagName('BusinessNameLine1')
	state = dom.getElementsByTagName('StateAbbreviationCd')
	state1 = dom.getElementsByTagName('State')
	taxyear = dom.getElementsByTagName('TaxYr')
	taxyear1 = dom.getElementsByTagName('TaxYear')
	namecontrol = dom.getElementsByTagName('BusinessNameControlTxt')
	namecontrol1 = dom.getElementsByTagName('NameControl')
	phone = dom.getElementsByTagName('PhoneNum')
	phone1 = dom.getElementsByTagName('Phone')
	address = dom.getElementsByTagName('AddressLine1Txt')
	address1 = dom.getElementsByTagName('AddressLine1')
	city = dom.getElementsByTagName('CityNm')
	city1 = dom.getElementsByTagName('City')
	zipcode = dom.getElementsByTagName('ZIPCd')
	zipcode1 = dom.getElementsByTagName('ZIPCode')
	    
	if (len(preparer) < 1):

	    try:
	        my_ein = ein[0]
	        my_child = my_ein.firstChild
	        my_text = my_child.data
	    except:
	        my_text = "Null"
	    
	    if (len(name) < 1):
	        try:
	            my_name = name1[0]
	            my_child1 = my_name.firstChild
	            my_text1 = my_child1.data
	        except:
	            my_text1 = "Null"
	    else:
	        try:
	            my_name = name[0]
	            my_child1 = my_name.firstChild
	            my_text1 = my_child1.data
	        except:
	            my_text1 = "Null"

	    if (len(namecontrol) < 1): 
	        try:
	            my_namecontrol = namecontrol1[0]
	            my_child2 = my_namecontrol.firstChild
	            my_text2 = my_child2.data
	        except:
	            my_text2 = "Null"
	    else:
	        try:
	            my_namecontrol = namecontrol[0]
	            my_child2 = my_namecontrol.firstChild
	            my_text2 = my_child2.data
	        except:
	            my_text2 = "Null"
	            
	    if (len(phone) < 1):        
	        try:
	            my_phone = phone1[0]
	            my_child3 = my_phone.firstChild
	            my_text3 = my_child3.data
	        except:
	            my_text3 = "Null"
	    else:
	        try:
	            my_phone = phone[0]
	            my_child3 = my_phone.firstChild
	            my_text3 = my_child3.data
	        except:
	            my_text3 = "Null"
	        


	    if (len(address) < 1):
	        try:
	            my_address = address1[0]
	            my_child4 = my_address.firstChild
	            my_text4 = my_child4.data
	        except:
	            my_text4 = "Null"
	    else:
	        try:
	            my_address = address[0]
	            my_child4 = my_address.firstChild
	            my_text4 = my_child4.data
	        except:
	            my_text4 = "Null"

	    if (len(city) < 1):
	        try:
	            my_city = city1[0]
	            my_child5 = my_city.firstChild
	            my_text5 = my_child5.data
	        except:
	            my_text5 = "Null"
	    else:
	        try:
	            my_city = city[0]
	            my_child5 = my_city.firstChild
	            my_text5 = my_child5.data
	        except:
	            my_text5 = "Null"

	    if (len(state) < 1):
	        try:
	            my_state = state1[0]
	            my_child6 = my_state.firstChild
	            my_text6 = my_child6.data
	        except:
	            my_text6
	    else:
	        try:
	            my_state = state[0]
	            my_child6 = my_state.firstChild
	            my_text6 = my_child6.data
	        except:
	            my_text6

	    if (len(zipcode) < 1):
	        try:
	            my_zipcode = zipcode1[0]
	            my_child7 = my_zipcode.firstChild
	            my_text7 = my_child7.data
	        except: 
	            my_text7 = "Null"
	    else:
	        try:
	            my_zipcode = zipcode[0]
	            my_child7 = my_zipcode.firstChild
	            my_text7 = my_child7.data
	        except: 
	            my_text7 = "Null"

	    if (len(taxyear) < 1):
	        try:
	            my_tax_year = taxyear1[0]
	            my_child8 = my_tax_year.firstChild
	            my_text8 = my_child8.data
	        except:
	            my_text8 = "Null"

	    else:
	    	try:
	    		my_tax_year = taxyear1[0]
	    		my_child8 = my_tax_year.firstChild
	    		my_text8 = my_child8.data
	    	except:
	    		my_text8 = "Null"



	else:


		if ((len(taxyear) < 1 ) and (len(phone) < 1) and (len(namecontrol) < 1)):


			if (len(ein) > 1):

			              
			    try:
			        my_ein = ein[1]
			        my_child = my_ein.firstChild
			        my_text = my_child.data
			    except:
			        my_text = "Null"

			else:

			    try:
			        my_ein = ein[0]
			        my_child = my_ein.firstChild
			        my_text = my_child.data
			    except:
			        my_text = "Null"



			if (len(name) > 1):        


			    try:
			        my_name = name1[1]
			        my_child1 = my_name.firstChild
			        my_text1 = my_child1.data
			    except:
			        my_text1 = "Null"
			else:

			    try:
			        my_name = name1[0]
			        my_child1 = my_name.firstChild
			        my_text1 = my_child1.data
			    except:
			        my_text1 = "Null"

			if (len(namecontrol1) > 1):

			    try:
			        my_namecontrol = namecontrol1[1]
			        my_child2 = my_namecontrol.firstChild
			        my_text2 = my_child2.data
			    except:
			        my_text2 = "Null"

			else:

			    try:
			        my_namecontrol = namecontrol1[0]
			        my_child2 = my_namecontrol.firstChild
			        my_text2 = my_child2.data
			    except:
			        my_text2 = "Null"

			if (len(phone1) > 1):

			    try:
			        my_phone = phone1[1]
			        my_child3 = my_phone.firstChild
			        my_text3 = my_child3.data
			    except:
			        my_text3 = "Null"

			else:

			    try:
			        my_phone = phone1[0]
			        my_child3 = my_phone.firstChild
			        my_text3 = my_child3.data
			    except:
			        my_text3 = "Null"

			if (len(address) > 1):

			    try:
			        my_address = address1[1]
			        my_child4 = my_address.firstChild
			        my_text4 = my_child4.data
			    except:
			        my_text4 = "Null"
			else:

			    try:
			        my_address = address1[0]
			        my_child4 = my_address.firstChild
			        my_text4 = my_child4.data
			    except:
			        my_text4 = "Null"

			if (len(city) > 1):

			    try:
			        my_city = city1[1]
			        my_child5 = my_city.firstChild
			        my_text5 = my_child5.data
			    except:
			        my_text5 = "Null"

			else:

			    try:
			        my_city = city1[0]
			        my_child5 = my_city.firstChild
			        my_text5 = my_child5.data
			    except:
			        my_text5 = "Null"



			if (len(state) > 1):

			    try:
			        my_state = state1[1]
			        my_child6 = my_state.firstChild
			        my_text6 = my_child6.data
			    except:
			        my_text6 = "Null"

			else:

			    try:
			        my_state = state1[0]
			        my_child6 = my_state.firstChild
			        my_text6 = my_child6.data
			    except:
			        my_text6 = "Null"


			if (len(zipcode) > 1):

			    try:
			        my_zipcode = zipcode1[1]
			        my_child7 = my_zipcode.firstChild
			        my_text7 = my_child7.data
			    except: 
			        my_text7 = "Null"
			else:

			    try:
			        my_zipcode = zipcode1[0]
			        my_child7 = my_zipcode.firstChild
			        my_text7 = my_child7.data
			    except: 
			        my_text7 = "Null"
			try:
			    my_tax_year = taxyear1[0]
			    my_child8 = my_tax_year.firstChild
			    my_text8 = my_child8.data
			except: 
			    my_text8 = "Null"

		else:




			if (len(ein) > 1):




			              
			    try:
			        my_ein = ein[1]
			        my_child = my_ein.firstChild
			        my_text = my_child.data
			    except:
			        my_text = "Null"

			else:

			    try:
			        my_ein = ein[0]
			        my_child = my_ein.firstChild
			        my_text = my_child.data
			    except:
			        my_text = "Null"



			if (len(name) > 1):        


			    try:
			        my_name = name1[1]
			        my_child1 = my_name.firstChild
			        my_text1 = my_child1.data
			    except:
			        my_text1 = "Null"
			else:

			    try:
			        my_name = name1[0]
			        my_child1 = my_name.firstChild
			        my_text1 = my_child1.data
			    except:
			        my_text1 = "Null"

			if (len(namecontrol) > 1):

			    try:
			        my_namecontrol = namecontrol[1]
			        my_child2 = my_namecontrol.firstChild
			        my_text2 = my_child2.data
			    except:
			        my_text2 = "Null"

			else:

			    try:
			        my_namecontrol = namecontrol[0]
			        my_child2 = my_namecontrol.firstChild
			        my_text2 = my_child2.data
			    except:
			        my_text2 = "Null"

			if (len(phone) > 1):

			    try:
			        my_phone = phone[1]
			        my_child3 = my_phone.firstChild
			        my_text3 = my_child3.data
			    except:
			        my_text3 = "Null"

			else:

			    try:
			        my_phone = phone[0]
			        my_child3 = my_phone.firstChild
			        my_text3 = my_child3.data
			    except:
			        my_text3 = "Null"

			if (len(address) > 1):

			    try:
			        my_address = address1[1]
			        my_child4 = my_address.firstChild
			        my_text4 = my_child4.data
			    except:
			        my_text4 = "Null"
			else:

			    try:
			        my_address = address1[0]
			        my_child4 = my_address.firstChild
			        my_text4 = my_child4.data
			    except:
			        my_text4 = "Null"

			if (len(city) > 1):

			    try:
			        my_city = city1[1]
			        my_child5 = my_city.firstChild
			        my_text5 = my_child5.data
			    except:
			        my_text5 = "Null"

			else:

			    try:
			        my_city = city1[0]
			        my_child5 = my_city.firstChild
			        my_text5 = my_child5.data
			    except:
			        my_text5 = "Null"



			if (len(state) > 1):

			    try:
			        my_state = state1[1]
			        my_child6 = my_state.firstChild
			        my_text6 = my_child6.data
			    except:
			        my_text6 = "Null"

			else:

			    try:
			        my_state = state1[0]
			        my_child6 = my_state.firstChild
			        my_text6 = my_child6.data
			    except:
			        my_text6 = "Null"


			if (len(zipcode) > 1):

			    try:
			        my_zipcode = zipcode1[1]
			        my_child7 = my_zipcode.firstChild
			        my_text7 = my_child7.data
			    except: 
			        my_text7 = "Null"
			else:

			    try:
			        my_zipcode = zipcode1[0]
			        my_child7 = my_zipcode.firstChild
			        my_text7 = my_child7.data
			    except: 
			        my_text7 = "Null"
			try:
			    my_tax_year = taxyear[0]
			    my_child8 = my_tax_year.firstChild
			    my_text8 = my_child8.data
			except: 
			    my_text8 = "Null"

	row1 = [my_text, my_text1, my_text2, my_text3, my_text4, my_text5, my_text6, my_text7, my_text8]
	csvwriter.writerow(row1)
