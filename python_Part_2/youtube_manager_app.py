import json

def load_data():
    try:
        with open("youtube.txt", 'r') as file:
            test = json.load(file)
            # print(test)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    finally:
        pass
        
def save_data_helper(videos):
    with open("youtube.txt", 'w') as file:
        json.dump(videos, file)

def add_video(videos):
    name = input("Enter your Name: ")
    time = input("Enter your Time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    

def update_video(videos):
    # list_all_videos(videos)
    # index = int(input("Enter the video number to update: "))
    pass
    

def delete_video(videos):
    pass

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager App | Choose an option:")
        print("1. View all videos")
        print("2. Add a new video")
        print("3. Update video details")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        # print(videos)
        
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the application. Goodbye!")
                break
if __name__ == "__main__":
    main()
    
