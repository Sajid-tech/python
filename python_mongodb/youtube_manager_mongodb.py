from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb+srv://manoj:test123@youtubepy.85ab7lp.mongodb.net/?retryWrites=true&w=majority&appName=youtubepy")

# Not a good idea to include id and password in code files
#  tlsAllowInvalidCertificates=True - Not a good way to handle ssl

print(client)


db = client["ytmanagerdb"]
video_collection = db["videos"]

print(video_collection)

# we have to give all in object
def list_videos():
    print("\n")
    print("*"*70)
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, and Time: {video['time']}")
    print("\n")
    print("*"*70)
def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})
# "$set" means here i am gona give a new value, it is mongodb update operator , it has many one of them is "sum" too
def update_video(video_id,new_name,new_time):
    video_collection.update_one({'_id': ObjectId(video_id)},{"$set":{"name":new_name,"time":new_time}})
    

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to update: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()