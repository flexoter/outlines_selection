# outlines_selection

Выделение контуров на изображении Азовского моря

Создал Буковшин Вадим

# Алгоритм

1. Загружаем изображение

   fn = 'sea.jpg' #an absolute path to an image file
   frame = cv.imread(fn)

 2. Меняем цветовую схему изображения на HSV, что позволит корректно использовать пороговые операции
 
   hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

3. Подбираем подходящую маску для исходного изображения, определяя соответствующие пороговые значения

   mask_lower = np.array([40, 60, 0])
   mask_upper = np.array([100, 120, 100])
   mask = cv.inRange(hsv, mask_lower, mask_upper)
  
4. Находим контуры изображения с помощью функции findContours

   cnts = cv.findContours(mask.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_NONE)[-2]

5. Получаем контур с наибольшим значением длины

   cnt = sorted(cnts, key=cv.contourArea)[-1]

6. Выполняем аппроксимацию найденного контура

   arclen = cv.arcLength(cnt, True)
   eps = 0.0005
   epsilon = arclen * eps
   approx = cv.approxPolyDP(cnt, epsilon, True)

7. Отображаем контур на исходном изображении

   canvas = frame.copy()
   cv.drawContours(canvas, [approx], -1, (0, 0, 255), 2, cv.LINE_AA)
   cv.imshow('res', canvas)
