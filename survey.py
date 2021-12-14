# ewise_cyber = pgodston@ewiseinc.com

print("What is your first name?", end='  ')
name = input()
print("What is your business email address?", end='  ')

email = input()
print("What is your phone (where you have personal voicemail)?", end='  ')
phone = input()

print(f"So {name}, you can suggest devices that we should remove from the network and (for any questions) we can reach you at {email} or calling {phone}? Great!")
print("How many hospitals are there in your organization?", end='  ')
hospitals = input()
print("How many clinics are there in your organization?", end='  ')
clinics = input()

print("What is the #1 most important device in your organization?")
print("For example, Siemens 3T 70", end='  ')
top_device = input()
print("What are top three (in order) obsolete devices in your organization?")
print("For example, GE MAC 800 ECG", end='  ')
most_numerous_device = input()
next_most_numerous_device = input()
third_most_numerous_device = input()

print(f"So we ought to download data from the {top_device} device(s), the {most_numerous_device} , the {next_most_numerous_device} and the {third_most_numerous_device} device(s) ?  Okay.")

print(f"In which of your {hospitals} hospitals can we find the {top_device} for download??", end='  ')
mostval_demo_hosp = input()
print(f"Which department(s) will coordinate our download visit(s) ?", end='  ')
mostval_demo_department = input()
print("Who is the best contact to coordinate these visits?")
print("name:", end='  ')
mostval_demo_contact = input()
print(f"What is {mostval_demo_contact}'s phone?", end='  ')
mostval_demo_contact_phone = input()
print(f"What is {mostval_demo_contact}'s email address?", end='  ')
mostval_demo_contact_email = input()

print(f"In which of your hospitals do you suggest for the {most_numerous_device} downloads?", end='  ')
mostnum_demo = input()
print(f"Which department will coordinate these downloads?", end='  ')
mostnum_demo_department = input()
print("Who is the best contact to coordinate these downloads?")
print ("name:", end='  ')
mostnum_demo_contact = input()
print(f"What is {mostnum_demo_contact}'s phone?", end='  ')
mostnum_demo_contact_phone = input()
print(f"What is {mostnum_demo_contact}'s email address?", end='  ')
mostnum_demo_contact_email = input()

print (f"Which hospitals do you suggest for the {next_most_numerous_device} download?", end='  ')
nextmost_demo = input()
print(f"Which department will coordinate these downloads?", end='  ')
nextmost_demo_department = input()
print("Who is the best contact to coordinate these downloads?")
print("name:", end='  ')
nextmost_demo_contact = input()
print(f"What is {nextmost_demo_contact}'s phone?", end='  ')
nextmost_demo_contact_phone = input()
print(f"What is {nextmost_demo_contact}'s email address?", end='  ')
nextmost_demo_contact_email = input()

print (f"Which hospital(s) do you suggest for the {third_most_numerous_device} downloads?", end='  ')
thirdmost_demo = input()
print(f"Which department will coordinate these downloads?", end='  ')
thirdmost_demo_department = input()
print("Who is the best contact to coordinate these downloads?")
print ("name:", end='  ')
thirdmost_demo_contact = input()
print(f"What is {thirdmost_demo_contact}'s phone?", end='  ')
thirdmost_demo_contact_phone = input()
print(f"What is {thirdmost_demo_contact}'s email address?", end='  ')
thirdmost_demo_contact_email = input()

print(f"We have recorded this information in our {email} data download project database:")

print("\n Summary of this Device Download Survey:\n")

print(f"Your most valuable device is the {top_device}.  We will coordinate our visit to \n \t download data from this device with {mostval_demo_contact} at {mostval_demo_hosp}.")
print(f"Your most numerous device is the {most_numerous_device}.  We will coordinate our visit to \n \t download data from this device with {mostnum_demo_contact} at {mostnum_demo}.")
print(f"Your next most numerous device is the {next_most_numerous_device}.  We will coordinate our visit to \n \t download data from this device with {nextmost_demo_contact} at {nextmost_demo}.")
print(f"Your third most numerous device is the {third_most_numerous_device}.  We will coordinate our visit to \n \t download data from this device with {thirdmost_demo_contact} at {thirdmost_demo}.\n")

print ("Thanks for your time!  This information will insure the right devices are scheduled for our download progect and efficiently removed from the network.\n \n")

print ("EMAIL INQUIRIES \n")
# send this email to {mostval_demo_contact_email}
print(f'{mostval_demo_contact}\n ')
print(f'{name} at {email} suggested contacting you about downloading data from \n your {top_device} device(s) at {mostval_demo_hosp}.')
print(f"Are you able to provide information about the vendor for the {top_device} device(s) ?")
demo1vendor = input ("y or n  ")
if demo1vendor == "y":
	print("Who is the vendor contact for that device?")
	print("name:", end='  ')
	mostval_vendor_contact = input()
	print(f"What is {mostval_vendor_contact}'s phone?", end='  ')
	mostval_vendor_contact_phone = input()
	print(f"What is {mostval_vendor_contact}'s email address?", end='  ')
	mostval_vendor_contact_email = input()

# send this email to {mostnum_demo_contact_email}
print(f'\n {mostnum_demo_contact}\n ')
print(f'{name} at {email} suggested contacting you about downloading data from \n your {most_numerous_device} at {mostnum_demo}.')
print(f"Are you able to provide information about the vendor for the {most_numerous_device} device(s) ? \n")
demo2vendor = input ("y or n  ")
if demo2vendor == "y":
	print("Who is the vendor contact for that device?")
	print("name:", end='  ')
	mostnum_vendor_contact = input()
	print(f"What is {mostnum_vendor_contact}'s phone?", end='  ')
	mostnum_vendor_contact_phone = input()
	print(f"What is {mostnum_vendor_contact}'s email address?", end='  ')
	mostnum_vendor_contact_email = input()

# send this  email to {nextmost_demo_contact_email}
print(f'\n {nextmost_demo_contact}\n ')
print(f'{name} at {email} suggested contacting you about downloading data from \n your {next_most_numerous_device} device(s) at {nextmost_demo}.')
print(f"Are you able to provide information about the vendor for the {next_most_numerous_device}? \n")
demo3vendor = input ("y or n  ")
if demo3vendor == "y":
	print("Who is the vendor contact for that device?")
	print("name:", end='  ')
	nextmost_vendor_contact = input()
	print(f"What is {nextmost_vendor_contact}'s phone?", end='  ')
	nextmost_vendor_contact_phone = input()
	print(f"What is {nextmost_vendor_contact}'s email address?", end='  ')
	nextmost_vendor_contact_email = input()

# send this email to {thirdmost_demo_contact_email}

print(f'\n {thirdmost_demo_contact}\n ')
print(f'{name} at {email} suggested contacting you about downloading data from \n your {third_most_numerous_device} device(s) at {thirdmost_demo}.')
print(f"Are you able to provide information about the vendor for the {third_most_numerous_device}? \n")
demo4vendor = input ("y or n  ")
if demo4vendor == "y":
	print("Who is the vendor contact for that device?")
	print("name:", end='  ')
	thirdmost_vendor_contact = input()
	print(f"What is {thirdmost_vendor_contact}'s phone?", end='  ')
	thirdmost_vendor_contact_phone = input()
	print(f"What is {thirdmost_vendor_contact}'s email address?", end='  ')
	thirdmost_vendor_contact_email = input()

# send this email to ewise_cyber

print (f"The following download input has arrived from {name}, {email} and phone {phone}:")
print (f"Coordinate downloads from {top_device} device(s) at {mostval_demo_hosp} with {mostval_demo_contact} \n \t in {mostval_demo_department}, {mostval_demo_contact_email} and phone {mostval_demo_contact_phone}.")
if demo1vendor == "y":
	print (f" \t The vendor contact is {mostval_vendor_contact}, {mostval_vendor_contact_email}, at {mostval_vendor_contact_phone}.")
print (f"Coordinate downloads from {most_numerous_device} device(s) at {mostnum_demo} with {mostnum_demo_contact} \n \t in {mostnum_demo_department}, {mostnum_demo_contact_email} and phone {mostnum_demo_contact_phone}.")
if demo2vendor == "y":
	print (f" \t The vendor contact is {mostnum_vendor_contact}, {mostnum_vendor_contact_email}, at {mostnum_vendor_contact_phone}.")
print (f"Coordinate downloads from {next_most_numerous_device} device(s) at {nextmost_demo} with {nextmost_demo_contact} \n \t in {nextmost_demo_department}, {nextmost_demo_contact_email}, and phone {nextmost_demo_contact_phone}.")
if demo3vendor == "y":
	print (f" \t The vendor contact is {nextmost_vendor_contact}, {nextmost_vendor_contact_email}, at {nextmost_vendor_contact_phone}.")
print (f"Coordinate downloads from {third_most_numerous_device} device(s) at {thirdmost_demo} with {thirdmost_demo_contact} \n \t in {thirdmost_demo_department}, {thirdmost_demo_contact_email} and phone {thirdmost_demo_contact_phone}.")
if demo4vendor == "y":
	print (f" \t The vendor contact is {thirdmost_vendor_contact}, {thirdmost_vendor_contact_email}, at {thirdmost_vendor_contact_phone}.")

#import boto3

"""GetSecretValue
    arn:aws:secretsmanager:us-east-1:064948119335:secret:Tech0710Access-U3h7gr 
    try:
        __version__ = get_distribution(__name__).version
        __version__ = get_distribution('aws_secretsmanager_caching').version
    except DistrubutionNotFound:
        __version__ = '0.0.0'

client = boto3.client(
'dynamodb',    
    arn:aws:secretsmanager:us-east-1:064948119335:secret:DSSdbAccess-fIkMja
	aws_access_key_id = ACCESS_KEY
	aws_secret_access_key = SECRET_ACCESS_KEY
	region=us-east-1
    try:
        __version__ = get_distribution(__name__).version
        __version__ = get_distribution('aws_secretsmanager_caching').version
    except DistrubutionNotFound:
        __version__ = '0.0.0'
)

dynamodb = boto3.resource('dynamodb')
    arn:aws:iam::032537808987:user/J10Developer

table=dynamodb.Table('device_std')

table.put_item(
				Item={
					'device': top_device,
					'hospital': mostval_hosp_demo,
					'contact': mostval_contact,
				}
)

dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table('contact_std')

table.put_item(
				Item={
					'device': top_device,
					'hospital': mostval_hosp_demo,
					'contact': mostval_contact,
					'vendor_contact': mostval_vendor_contact
				}
				
try: https:// <firewall-IP>/api/?type=config&action=get&key=<key>&xpath=/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address.. import PA.xls

table.put_item(
		try: from PA.xls get row1..rowZ for
				Item={
					'device': name,
					'ip_address': Ip netmask,
					'hospital': admin2,
					'contact': code,
					'vendor_contact': admin4
				}

Table.meta.client.get.waiter('table_exists').wait(TableName = 'devices')

Print(Table.item_count)

"""
