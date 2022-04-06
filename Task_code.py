from numpy import min 
import pandas as pd
import cv2
#Creating path
img_path = 'images\pic1.jpg'
csv_path = 'images\colors.csv'
index = ['color','color_name','Hex','Red','Green','Blue']
df = pd.read_csv(csv_path, names=index, header=None) 

img = cv2.imread(img_path)
img = cv2.resize(img,(800,600)) 

#Intializing Coordinates
clicked = False
b = g = r = x_position = y_position = 0

# Read image in RGB color space
def get_color(Red, Green, Blue):
    min = 2000
    for i in range(len(df)):
        z = abs(Red - int(df.loc[i,'Red'])) + abs(Green - int(df.loc[i,'Green'])) + abs(Blue- int(df.loc[i,'Blue']))
        if z <= min:
            min = z
            col_name = df.loc[i,'color_name']
    return col_name


# Defined Function to OpenCV
def draw_function(occasion, x_coordinate, y_coordinate, flags, frame_work):
    if occasion == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, g, r, b, x_position, y_position 
        clicked = True
        x_position = x_coordinate
        y_position = y_coordinate
        b, g, r = img[y_coordinate, x_coordinate]
        b = int(b)
        g = int(g)
        r = int(r)
       
# Displaying img 
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function )
# Displaying Results on the Window
while True:
    cv2.imshow('image',img)
    if clicked == True:
        #cv2.rectangle(image, starting_point, Final_point, color, thickness)
        cv2.rectangle(img, (20,20), (1000,70), (b,g,r), -1)
        # Creating Text to display the RGB Values
        text = get_color(r, g, b) + '//Red = ' + str(r) + ' Green = ' + str(g) + ' Blue = ' + str(b)
        # cv2.put_text(image, text, )
        cv2.putText(img, text, (50,50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)

    if r + g +b >= 1000:
          cv2.putText(img, text, (50,50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break

        

cv2.destroyAllWindows() 