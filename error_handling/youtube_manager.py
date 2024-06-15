import json

# mostly json have two function load and dump , load means load the file , dump means save or dump the file
def load_data():
    try:
        #to open file
        with open('youtube.txt','r') as file:
            return json.load(file) # automatically feed whatever value in file and convert string into json also
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos): 
    print("\n")
    print("*" *70)
    for index, video in enumerate(videos, start=1): #start indexing frm 1
        print(f" {index}. {video['name']} , Duration: {video['time']} ")
    print("\n")
    print("*" *70)
def add_video(videos):
    name =input("Enter video name: ")
    time =input("Enter video time: ")
    videos.append({'name':name,"time": time}) # [{name: "" , time =" "},{}]
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos) # pass whole list
    index = int(input('Enter the videos no to update '))
    if 1<= index <= len(videos):
        name =input("Enter the new video name: ")
        time =input("Enter the new video time: ")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the videos no to delete '))

    if 1<=index <= len(videos):
        del videos[index-1]    # because enumarete strat from 1
        save_data_helper(videos)
    else:
        print("invalid video index selected")
# entry point call in last see
def main():

    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List a all youtube videos ")
        print("2. Add a Youtube video ")
        print("3. Update a Youtube video  details ")
        print("4. Delete a Youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()

# json work is to convert value in  string to json , json to string