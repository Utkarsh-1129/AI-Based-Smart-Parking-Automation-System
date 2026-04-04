import numpy as np
import cvzone
import cv2
import pickle

# video feed
cap = cv2.VideoCapture('Backend/Input/carPark.mp4')

# Parking slot width & height
w, h = 107, 48

# Load positions
with open('Backend/Model/Positions', 'rb') as fil:
    lis = pickle.load(fil)

# ✅ Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# ✅ Create VideoWriter object
out = cv2.VideoWriter(
    'Backend/Output/output.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height)
)

def chkSpace(modified_img, img):
    free = len(lis)

    for pos in lis:
        x, y = pos

        crop = modified_img[y:y+h, x:x+w]
        cnt = cv2.countNonZero(crop)

        if cnt < 900:
            color = (0, 255, 0)  # Green → Free
        else:
            color = (0, 0, 255)  # Red → Occupied
            free -= 1

        # Draw rectangle
        cv2.rectangle(img, pos, (pos[0]+w, pos[1]+h), color, 2)

        # Put count text
        cvzone.putTextRect(
            img,
            str(cnt),
            (x, y+h-10),
            colorR=color,
            scale=1,
            thickness=2,
            offset=0
        )

    # Show total available spots
    cvzone.putTextRect(
        img,
        f'Total Available Spots: {free} / {len(lis)}',
        (100, 70),
        colorR=(0, 255, 0),
        scale=3,
        thickness=5,
        offset=0
    )


while True:

    # Loop video
    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
    #     cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    if not success:
        break

    # Image processing
    gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bImg = cv2.GaussianBlur(gImg, (3, 3), 1)
    tImg = cv2.adaptiveThreshold(
        bImg, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        25, 16
    )

    mImg = cv2.medianBlur(tImg, 5)
    kernel = np.ones((3, 3), np.uint8)
    modified_img = cv2.dilate(mImg, kernel, iterations=1)

    # Check parking spaces
    chkSpace(modified_img, img)

    # ✅ Save frame to output video
    out.write(img)

    # Show output
    cv2.imshow("Parking Detection", img)

    # Press 'q' to exit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


# ✅ Release resources
cap.release()
out.release()
cv2.destroyAllWindows()