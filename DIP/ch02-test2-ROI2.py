import cv2
import numpy as np

# 全域變數來追蹤滑鼠事件狀態
drawing = False
ix, iy = -1, -1
roi_list = []

def mergeROI(x,y):
    # Extract ROI from the image
    roi = img1[y:y+h, x:x+w, :]
    
    # Separate each channel image from an RGB image
    img1_r = np.zeros_like(roi)
    img1_g = np.zeros_like(roi)
    img1_b = np.zeros_like(roi)
    img1_r [:, :, 2] = roi[:, :, 2]
    img1_g [:, :, 1] = roi[:, :, 1]
    img1_b [:, :, 0] = roi[:, :, 0]
    
    # Concatenate horizontally
    upper_img = np.concatenate((roi, img1_r), axis=1)
    # Concatenate horizontally
    lower_img = np.concatenate((img1_g, img1_b), axis=1)
    # Concatenate vertically
    merged_img = np.concatenate((upper_img, lower_img), axis=0)



def draw_roi(event, x, y, flags, param):
    global ix, iy, drawing, image

    if event == cv2.EVENT_LBUTTONDOWN:
        # 開始繪製
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        # 當滑鼠移動且按下左鍵時，繪製臨時矩形
        if drawing:
            img_copy = image.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('Image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        # 結束繪製
        drawing = False
        
        # 確保座標正確
        x1, y1 = min(ix, x), min(iy, y)
        x2, y2 = max(ix, x), max(iy, y)
        
        # 繪製最終矩形
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # 詢問標籤
        label = input("請輸入此ROI的標籤: ")
        
        # 在矩形上方添加文字
        cv2.putText(image, label, (x1, y1-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # 儲存ROI資訊
        roi_list.append({
            'coords': (x1, y1, x2, y2),
            'label': label
        })
        
        cv2.imshow('Image', image)

def main():
    global image

    # 載入圖像
    image_path = "Breakfast.bmp"
    image = cv2.imread(image_path)

    if image is None:
        print("無法載入圖像，請檢查路徑是否正確")
        return

    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', draw_roi)
    
    # cv2.imshow('Image',image)
    # cv2.waitKey(0)
    ## 這邊用 loop攔截鍵盤事件做 r,s,q功能
    while True:
        cv2.imshow('Image', image)
        key = cv2.waitKey(1) & 0xFF ## wait 0.001秒 偵測按鍵盤

        # 按 'r' 重置圖像
        if key == ord('r'):
            image = cv2.imread(image_path)
            roi_list.clear()

        # 按 's' 儲存圖像
        elif key == ord('s'):
            save_path = input("請輸入儲存圖像的路徑: ")
            cv2.imwrite(save_path, image)
            print(f"圖像已儲存至 {save_path}")

        # 按 'q' 退出
        elif key == ord('q'):
            break

    cv2.destroyAllWindows()

    # 列印ROI資訊
    print("\nROI 資訊:")
    for idx, roi in enumerate(roi_list, 1):
        print(f"ROI {idx}: 標籤 = {roi['label']}, 座標 = {roi['coords']}")

if __name__ == "__main__":
    main()