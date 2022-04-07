#Owned By HasHCatz!
import requests
import urllib

#Username And Password Of imgflip.com.. *Use Your Own Acc When You Use This Brat!*
username = 'TROJ3N'
password = 'Nethika123'

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 \
    Safari/537.36'

#Requesting data From The API using 'GET' Method
print("""

▒█▀▄▀█ █▀▀ █▀▄▀█ █▀▀ 　 ▒█▀▀█ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ 
▒█▒█▒█ █▀▀ █░▀░█ █▀▀ 　 ▒█░▄▄ █▀▀ █░░█ █▀▀ █▄▄▀ █▄▄█ ░░█░░ █░░█ █▄▄▀ 
▒█░░▒█ ▀▀▀ ▀░░░▀ ▀▀▀ 　 ▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀░▀▀
Version: 0.1                                       Made By: HasHCatz
""")
while True:
    try:
        damn_data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
        memepics = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in damn_data]
    except:
        print("Some Bullshit Happened So Restarting('Check Your Network Connection')\n")
        continue
    print('\nHere is the list of available memes : \n')
    #Printing the List Of Meme Templates
    crap = 1
    for img in memepics:
        print(crap,img['name'])
        crap = crap+1

    #Getting Input
    while True:
        try:
            id = int(input('\nEnter the serial number of the meme : '))
            if id >100:
                print("\nEnter A Correct serial Numeber")
                continue
            else:
                break
        except:           
            print("\n\nEnter A Number Baaaaaakaaaaa!")
            continue
    txt1 = input('Enter first text : ')
    txt2 = input('Enter second text : ')

    URL = 'https://api.imgflip.com/caption_image'
    params = {
        'username':username,
        'password':password,
        'template_id':memepics[id-1]['id'],
        'text0':txt1,
        'text1':txt2
    }
    while True:
        try:
            response = requests.request('POST',URL,params=params).json()
            #Printing Whether Creating A meme was A success
            print(f"\n\nSuccessed = {response['success']}\nImage Link = {response['data']['url']}\nPage Link = {response['data']['page_url']}")
            break
        except:
            print("\nAaaaah An error occured when requesting Data..Trying Again!")
            continue

    while True:
        try:
            xoxo=int(input("\nWhat is The Lib That you Want To Use to Save The Meme?\n\n1 -  Urllib\n2 - Requests\n\nEnter The Number Of The Lib: "))
            if xoxo == 1:
                    #------------------------Saving The Meme Using urllib------------------------------------------#
                try:
                    print("\nProcess Is Starting Using Urllib Lib...\n")
                    opener = urllib.request.URLopener()
                    shitty_name = memepics[id-1]['name']
                    print("\nName Of The Meme That is Gonna save: "+shitty_name)
                    opener.addheader('User-Agent', userAgent)
                    filename, headers = opener.retrieve(response['data']['url'], memepics[id-1]['name']+'.jpg')
                    print("\n\nMeme was Saved Successfuly")
                    break
                except:
                    print("\nSomething's Wrong with the urllib So try again")
                    continue
            elif xoxo == 2:
                try:
            #------------------------------------Saving Image Using Requests---------------------------------#
                    print("\nProcess Is Starting Using Requests Lib...\n")
                    shitty_name = memepics[id-1]['name']
                    print("\nName Of The Meme That is Gonna save: "+shitty_name)
                    response = requests.get(f"{response['data']['url']}")
                    file = open(shitty_name+".jpg", "wb")
                    file.write(response.content)
                    lol = print("\nMeme was Saved Successfuly")
                    break
                except:
                    print("\nSomething's Wrong with the urllib So try again")
                    continue
            else:
                print("\nEnter A Correct Number")
                continue
        except:
            print("\nEnter A Number Not Letters you dipshit!")
            continue
    left=input('If you want to close the terminal Type Y else Press Enter\n>>>')
    left=left.lower()
    if left=="y":
        print("====>> Closing The Terminal! <<====")
        break
    elif not left=="y":
        print("\n------> Continuing <------")
        continue
    else:
        continue

