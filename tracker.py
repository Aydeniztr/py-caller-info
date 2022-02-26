from phonenumbers import parse,carrier,timezone # mem_info(20100kb)
from sys import argv 


banner = '''
  .oooooo.             oooo  oooo                              o8o               .o88o.           
 d8P'  `Y8b            `888  `888                              `"'               888 `"           
888           .oooo.    888   888   .ooooo.  oooo d8b         oooo  ooo. .oo.   o888oo   .ooooo.  
888          `P  )88b   888   888  d88' `88b `888""8P         `888  `888P"Y88b   888    d88' `88b 
888           .oP"888   888   888  888ooo888  888     8888888  888   888   888   888    888   888 
`88b    ooo  d8(  888   888   888  888    .o  888              888   888   888   888    888   888 
 `Y8bood8P'  `Y888""8o o888o o888o `Y8bod8P' d888b            o888o o888o o888o o888o   `Y8bod8P' 
                                                                                                  
author: Ahmet Yigit AYDENIZ                                                                                               
'''


usg = '''
costum argumants:

'--help,-h'

'--list'

'--location'

'''

# setting up ANSI colors:

# black   = '\033[30m'
# red     = '\033[31m'
# green   = '\033[32m'
# yellow  = '\033[33m'
# blue    = '\033[34m'
# magenta = '\033[35m'
# cyan    = '\033[36m'
# white   = '\033[37m'


def black():
	print('\033[30m')

def red():
	print('\033[31m')

def green():
	print('\033[32m')

def yellow():
	print('\033[33m')

def blue():
	print('\033[34m')

def magenta():
	print('\033[35m')

def cyan():
	print('\033[36m')

def white():
	print('\033[37m')
	
def reset():
	print('\033[0m')
	
#some functions to make the code easier to write
#I am not gonna explain them they are all self explanatory
	
def generate_maps_link(gps):

	string = ''.join(gps).replace("/", "").replace("Europe","")
	gps_query = string
	maps = 'https://www.google.com/maps/place/'+ gps_query
	 
	print ('\nsee the location in google maps:\n'+ maps +'\n')
	

def get_info(phone_number):
	
	print('\n')
	
	print(banner)

	ni = parse(str(phone_number))
	print (ni)
	
	sp = carrier.name_for_number(ni,'en')
	print(sp)
	
	tz = timezone.time_zones_for_number(ni)
	print(''.join(tz))
	
	generate_maps_link(tz)

if len(argv) <= 1:
	
	print(banner + usg)

elif argv[1] == '--list':

	print(banner)
	
	while True:
		
		try:

			with open ("list.txt", "r") as mylist:
				data = mylist.read().splitlines()
				
				choice = input('Do you want to save the output in the output-logs.txt file ? (y/n):')
				
				for i in data:
					
					get_info(i)
					
					if choice == 'y':
						with open("output.txt", "a") as f:
							print(get_info(i), file=f)
					else:
						exit()
				
		except:
			
			print('there in no file named list.txt or the file \nis empty.(please check the file)\n')
			exit()
				
				
elif argv[1] == '--help' or argv[1] == '-h':

	print(banner + usg)

elif argv[1] == '--location':

	gps = argv[2]
	print(banner)
	generate_maps_link(gps)
	
else:

	print(banner)
	phone_number = argv[1]
	get_info(phone_number)
