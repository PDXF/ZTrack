
import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[1;34m'   # Blue
Re = '\033[1;31m'   # Red
Gr = '\033[0;35m'   # Magenta
Ye = '\033[1;103m'   # Bright Yellow	
Blu = '\033[1;36m'  # Cyan
Mage = '\033[1;35m' # Magenta (Purple)
Cy = '\033[1;37m'   # White
Wh = '\033[1;90m'   # Gray

# Colors

# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()  # Call the function to display a banner
        return func(*args, **kwargs)  # Ensure the original function is called and returns its result
    return wrapper


@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target: {Gr}")  # Prompt for IP address input
    print()
    
    # Display the header for the IP address information
    print(f"{Wh}============= {Gr}SHOW INFORMATION FOR IP ADDRESS {Wh}=============")

    # API call to retrieve IP information
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API: IPWHOIS.IS
    ip_data = json.loads(req_api.text)  # Parse the JSON response
    time.sleep(2)

    # Display IP information
    print(f"{Wh}\n IP Target       : {Gr}{ip}")
    print(f"{Wh} Type IP         : {Gr}{ip_data['type']}")
    print(f"{Wh} Country         : {Gr}{ip_data['country']}")
    print(f"{Wh} Country Code    : {Gr}{ip_data['country_code']}")
    print(f"{Wh} City            : {Gr}{ip_data['city']}")
    print(f"{Wh} Continent       : {Gr}{ip_data['continent']}")
    print(f"{Wh} Continent Code  : {Gr}{ip_data['continent_code']}")
    print(f"{Wh} Region          : {Gr}{ip_data['region']}")
    print(f"{Wh} Region Code     : {Gr}{ip_data['region_code']}")
    print(f"{Wh} Latitude        : {Gr}{ip_data['latitude']}")
    print(f"{Wh} Longitude       : {Gr}{ip_data['longitude']}")

    # Extract latitude and longitude for map link
    lat = ip_data['latitude']
    lon = ip_data['longitude']
    print(f"{Wh} Maps            : {Gr}https://www.google.com/maps/@{lat},{lon},8z")
    
    # Additional information
    print(f"{Wh} EU              : {Gr}{ip_data['is_eu']}")
    print(f"{Wh} Postal          : {Gr}{ip_data['postal']}")
    print(f"{Wh} Calling Code    : {Gr}{ip_data['calling_code']}")
    print(f"{Wh} Capital         : {Gr}{ip_data['capital']}")
    print(f"{Wh} Borders         : {Gr}{ip_data['borders']}")
    print(f"{Wh} Country Flag    : {Gr}{ip_data['flag']['emoji']}")
    print(f"{Wh} ASN             : {Gr}{ip_data['connection']['asn']}")
    print(f"{Wh} ORG             : {Gr}{ip_data['connection']['org']}")
    print(f"{Wh} ISP             : {Gr}{ip_data['connection']['isp']}")
    print(f"{Wh} Domain          : {Gr}{ip_data['connection']['domain']}")
    print(f"{Wh} Timezone ID     : {Gr}{ip_data['timezone']['id']}")
    print(f"{Wh} ABBR            : {Gr}{ip_data['timezone']['abbr']}")
    print(f"{Wh} DST             : {Gr}{ip_data['timezone']['is_dst']}")
    print(f"{Wh} Offset          : {Gr}{ip_data['timezone']['offset']}")
    print(f"{Wh} UTC             : {Gr}{ip_data['timezone']['utc']}")
    print(f"{Wh} Current Time    : {Gr}{ip_data['timezone']['current_time']}")



@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Target Phone Number {Gr}Eg [+6281xxxxxxxxx] {Wh}: {Gr}")  # INPUT NUMBER PHONE
    default_region = "ID"  # DEFAULT NEGARA INDONESIA

    parsed_number = phonenumbers.parse(User_phone, default_region)  # VARIABLE PHONENUMBERS
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
    print(f"\n {Wh}Location             :{Gr} {location}")
    print(f" {Wh}Region Code          :{Gr} {region_code}")
    print(f" {Wh}Timezone             :{Gr} {timezoneF}")
    print(f" {Wh}Operator             :{Gr} {jenis_provider}")
    print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
    print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
    print(f" {Wh}International format :{Gr} {formatted_number}")
    print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Gr} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{Gr} This is another type of number")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Enter Username : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "YouTube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"},
        ]

        # Construct URLs and store results
        for platform in social_media:
            results[platform['name']] = platform['url'].format(username)

        # Display the results
        print(f"\n {Wh}========== {Gr}SOCIAL MEDIA LINKS {Wh}==========")
        for name, link in results.items():
            print(f" {Wh}{name:20}:{Gr} {link}")

    except Exception as e:
        print(f"{Wh}Error occurred: {Gr}{str(e)}")

        
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Username not found {Ye}!")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")


@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
    print(f"\n {Wh}[{Gr} + {Wh}] Your IP Adrress : {Gr}{Show_IP}")
    print(f"\n {Wh}==============================================")


# OPTIONS
options = [
    {
        'num': 1,
        'text': 'Track IP Address',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Retrieve IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': 'Track Phone Number',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'Track Username',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Exit Program',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # BANNER TOOLS
    clear()
    stderr.writelines(f"""
    
 ▄███████▄      ███        ▄████████    ▄████████  ▄████████    ▄█   ▄█▄ 
██▀     ▄██ ▀█████████▄   ███    ███   ███    ███ ███    ███   ███ ▄███▀ 
      ▄███▀    ▀███▀▀██   ███    ███   ███    ███ ███    █▀    ███▐██▀   
 ▀█▀▄███▀▄▄     ███   ▀  ▄███▄▄▄▄██▀   ███    ███ ███         ▄█████▀    
  ▄███▀   ▀     ███     ▀▀███▀▀▀▀▀   ▀███████████ ███        ▀▀█████▄    
▄███▀           ███     ▀███████████   ███    ███ ███    █▄    ███▐██▄   
███▄     ▄█     ███       ███    ███   ███    ███ ███    ███   ███ ▀███▄ 
 ▀████████▀    ▄████▀     ███    ███   ███    █▀  ████████▀    ███   ▀█▀ 
                          ███    ███                           ▀         


              {Wh}[ + ]  MADE BY  PDXD3V  [ + ]
    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠠⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡴⠒⠒⠒⠒⠒⠶⠦⠄⢹⣄⠀⠀⠑⠄⣀⡠⠤⠴⠒⠒⠒⠀⠀
⢇⠀⠀⠀⠀⠀⠀⠐⠋⠀⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀
⠈⢆⠀⠀⠀⠀⡤⠤⣄⠀⠀⠀⠀⡤⠤⢄⠀⠀⠀⠀⠀⣠⠃⠀
⠀⡀⠑⢄⡀⡜⠀⡜⠉⡆⠀⠀⠀⡎⠙⡄⠳⡀⢀⣀⣜⠁⠀⠀
⠀⠹⣍⠑⠀⡇⠀⢣⣰⠁⠀⠀⠀⠱⣠⠃⠀⡇⠁⣠⠞⠀⠀⠀
⠀⠀⠀⡇⠔⣦⠀⠀⠀⠈⣉⣀⡀⠀⠀⠰⠶⠖⠘⢧⠀⠀⠀⠀
⠀⠀⠰⠤⠐⠤⣀⡀⠀⠈⠑⣄⡁⠀⡀⣀⠴⠒⠀⠒⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢯⡉⠁⠀⠀⠀⠀⠉⢆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣞⡄⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀
    {Wh}--------------------------------
    {Wh}| {Gr}ZTrack - IP ADDRESS - TRACKER {Wh}|
    {Wh}|       {Gr}@CODE BY PDXD3V      {Wh}|
    {Wh}--------------------------------
    """)
    time.sleep(0.5)



def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}Select Option : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()
