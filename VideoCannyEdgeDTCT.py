import cv2

# Read the video file
video_capture = cv2.VideoCapture(r'messi.mp4')

# Check if the video file opened successfully
if not video_capture.isOpened():
    print("Error: Unable to open video file.")
    exit()

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()
    
    # Check if the frame was read successfully
    if not ret:
        # If the video ends, rewind it to the beginning
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
    # Display the frame
    cv2.imshow('Video', frame)
    
    # Convert to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Blur the frame for better edge detection
    frame_blur = cv2.GaussianBlur(frame_gray, (3, 3), 0)
    
    # Canny Edge Detection
    edges = cv2.Canny(image=frame_blur, threshold1=100, threshold2=200)  # Canny Edge Detection
    
    # Display Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', edges)
    
    # Break the loop if spacebar is pressed
    if cv2.waitKey(25) & 0xFF == ord(' '):
        break


# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()
