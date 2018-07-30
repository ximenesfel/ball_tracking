import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())

colorRanges = [
    ((29, 86, 6), (64,255,255), "green")
    ((57,68,0), (151,255,255), "blue")]

if not args.get("video", False):
    camera = cv2.VideoCapture()

else:
    camera = cv2.VideoCapture(args["video"])

while True:

    (grabbed, frame) = camera.read()

    if args.get("video") and not grabbed:
        break

    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for (lower, upper, colorName) in colorRanges:

        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        if len(cnts) > 0:

            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            (cX, cY) = ( int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]) )

            if radius > 10:

                cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
                cv2.putText(frame, colorName, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) && 0xFF

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

