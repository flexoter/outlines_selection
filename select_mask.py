#!/usr/bin/env python

# Project: outlines_selection
# File: select_mask
# Written by: Vadim Bukovshin
# Copyright (c) 2021
# -------------------------------------

"""
    This is the select_mask module.

    This module does selection of image outlines.
"""

import cv2 as cv
import numpy as np

fn = 'content/sea.jpg' # путь к файлу с картинкой
frame = cv.imread(fn)

hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

lower = np.array([40, 60, 0])
upper = np.array([100, 120, 100])

mask = cv.inRange(hsv, lower, upper)
res = cv.bitwise_and(frame, frame, mask = mask)

# find contours without approx
cnts = cv.findContours(mask.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_NONE)[-2]

# get the max-area contour
cnt = sorted(cnts, key=cv.contourArea)[-1]

# calc arclentgh
arclen = cv.arcLength(cnt, True)

# do approx
eps = 0.0005
epsilon = arclen * eps
approx = cv.approxPolyDP(cnt, epsilon, True)

# draw the result
canvas = frame.copy()
cv.drawContours(canvas, [approx], -1, (0,0,255), 2, cv.LINE_AA)
cv.imshow('res', canvas)
cv.imwrite('content/biggest_countered_sea.jpg', canvas)

cv.waitKey(0)
cv.destroyAllWindows()