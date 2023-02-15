import numpy as np
import cv2


# 转为灰度图并转为01矩阵
def pretreatment(path):
    im = cv2.imread(path)
    image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = np.array(image) // 255
    # print(im)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if im[i, j] == 0:
                im[i, j] = 1
            else:
                im[i, j] = 0
    return im


# 自动转为灰度图并转为01矩阵
def auto_pretreatment(img):
    X = []
    Y = []
    im = cv2.imread(img)
    image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = np.array(image) // 255
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if im[i, j] == 0:
                im[i, j] = 1
                X.append(j)
                Y.append(i)
            else:
                im[i, j] = 0
    min_X = min(X)-6
    max_X = max(X)+6
    min_Y = min(Y)
    max_Y = max(Y)
    img = image[min_Y: max_Y, min_X: max_X]
    img = cv2.resize(img, (32, 32))
    cv2.imwrite('images/text.png', img)

    im = im[min_Y: max_Y, min_X: max_X]
    im = cv2.resize(im, (32, 32))
    return im


def save_pic_to_file(filename, path='images/text.png', mode=0):
    """
    :param filename:
    :param path:
    :param mode: 0为手动, 其他为自动模式
    :return:
    """
    # path = 'D:/ML_num/images/text.png'
    if mode == 0:
        ret = pretreatment(path)
    else:
        ret = auto_pretreatment(path)
    # for i in ret:
    #     print(i)
    np.savetxt('testDigits/{}.txt'.format(filename), ret, fmt='%d')
    with open('testDigits/{}.txt'.format(filename)) as f:
        num = f.read()
    # 去除多余的空格
    num = num.replace(' ', '')
    with open('testDigits/{}.txt'.format(filename), 'w') as f:
        f.write(num)


if __name__ == '__main__':
    save_pic_to_file('8_2', 'images/text.png')
