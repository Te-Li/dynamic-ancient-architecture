from PIL import Image, ImageSequence

def combine_gifs(gif_paths, output_path):
    # 获取帧序列
    with Image.open(gif_paths[0]) as im:
        frames = [frame.copy() for frame in ImageSequence.Iterator(im)]

    # 遍历后续的 GIF 文件
    for path in gif_paths[1:]:
        with Image.open(path) as im:

            frames.extend([frame.copy() for frame in ImageSequence.Iterator(im)])

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=im.info['duration'], loop=0)

gif_paths = ['2.gif', '4.gif','5.gif']  # 替换为你的 GIF 文件路径
output_path = 'combined.gif'  # 输出文件路径
combine_gifs(gif_paths, output_path)
