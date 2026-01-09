
def load_data():
    pass

def add_video(video):
    pass

def update_video(video):
    pass

def delete_video(video):
    pass

def list_all_videos(video):
    pass

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
    
