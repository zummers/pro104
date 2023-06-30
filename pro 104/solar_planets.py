import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (90,100,),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (255,255,255)
            )
cv2.putText(img,
            "Mercury",
            (100,250,),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Venus",
            (200,200,),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Earth",
            (300,250,),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Mars",
            (400,200,),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Jupiter",
            (500,100,),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Saturn",
            (800,300,),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Uranus",
            (900,200,),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Neptune",
            (1100,300,),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )




cv2.imshow("output",img)
cv2.waitKey(0)
