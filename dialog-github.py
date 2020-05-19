# ewise_cyber = pgodston@ewiseinc.com

print("What is your first name?", end='  ')
name = input()
print("What is your business email address?", end='  ')

email = input()
print("What is your phone (where you have personal voicemail)?", end='  ')
phone = input()

print(f"So {name}, we can coordinate some demostrations with you at {email} or calling {phone}? Great!")
print("How many hospitals are there in your organization?", end='  ')
hospitals = input()
print("How many clinics are there in your organization?", end='  ')
clinics = input()

print("What is the #1 most important device in your organization?")
print("For example, Siemens 3T 70", end='  ')
top_device = input()
print("What are the top three (in order) highest volume devices in your organization?")
print("For example, GE MAC 800 ECG", end='  ')
most_numerous_device = input()
next_most_numerous_device = input()
third_most_numerous_device = input()

print(f"So we ought to do the demo on the {top_device} and on the {most_numerous_device} , the {next_most_numerous_device} and the {third_most_numerous_device}?  Okay.")

print(f"In which of your {hospitals} hospitals do you want to do the {top_device} demo?", end='  ')
mostval_demo_hosp = input()
print(f"Which department at the hospital will coordinate this demo?", end='  ')
mostval_demo_department = input()
print("Who is the best contact to coordinate things there?")
print("name:", end='  ')
mostval_demo_contact = input()
print(f"What is {mostval_demo_contact}'s phone?", end='  ')
mostval_demo_contact_phone = input()
print(f"What is {mostval_demo_contact}'s email address?", end='  ')
mostval_demo_contact_email = input()

print(f"In which hospital do you want to do the initial {most_numerous_device} demo?", end='  ')
mostnum_demo = input()
print(f"Which department at the hospital will coordinate this demo?", end='  ')
mostnum_demo_department = input()
print("Who is the best contact to coordinate things there?")
print ("name:", end='  ')
mostnum_demo_contact = input()
print(f"What is {mostnum_demo_contact}'s phone?", end='  ')
mostnum_demo_contact_phone = input()
print(f"What is {mostnum_demo_contact}'s email address?", end='  ')
mostnum_demo_contact_email = input()

print (f"In which hospital do you want to do the initial {next_most_numerous_device} demo?", end='  ')
nextmost_demo = input()
print(f"Which department at the hospital will coordinate this demo?", end='  ')
nextmost_demo_department = input()
print("Who is the best contact to coordinate things there?")
print("name:", end='  ')
nextmost_demo_contact = input()
print(f"What is {nextmost_demo_contact}'s phone?", end='  ')
nextmost_demo_contact_phone = input()
print(f"What is {nextmost_demo_contact}'s email address?", end='  ')
nextmost_demo_contact_email = input()

print (f"In which hospital do you want to do the initial {third_most_numerous_device} demo?", end='  ')
thirdmost_demo = input()
print(f"Which department at the hospital will coordinate this demo?", end='  ')
thirdmost_demo_department = input()
print("Who is the best contact to coordinate things there?")
print ("name:", end='  ')
thirdmost_demo_contact = input()
print(f"What is {thirdmost_demo_contact}'s phone?", end='  ')
thirdmost_demo_contact_phone = input()
print(f"What is {thirdmost_demo_contact}'s email address?", end='  ')
thirdmost_demo_contact_email = input()

print(f"We have recorded this information in our {email} preliminary project database:")

print("\n Summary of Demonstration Request:\n")

print(f"Your most valuable device is the {top_device}.  We will schedule installation of our sensor and \n \t demonstration date with {mostval_demo_contact} at {mostval_demo_hosp}.")
print(f"Your most numerous device is the {most_numerous_device}.  We will schedule installation of our \n \t sensor and demonstration date with {mostnum_demo_contact} at {mostnum_demo}.")
print(f"Your next most numerous device is the {next_most_numerous_device}.  We will schedule installation \n \t of our sensor and demonstration date with {nextmost_demo_contact} at {nextmost_demo}.")
print(f"Your third most numerous device is the {third_most_numerous_device}.  We will schedule installation \n \t of our sensor and demonstration date with {thirdmost_demo_contact} at {thirdmost_demo}.\n")

print ("Thanks for your time!  We will call to schedule the installations and demonstrations.\n \n")

print ("EMAIL INQUIRIES \n")
# send this email to {mostval_demo_contact_email}
print(f'{mostval_demo_contact}\n ')
print(f'{name} at {email} suggested contacting you about arranging installation of a malware sensor \n on a {top_device} at {mostval_demo_hosp}.')
print(f"Are you able to provide information about the vendor for the {top_device}?")
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
print(f'{name} at {email} suggested contacting you about arranging installation of a malware sensor \n on a {most_numerous_device} at {mostnum_demo}.')
print(f"Are you able to provide information about the vendor for the {most_numerous_device}? \n")
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
print(f'{name} at {email} suggested contacting you about arranging installation of a malware sensor \n on a {next_most_numerous_device} at {nextmost_demo}.')
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
print(f'{name} at {email} suggested contacting you about arranging installation of a malware sensor \n on a {third_most_numerous_device} at {thirdmost_demo}.')
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

print (f"The following demonstration request has arrived from {name}, {email} and phone {phone}:")
print (f"Coordinate a sensor demo on a {top_device} at {mostval_demo_hosp} with {mostval_demo_contact} \n \t in {mostval_demo_department}, {mostval_demo_contact_email} and phone {mostval_demo_contact_phone}.")
if demo1vendor == "y":
	print (f" \t The vendor contact is {mostval_vendor_contact}, {mostval_vendor_contact_email}, at {mostval_vendor_contact_phone}.")
print (f"Coordinate a sensor demo on a {most_numerous_device} at {mostnum_demo} with {mostnum_demo_contact} \n \t in {mostnum_demo_department}, {mostnum_demo_contact_email} and phone {mostnum_demo_contact_phone}.")
if demo2vendor == "y":
	print (f" \t The vendor contact is {mostnum_vendor_contact}, {mostnum_vendor_contact_email}, at {mostnum_vendor_contact_phone}.")
print (f"Coordinate a sensor demo on a {next_most_numerous_device} at {nextmost_demo} with {nextmost_demo_contact} \n \t in {nextmost_demo_department}, {nextmost_demo_contact_email}, and phone {nextmost_demo_contact_phone}.")
if demo3vendor == "y":
	print (f" \t The vendor contact is {nextmost_vendor_contact}, {nextmost_vendor_contact_email}, at {nextmost_vendor_contact_phone}.")
print (f"Coordinate a sensor demo on a {third_most_numerous_device} at {thirdmost_demo} with {thirdmost_demo_contact} \n \t in {thirdmost_demo_department}, {thirdmost_demo_contact_email} and phone {thirdmost_demo_contact_phone}.")
if demo4vendor == "y":
	print (f" \t The vendor contact is {thirdmost_vendor_contact}, {thirdmost_vendor_contact_email}, at {thirdmost_vendor_contact_phone}.")

import boto3

GetSecretValue
    arn:aws:iam::064948119335:user/Tech0710/Tech0710Access

client = boto3.client(
'dynamodb',
    arn:aws:iam::064948119335:user/Tech0710/DSSdbAccess
	aws_access_key_id = ACCESS_KEY
	aws_secret_access_key = SECRET_ACCESS_KEY
	region=us-east-1
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
				
Table.meta.client.get.waiter('table_exists').wait(TableName = 'devices')

Print(Table.item_count)




