import cv2


def drawBbox(action, x, y, flags, userdata):
    global topleft, bottomright
    if action == cv2.EVENT_LBUTTONDOWN:
        topleft = [(x, y)]
    elif action == cv2.EVENT_LBUTTONUP:
        bottomright = [(x, y)]
        copy = source[topleft[0][1]:bottomright[0][1], topleft[0][0]:bottomright[0][0]]
        cv2.imwrite("cropped.jpg", copy)
        cv2.rectangle(source, topleft[0], bottomright[0], (255, 255, 0), 2, cv2.LINE_AA)


source = cv2.imread("sample.jpg", 1)
cv2.namedWindow("Window")
cv2.setMouseCallback("Window", drawBbox)
k = 0
while k != 27:
    cv2.imshow("Window", source)
    cv2.putText(source, '''Choose top left corner, and drag,?''',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 2);
    k = cv2.waitKey(20) & 0xFF

cv2.destroyAllWindows()
