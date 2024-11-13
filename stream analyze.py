import cv2
from google.colab.patches import cv2_imshow 

video_file_path = "/content/Animotica_3_4_17_24_44.mp4"

# Initialize video capture with the video file
video_capture = cv2.VideoCapture(video_file_path)

# Check if the video stream is opened successfully
if not video_capture.isOpened():
    print("Error opening video stream or file")
    exit()

while True:
    # Read a frame from the video stream
    ret, frame = video_capture.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Perform analysis on the frame here
    # Example: Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame using cv2_imshow for Colab
    cv2_imshow(gray) # Replaced cv2.imshow with cv2_imshow

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video_capture.release()
cv2.destroyAllWindows()