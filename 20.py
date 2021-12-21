f = open("20.txt", "r")
raw_lines = f.read().splitlines()
algo = raw_lines[0]
image = raw_lines[2:]

def get_padded_image(image, pad):
    width = len(image[0])
    padded_image = []
    padded_image.append(pad * (width + 4))
    padded_image.append(pad * (width + 4))
    for row in image:
        padded_image.append(pad*2 + row + pad*2)
    padded_image.append(pad * (width + 4))
    padded_image.append(pad * (width + 4))
    return padded_image


def get_transformed_image(img):
    width = len(img[0])
    height = len(img)
    print("Height : ", height, "Widht: ", width)
    new_img = []
    for i in range(height-2):
        new_row = []
        for j in range(width-2):
            binary = img[i][j] + img[i][j+1] + img[i][j+2] + img[i+1][j] + img[i+1][j+1] + img[i+1][j+2] + img[i+2][j] + img[i+2][j+1] + img[i+2][j+2]
            new_binary = binary.replace("#", "1")
            new_binary2 = new_binary.replace(".", "0")
            idx = int(new_binary2, 2)
            new_row.append(algo[idx])
        new_img.append(''.join(new_row))
    return new_img

def count_lights(imge):
    total = 0
    for row in imge:
        for el in row:
            if el == "#":
                total += 1
    return total

if __name__ == "__main__":
    img2 = image
    for i in range(50):
        padding = ['.', '#']
        pi = get_padded_image(img2, padding[i%2])
        ti = get_transformed_image(pi)
        img2 = ti
    ans = count_lights(img2)
    print(ans)