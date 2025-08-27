import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader(
    download_videos=False,
    download_video_thumbnails=False,
    download_geotags=False,
    save_metadata=False,
    post_metadata_txt_pattern="",
    download_comments=False,
)

# Target username (public account only)
target_username = "paulina.thewarning"

# Load profile without logging in
try:
    # Load profile metadata without login (public profiles only)
    profile = instaloader.Profile.from_username(L.context, target_username)

    # Loop to download the latest 5 posts
    for index, post in enumerate(profile.get_posts()):
        if index >= 5:
            break
        L.download_post(post, target_username)

    print(f"✅ Downloaded {index + 1} latest posts from @{target_username}")

except instaloader.exceptions.ProfileNotExistsException:
    print(f"❌ Profile '{target_username}' does not exist.")
except instaloader.exceptions.PrivateProfileNotFollowedException:
    print(f"🔒 Profile '{target_username}' is private. Can't download without login.")
except Exception as e:
    print(f"⚠️ Something went wrong: {e}")
