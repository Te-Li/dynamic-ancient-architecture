from PIL import Image, ImageSequence

def resize_gif(input_path, output_path, new_size=(400, 300)):
    # 打开 GIF 文件
    with Image.open(input_path) as im:
        # 获取 GIF 的帧序列
        frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
        
        # 调整每一帧的尺寸
        resized_frames = [frame.resize(new_size, Image.LANCZOS) for frame in frames]
        
        # 保存调整尺寸后的 GIF
        resized_frames[0].save(output_path, save_all=True, append_images=resized_frames[1:], duration=im.info['duration'], loop=0)

# 示例用法
input_path = 'combined.gif'  # 替换为你的 GIF 文件路径
output_path = 'resized.gif'  # 输出文件路径
resize_gif(input_path, output_path)