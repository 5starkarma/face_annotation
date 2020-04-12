import cv2


def draw_bbox(event, x, y, flags, userdata):
    global top_left, btm_right

    if event == cv2.EVENT_LBUTTONDOWN:
        top_left = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        btm_right = [(x, y)]
        copy = source[
               top_left[0][1]:btm_right[0][1],
               top_left[0][0]:btm_right[0][0]
               ]
        cv2.imwrite("cropped.jpg", copy)
        cv2.rectangle(
            source,
            top_left[0],
            btm_right[0],
            (255, 255, 0),
            2,
            cv2.LINE_AA
        )


source = cv2.imread("sample.jpg", 1)
cv2.namedWindow("Window")
cv2.setMouseCallback("Window", draw_bbox)
k = 0

while k != 27:
    cv2.imshow("Window", source)
    cv2.putText(
        source,
        '''Choose top left corner, and drag,?''',
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )
    k = cv2.waitKey(20) & 0xFF

cv2.destroyAllWindows()
