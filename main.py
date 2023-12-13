from PIL import Image, ImageDraw, ImageFont  
import os  
  
# 定义图片文件夹路径和水印文本  
image_folder = '/Users/wangshubo/Desktop/wen'  
text = '号作品'  
# idx = 1
# 获取图片文件夹中的所有图片文件  
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]  
  
# 遍历每个图片文件  
for image_file in image_files:  
    # 打开图片文件  
    image = Image.open(os.path.join(image_folder, image_file))  
  
    # 创建画布和字体  
    draw = ImageDraw.Draw(image)  
    font = ImageFont.truetype('/Users/wangshubo/imgedit/ttf/字魂布丁体.ttf', 70)  
  
  
    idx = image_file.split('(')[1].split(')')[0]
    print(idx)
  
    # 添加水印文本  
    text_width, text_height = draw.textsize(str(idx)+text, font)  
    x = (image.width - text_width) // 2  
    y = (image.height - text_height) // 5*3  
    draw.text((x, y), str(idx)+text, font=font, fill=(255, 255, 255, 50), stroke_fill=(255, 140, 0,50), stroke_width=2)  
  
    # 保存带水印的图片文件  
    output_file = os.path.join(image_folder+"/out/", f'{str(idx)}.jpg')  
    image = image.convert('RGB')

    image.save(output_file)
    # idx+=1