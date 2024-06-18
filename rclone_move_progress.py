from rclone_python import rclone

rclone.move("data/", "os_dir", show_progress=False)
