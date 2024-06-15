import sqlite3

conn =sqlite3.connect('youtube_video.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT FILED NOT NULL,
                time TEXT NOT NULL        
    )
 ''')

def list_videos():
    print("\n")
    print("*" * 70)
    cursor.execute(" SELECT * FROM videos")
    rows =cursor.fetchall()
    if not rows:
        print("no videos found")
    else:
        for row in rows:
            print(row)
    print("\n")
    print("*" * 70)

def add_videos(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ? ,time = ? WHERE id = ? ", (new_name,new_time,video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos where id = ?",(video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name =input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name,time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name =input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id =input("Enter the video id to delete: ")
            delete_videos(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

    conn.close()

if __name__ == '__main__':
    main()