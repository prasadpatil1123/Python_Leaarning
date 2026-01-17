import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS video(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos():
    pass

def add_videos():
    pass

def update_videos():
    pass

def delete_videos():
    pass

def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)

        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_videos(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter video ID to Delete: ")
            delete_videos(video_id)

        elif choice == '5':
            break

        else: 
            print("Invalid choice! ")

        conn.close()


if __name__ == "__main__":
    main()